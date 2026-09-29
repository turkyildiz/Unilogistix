"""Review candidate: exact received-copy restore into owned network-isolated containers.

Custody JSON comes exclusively from an existing approved collector on stdin. This
program never opens a token/share file or derives a production API endpoint.
"""
import argparse
from contextlib import contextmanager
import resource
import shutil
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import re
import uuid
from backup_common import config, manifest, trusted_json, validate_snapshot, no_symlinks, timestamp
import datetime

BAO_IMAGE='openbao/openbao@sha256:11fd73a2102cda9c55d5d881a8c3210303146a7ec1e8ac76f526e175c6d24641'
PYTHON_IMAGE='python@sha256:9e9fde4d32eedce0b661d9ab91e826b62dddf28e928c230ec55f1866cac66b01'


# Required operational restore input: declarative audit configuration is not
# reconstructed from the raft snapshot. This sink uses NEW disposable tmpfs.
AUDIT_CONFIG='audit "file" "unilogistix-file" {\n description = "Fleet audit with HMAC-protected values"\n options {\n  file_path = "/openbao/data/unilogistix-audit.jsonl"\n  mode = "0600"\n }\n}\n'

class CleanupFailure(RuntimeError):
    pass

@contextmanager
def protected_staging():
    path=tempfile.mkdtemp(prefix='uni-received-restore-')
    retain=False
    try:
        yield path
    except CleanupFailure:
        retain=True
        raise
    finally:
        if not retain:shutil.rmtree(path)


class DriverFailure(RuntimeError):
    def __init__(self,diagnostic):
        self.diagnostic=diagnostic
        super().__init__('driver_'+diagnostic['stage'])

def safe_diagnostic(value):
    stages={'startup','initialize_target','restore_archive','original_custody_unseal','restored_canary','restored_audit','restored_audit_metadata','restored_bootstrap_role','restored_bootstrap_secret_id','restored_bootstrap_login','restored_bootstrap_canary','restored_bootstrap_denials','restored_bootstrap_revoke','restored_bootstrap_revoked_denial','restored_vakf_roles'}
    codes={'custody_shape','custody_bound','disposable_unavailable','target_not_fresh','disposable_not_ready','restored_seal_mismatch','http_failure','restored_identity_mismatch','restored_vakf_binding_mismatch','restored_audit_mismatch','isolated_restore_failed'}
    if not isinstance(value,dict) or value.get('stage') not in stages or value.get('code') not in codes:return None
    result={'stage':value['stage'],'code':value['code']}
    seal=value.get('seal_metadata',{})
    result['seal_metadata']={k:v for k,v in seal.items() if (k=='sealed' and type(v) is bool) or (k in {'n','t','progress'} and type(v) is int and 0<=v<=255)} if isinstance(seal,dict) else {}
    result['unseal_step']=value.get('unseal_step') if type(value.get('unseal_step')) is int and 0<=value['unseal_step']<=3 else None
    result['http_status']=value.get('http_status') if type(value.get('http_status')) is int and 400<=value['http_status']<=599 else None
    return result

def command(args, *, data=None, timeout=30):
    result=subprocess.run(args,input=data,capture_output=True,timeout=timeout)
    if result.returncode:
        if '/driver.py' in args:
            try:
                failed=json.loads(result.stdout)
                diagnostic=safe_diagnostic(failed)
                if diagnostic:raise DriverFailure(diagnostic)
            except (ValueError,TypeError):pass
        raise ValueError('command_failed')
    return result.stdout


def cleanup(name, marker):
    result=subprocess.run(['docker','inspect','--format','{{index .Config.Labels "unilogistix.restore-run"}}',name],capture_output=True,timeout=15)
    if result.returncode:
        if b'No such object' in result.stderr or b'No such container' in result.stderr:return
        raise ValueError('cleanup_inspection_failed')
    if result.stdout.decode().strip()!=marker:raise ValueError('cleanup_ownership_mismatch')
    command(['docker','rm','-f',name])


