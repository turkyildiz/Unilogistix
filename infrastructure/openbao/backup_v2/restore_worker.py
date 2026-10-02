"""Runs only inside the disposable vault's isolated network namespace.

No remote endpoint/configuration option. All custody arrives through bounded stdin.
"""
import json
from pathlib import Path
import sys
import time
import urllib.error
import urllib.request

STAGE='startup'
SEAL_DIAGNOSTIC={}
UNSEAL_STEP=0
FAILURE_HTTP_STATUS=None
BASE = 'http://127.0.0.1:8200/v1/'

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs):
        raise ValueError('redirect_refused')

class Denied(Exception):
    pass


def api(path, body=None, token=None, raw=False, method=None):
    global FAILURE_HTTP_STATUS
    headers = {'Content-Type': 'application/octet-stream' if raw else 'application/json'}
    if token:
        headers['X-Vault-Token'] = token
    data = body if raw else json.dumps(body).encode() if body is not None else None
    request = urllib.request.Request(BASE+path, data=data, headers=headers, method=method)
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}),NoRedirect())
    try:
        with opener.open(request, timeout=30) as response:
            data = response.read(1_048_577)
            if len(data) > 1_048_576:
                raise ValueError('response_bound')
            return json.loads(data) if data else {}
    except urllib.error.HTTPError as exc:
        code = exc.code
        FAILURE_HTTP_STATUS=code
        exc.close()
        if code == 403:
            raise Denied() from None
        raise ValueError('http_failure') from None


def qualify_bindings(operator, profile):
    results=[]
    for binding in profile:
        role=binding['role'];base='auth/unilogistix-approle/role/'+role
        rid=api(base+'/role-id',token=operator)['data']['role_id']
        sid=api(base+'/secret-id',{},operator)['data']['secret_id']
        token=api('auth/unilogistix-approle/login',{'role_id':rid,'secret_id':sid})['auth']['client_token']
        own=binding['path']
        try:
            response=api(own,token=token)['data'];bundle=response['data']
            if response['metadata']['version']!=binding['expected_version'] or any(bundle.get(k)!=v for k,v in binding['expected_fields'].items()):
                raise ValueError('restored_vakf_binding_mismatch')
            for denial in binding['denials']:
                try:api(denial['path'],token=token,method=denial['method'])
                except Denied:continue
                raise ValueError('restored_vakf_denial_missing')
        finally:
            api('auth/token/revoke-self',{},token)
        try:api(own,token=token)
        except Denied:pass
        else:raise ValueError('restored_vakf_revocation_missing')
        results.append({'role':role,'source_version':binding['expected_version'],'active_binding_match':True,
                        'configured_denials_passed':True,'revoked_token_denied':True})
    return results


def ready():
    for _ in range(60):
        try:
            health=api('sys/health')
            if health.get('sealed') is False and health.get('version')=='2.6.2':
                return health
        except Exception:
            pass
        time.sleep(.25)
    raise ValueError('disposable_not_ready')


