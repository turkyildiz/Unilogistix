"""Explicit real synthetic fixture: no existing credential files or live API calls."""
import base64
import hashlib
import json
from pathlib import Path
import tempfile
import time
import uuid
from unittest.mock import patch
import restore_qualification as h
from backup_common import utcnow


MISMATCHED_AUDIT_CONFIG='audit "file" "unilogistix-file" {\n options {\n file_path="/openbao/data/unilogistix-audit.jsonl"\n }\n}\n'
SOURCE_AUDIT_CONFIG='audit "file" "unilogistix-file" {\n description = "Fleet audit with HMAC-protected values"\n options {\n  file_path = "/openbao/data/unilogistix-audit.jsonl"\n  mode = "0600"\n }\n}\n'

def main():
 marker=uuid.uuid4().hex;name='uni-synthetic-'+marker;driver=name+'-driver'
 rootcode=Path(__file__).parent
 with tempfile.TemporaryDirectory(prefix='uni-synthetic-fixture-') as directory:
  root=Path(directory);conf=root/'config.hcl'
  conf.write_text(SOURCE_AUDIT_CONFIG+'disable_mlock=true\napi_addr="http://127.0.0.1:8200"\ncluster_addr="https://127.0.0.1:8201"\nstorage "raft" {\n path="/data"\n node_id="synthetic-source"\n}\nlistener "tcp" {\n address="127.0.0.1:8200"\n tls_disable=1\n}\n');conf.chmod(0o644)
  try:
   h.command(['docker','run','--pull=never','--name',name,'--label','unilogistix.restore-run='+marker,
    '--network','none','--read-only','--cap-drop','ALL','--security-opt','no-new-privileges','--user','100:1000',
    '--tmpfs','/data:uid=100,gid=1000,mode=0700','--tmpfs','/openbao/data:uid=100,gid=1000,mode=0700','--tmpfs','/tmp','-v',str(conf)+':/config.hcl:ro',
    '--entrypoint','bao','-d',h.BAO_IMAGE,'server','-config=/config.hcl'])
   time.sleep(2)
   payload=json.loads(h.command(['docker','run','--pull=never','--name',driver,'--label','unilogistix.restore-run='+marker,
     '--network','container:'+name,'--read-only','--cap-drop','ALL','--security-opt','no-new-privileges',
     '-v',str(rootcode)+':/work:ro','-w','/work',h.PYTHON_IMAGE,'python','synthetic_source.py'],timeout=90))
   data=base64.b64decode(payload['archive']);capture=uuid.uuid4().hex;archive=root/(capture+'.snap');archive.write_bytes(data)
   m={'protocol':1,'source_id':'shared-fleet','cluster_id':payload['cluster_id'],'source_version':'2.6.2',
      'capture_id':capture,'captured_at':utcnow(),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
   receipt=root/(capture+'.receipt.json');receipt.write_text(json.dumps({'status':'stored_unverified','manifest':m,'received_at':utcnow()}));receipt.chmod(0o600)
   profile=[{'role':'vakf-staging-us-'+service,'path':'unilogistix/data/vakf/staging/us/'+service,'expected_version':2,'expected_fields':{'project_ref':'synthetic-project','role':'vakf_staging_'+kind+'_runtime','environment':'staging','cell':'us','status':'active'},'denials':[{'path':'unilogistix/data/vakf/prod/us/'+service,'method':None},{'path':'unilogistix/data/vakf/admin/cloudflare','method':None},{'path':'unilogistix/metadata/vakf','method':'LIST'}]} for service,kind in [('db-api','api'),('db-worker','worker')]]
   c={'qualification_bindings':profile,'source_id':'shared-fleet','cluster_id':payload['cluster_id'],'allowed_versions':['2.6.2'],'storage_root':str(root),'capture_root':str(root),'retain_candidates':28}
   (root/'config.json').write_text(json.dumps(c));(root/'config.json').chmod(0o600)
   # Only generated fixture custody/capture binding is injected. The actual local
   # entry, config ownership checks, Docker, HTTP and restore are exercised.
   with patch.object(h,'AUDIT_CONFIG',''):
    try:h.run(archive,receipt,root/'config.json',json.dumps(payload['custody']).encode())
    except RuntimeError as exc:
     if str(exc)!='driver_restored_audit_metadata':raise
    else:raise AssertionError('missing_audit_config_must_fail')
   with patch.object(h,'AUDIT_CONFIG',MISMATCHED_AUDIT_CONFIG):
    try:h.run(archive,receipt,root/'config.json',json.dumps(payload['custody']).encode())
    except h.DriverFailure as exc:
     assert exc.diagnostic['stage']=='original_custody_unseal'
     assert exc.diagnostic['code']=='disposable_not_ready'
     assert exc.diagnostic['seal_metadata']['sealed'] is False
     assert exc.diagnostic['http_status']==429
     assert exc.diagnostic['log_categories']['audit_description_mismatch'] is True
    else:raise AssertionError('mismatched_audit_config_must_fail')
   result=h.run(archive,receipt,root/'config.json',json.dumps(payload['custody']).encode())
   print(json.dumps({'mismatched_audit_config_denied':True,'missing_declarative_config_denied':True,'qualification':'real_synthetic_only','status':result['status'],'vault_version':'2.6.2',
      'audit_available':result['audit_available'],'original_3_of_5_unseal':result['original_3_of_5_unseal'],'scoped_denials':result['scoped_denials'],'bindings':result['bindings']}))
  finally:
   h.cleanup(driver,marker);h.cleanup(name,marker)

if __name__=='__main__':
 try:main()
 except Exception as exc:
  code=str(exc) if isinstance(exc,RuntimeError) and str(exc).startswith('driver_') else 'synthetic_restore_failed'
  print(json.dumps({'status':'FAIL','code':code}))
  raise SystemExit(1)