def validate_profile(profile):
    if not isinstance(profile,list) or not 1<=len(profile)<=8:raise ValueError('qualification_profile_required')
    seen=set()
    for b in profile:
        if not isinstance(b,dict) or set(b)!={'role','path','expected_version','expected_fields','denials'}:raise ValueError('profile_shape')
        if not re.fullmatch(r'[a-z0-9-]{1,80}',b['role']) or b['role'] in seen:raise ValueError('profile_role')
        seen.add(b['role'])
        if not re.fullmatch(r'unilogistix/data/[a-z0-9/_-]{1,180}',b['path']):raise ValueError('profile_path')
        if type(b['expected_version']) is not int or b['expected_version']<1:raise ValueError('profile_version')
        fields=b['expected_fields']
        if not isinstance(fields,dict) or not fields or len(fields)>12:raise ValueError('profile_fields')
        # Binding metadata only: never accept credential values as expectations.
        if not set(fields)<={'project_ref','role','environment','cell','status'} or any(not isinstance(v,str) or not re.fullmatch(r'[a-zA-Z0-9_-]{1,100}',v) for v in fields.values()):raise ValueError('profile_fields')
        if not isinstance(b['denials'],list) or len(b['denials'])!=3:raise ValueError('profile_denials')
        if len({d.get('path') for d in b['denials'] if isinstance(d,dict)})!=3 or sum(d.get('method')=='LIST' for d in b['denials'] if isinstance(d,dict))!=1:raise ValueError('profile_denials')
        for d in b['denials']:
            if set(d)!={'path','method'} or d['method'] not in (None,'LIST') or not re.fullmatch(r'unilogistix/(data|metadata)/[a-z0-9/_-]{1,180}',d['path']):raise ValueError('profile_denial')
    return profile