def qualify(custody, manifest, profile):
    global STAGE,SEAL_DIAGNOSTIC,UNSEAL_STEP
    # Only an already reviewed custody collector may provide these values.
    if set(custody) != {'shares', 'operator_token'} or not isinstance(custody['shares'],list) or len(custody['shares']) != 3:
        raise ValueError('custody_shape')
    if any(not isinstance(v,str) or not 10 <= len(v) <= 1024 for v in custody['shares']+[custody['operator_token']]):
        raise ValueError('custody_shape')
    for _ in range(60):
        try:
            status=api('sys/seal-status')
            break
        except Exception:
            time.sleep(.25)
    else:
        raise ValueError('disposable_unavailable')
    if status.get('initialized') is not False:
        raise ValueError('target_not_fresh')
    STAGE='initialize_target'
    initial=api('sys/init', {'secret_shares':5,'secret_threshold':3})
    for ephemeral in initial['keys_base64'][:3]:
        api('sys/unseal', {'key':ephemeral})
    ready()
    archive=Path('/input/archive.snap').read_bytes()
    if not 0 < len(archive) <= 64*1024*1024:
        raise ValueError('archive_bound')
    STAGE='restore_archive'
    api('sys/storage/raft/snapshot-force', archive, initial['root_token'], raw=True)
    for _ in range(60):
        status=api('sys/seal-status')
        SEAL_DIAGNOSTIC={k:status.get(k) for k in ('sealed','t','n','progress')}
        if status.get('sealed') is True and status.get('t')==3 and status.get('n')==5:
            break
        time.sleep(.25)
    else:
        raise ValueError('restored_seal_mismatch')
    STAGE='original_custody_unseal'
    for step,share in enumerate(custody['shares'],1):
        UNSEAL_STEP=step
        try:status=api('sys/unseal', {'key':share})
        except Exception:
            try:status=api('sys/seal-status')
            except Exception:status={}
            SEAL_DIAGNOSTIC={k:status.get(k) for k in ('sealed','t','n','progress')}
            raise
        SEAL_DIAGNOSTIC={k:status.get(k) for k in ('sealed','t','n','progress')}
    health=ready()
    if health.get('sealed') is not False or health.get('version')!='2.6.2' or health.get('cluster_id')!=manifest['cluster_id']:
        raise ValueError('restored_identity_mismatch')
    operator=custody['operator_token']
    STAGE='restored_audit'
    audits=api('sys/audit',token=operator)
    STAGE='restored_audit_metadata'
    audit=audits.get('data',{}).get('unilogistix-file/',{})
    if audit.get('type')!='file' or audit.get('options',{}).get('file_path')!='/openbao/data/unilogistix-audit.jsonl':
        raise ValueError('restored_audit_mismatch')
    STAGE='restored_canary'
    if api('unilogistix/data/bootstrap/health', token=operator)['data']['data'].get('status')!='ready':
        raise ValueError('canary_mismatch')
    # Exercise the restored role/policy, not a newly invented permissive policy.
    STAGE='restored_bootstrap_role'
    role='auth/unilogistix-approle/role/bootstrap-reader'
    rid=api(role+'/role-id',token=operator)['data']['role_id']
    STAGE='restored_bootstrap_secret_id'
    sid=api(role+'/secret-id',{},operator)['data']['secret_id']
    STAGE='restored_bootstrap_login'
    token=api('auth/unilogistix-approle/login',{'role_id':rid,'secret_id':sid})['auth']['client_token']
    try:
        STAGE='restored_bootstrap_canary'
        if api('unilogistix/data/bootstrap/health',token=token)['data']['data'].get('status')!='ready':
            raise ValueError('scoped_canary_mismatch')
        STAGE='restored_bootstrap_denials'
        for path,body in [('secret/data/__restore_probe__',None),('unilogistix/data/__restore_probe__',None),
                          ('unilogistix/data/bootstrap/health',{'data':{'status':'must-deny'}}),('sys/policies/acl',None),('auth/token/revoke-self',{})]:
            try:
                api(path,body,token)
            except Denied:
                continue
            raise ValueError('scoped_denial_missing')
    finally:
        previous_stage=STAGE
        STAGE='restored_bootstrap_revoke'
        api('auth/token/revoke',{'token':token},operator)
        STAGE=previous_stage
    STAGE='restored_bootstrap_revoked_denial'
    try:api('unilogistix/data/bootstrap/health',token=token)
    except Denied:pass
    else:raise ValueError('scoped_denial_missing')
    STAGE='restored_vakf_roles'
    bindings=qualify_bindings(operator,profile)
    return {'audit_available':True,'bindings':bindings,'status':'PASS','source_version':'2.6.2','original_3_of_5_unseal':True,
            'cluster_identity_match':True,'canary_read':True,'scoped_denials':True}


def main():
    try:
        content=sys.stdin.buffer.read(32_769)
        if len(content)>32_768:raise ValueError('custody_bound')
        custody=json.loads(content)
        manifest=json.loads(Path('/input/receipt.json').read_text())['manifest']
        profile=json.loads(Path('/input/profile.json').read_text())
        result=qualify(custody,manifest,profile)
        print(json.dumps(result))
        return 0
    except Exception as exc:
        allowed={'custody_shape','custody_bound','disposable_unavailable','target_not_fresh','disposable_not_ready','restored_seal_mismatch','http_failure','restored_identity_mismatch','restored_vakf_binding_mismatch','restored_audit_mismatch'}
        code=str(exc) if isinstance(exc,ValueError) and str(exc) in allowed else 'isolated_restore_failed'
        print(json.dumps({'status':'FAIL','code':code,'stage':STAGE,'seal_metadata':SEAL_DIAGNOSTIC,'unseal_step':UNSEAL_STEP,'http_status':FAILURE_HTTP_STATUS}))
        return 1

if __name__=='__main__':sys.exit(main())