def run(archive, receipt, configuration, custody):
    c=config(configuration,trusted_uid=os.getuid())
    profile=validate_profile(c.get('qualification_bindings'))
    receipt=trusted_json(receipt,trusted_uid=os.getuid())
    if set(receipt)!={'status','manifest','received_at'} or receipt['status']!='stored_unverified':
        raise ValueError('receipt_mismatch')
    m=manifest(receipt['manifest'],c)
    received=timestamp(receipt['received_at'])
    if not timestamp(m['captured_at'])<=received<=datetime.datetime.now(datetime.timezone.utc):
        raise ValueError('receipt_time_mismatch')
    if m['source_version']!='2.6.2' or Path(archive).name!=m['capture_id']+'.snap':
        raise ValueError('archive_identity_mismatch')
    no_symlinks(archive)
    # Require images already installed; no implicit pull during custody handling.
    for image in (BAO_IMAGE,PYTHON_IMAGE):command(['docker','image','inspect',image])
    marker=uuid.uuid4().hex
    vault='uni-restore-'+marker
    driver=vault+'-driver'
    with protected_staging() as temporary:
        root=Path(temporary);inputs=root/'input';inputs.mkdir(mode=0o700)
        source=Path(archive)
        if not source.is_file() or source.stat().st_size>64*1024*1024:raise ValueError('archive_bound')
        with source.open('rb') as incoming, (inputs/'archive.snap').open('wb') as outgoing:
            copied=0
            while block:=incoming.read(65536):
                copied+=len(block)
                if copied>64*1024*1024:raise ValueError('archive_bound')
                outgoing.write(block)
        digest,size=validate_snapshot(inputs/'archive.snap')
        if digest!=m['sha256'] or size!=m['bytes']:raise ValueError('archive_receipt_digest_mismatch')
        (inputs/'receipt.json').write_text(json.dumps(receipt))
        (inputs/'profile.json').write_text(json.dumps(profile))
        conf=root/'config.hcl'
        conf.write_text(AUDIT_CONFIG+'disable_mlock=true\napi_addr="http://127.0.0.1:8200"\ncluster_addr="https://127.0.0.1:8201"\nstorage "raft" {\n path="/data"\n node_id="isolated-restore"\n}\nlistener "tcp" {\n address="127.0.0.1:8200"\n tls_disable=1\n}\n')
        conf.chmod(0o644)
        try:
            command(['docker','run','--pull=never','--name',vault,'--label','unilogistix.restore-run='+marker,
                '--network','none','--read-only','--cap-drop','ALL','--security-opt','no-new-privileges',
                '--user','100:1000','--memory','512m','--memory-swap','512m','--ulimit','core=0:0','--cpus','1','--pids-limit','128',
                '--tmpfs','/data:uid=100,gid=1000,mode=0700','--tmpfs','/openbao/data:uid=100,gid=1000,mode=0700','--tmpfs','/tmp',
                '-v',str(conf)+':/config.hcl:ro','--entrypoint','bao','-d',BAO_IMAGE,'server','-config=/config.hcl'])
            inspected=json.loads(command(['docker','inspect',vault]))[0]
            if inspected['HostConfig']['NetworkMode']!='none' or inspected['HostConfig']['PortBindings']:
                raise ValueError('container_isolation_mismatch')
            output=command(['docker','run','--pull=never','--name',driver,'--label','unilogistix.restore-run='+marker,
                '--network','container:'+vault,'--user',str(os.getuid())+':'+str(os.getgid()),'--read-only','--cap-drop','ALL','--security-opt','no-new-privileges',
                '--memory','256m','--memory-swap','256m','--ulimit','core=0:0','--cpus','1','--pids-limit','64','-i',
                '-v',str(inputs)+':/input:ro','-v',str(Path(__file__).with_name('restore_worker.py'))+':/driver.py:ro',
                PYTHON_IMAGE,'python','/driver.py'],data=custody,timeout=180)
            result=json.loads(output)
            expected_bindings=[{'role':b['role'],'source_version':b['expected_version'],'active_binding_match':True,
                'configured_denials_passed':True,'revoked_token_denied':True} for b in profile]
            if result!={'audit_available':True,'bindings':expected_bindings,'status':'PASS','source_version':'2.6.2','original_3_of_5_unseal':True,
                'cluster_identity_match':True,'canary_read':True,'scoped_denials':True}:
                raise ValueError('driver_result_mismatch')
            return result|{'archive_sha256':digest,'archive_bytes':size,'capture_id':m['capture_id'],'cleanup':'completed'}
        except DriverFailure as exc:
            try:
                inspected=json.loads(command(['docker','inspect',vault]))[0]
                if inspected.get('Config',{}).get('Labels',{}).get('unilogistix.restore-run')==marker:
                    logs=subprocess.run(['docker','logs','--tail','100',vault],capture_output=True,timeout=10)
                    text=(logs.stdout+logs.stderr).decode(errors='replace').lower()
                    exc.diagnostic['log_categories']={k:(needle in text) for k,needle in {
                        'permission_denied':'permission denied',
                        'read_only_filesystem':'read-only file system','file_missing':'no such file or directory',
                        'audit_duplicate':'already enabled','audit_description_mismatch':'different descriptions','audit_options_mismatch':'missing option','post_unseal_error':'post-unseal setup failed',
                        'raft_no_peer':'cannot find peer','sealed_error':'vault is sealed'}.items()}
                    exc.diagnostic['log_categories']['audit_error']=any('audit' in line and ('error' in line or 'failed' in line) for line in text.splitlines())
            except Exception:pass
            raise
        finally:
            # Clean only exact names bearing this invocation's random ownership label.
            failed=False
            for name in (driver,vault):
                try:cleanup(name,marker)
                except Exception:failed=True
            if failed:raise CleanupFailure('owned_cleanup_incomplete')


def main():
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive',required=True)
    parser.add_argument('--receipt',required=True)
    parser.add_argument('--config',required=True)
    args=parser.parse_args()
    try:
        custody=sys.stdin.buffer.read(32_769)
        if len(custody)>32_768:raise ValueError('custody_bound')
        # Validate JSON before any container starts; do not print values on failure.
        value=json.loads(custody)
        if not isinstance(value,dict) or set(value)!={'shares','operator_token'}:raise ValueError('custody_shape')
        result=run(args.archive,args.receipt,args.config,custody)
        print(json.dumps(result));return 0
    except Exception:
        print('{"status":"FAIL","code":"isolated_restore_failed_or_cleanup_required"}')
        return 1

if __name__=='__main__':sys.exit(main())
