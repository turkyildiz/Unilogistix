import subprocess
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
import restore_worker as worker
import restore_qualification as host

class RestoreCandidateTests(unittest.TestCase):
 def exercise(self, wrong_cluster=False, allow_denied=False):
  calls=[];seals=0;revoked=False
  custody={'shares':['synthetic-share-one','synthetic-share-two','synthetic-share-three'],'operator_token':'synthetic-operator-token'}
  def api(path,body=None,token=None,raw=False):
   nonlocal seals,revoked
   calls.append(path)
   if path=='sys/seal-status':
    seals+=1;return {'initialized':False} if seals==1 else {'sealed':True,'t':3,'n':5}
   if path=='sys/audit':return {'data':{'unilogistix-file/':{'type':'file','options':{'file_path':'/openbao/data/unilogistix-audit.jsonl'}}}}
   if path=='sys/init':return {'keys_base64':['ephemeral-key-one','ephemeral-key-two','ephemeral-key-three'],'root_token':'ephemeral-root'}
   if path=='sys/health':return {'sealed':False,'version':'2.6.2','cluster_id':'wrong' if wrong_cluster else 'synthetic'}
   if path=='sys/unseal':return {}
   if path=='auth/token/revoke':
    self.assertEqual(token,'synthetic-operator-token');self.assertEqual(body,{'token':'scoped'});revoked=True;return {}
   if revoked and token=='scoped':raise worker.Denied()
   if path=='sys/storage/raft/snapshot-force':
    self.assertEqual(token,'ephemeral-root');self.assertTrue(raw);return {}
   if path.endswith('/role-id'):return {'data':{'role_id':'role'}}
   if path.endswith('/secret-id'):return {'data':{'secret_id':'secret'}}
   if path.endswith('/login'):return {'auth':{'client_token':'scoped'}}
   if path=='unilogistix/data/bootstrap/health' and body is None:return {'data':{'data':{'status':'ready'}}}
   if allow_denied:return {}
   raise worker.Denied()
  with patch.object(worker,'qualify_bindings',return_value=[]),patch.object(worker,'api',api),patch.object(worker.Path,'read_bytes',return_value=b'synthetic-archive'):
   if wrong_cluster or allow_denied:
    with self.assertRaises(ValueError):worker.qualify(custody,{'cluster_id':'synthetic'},[])
   else:self.assertEqual(worker.qualify(custody,{'cluster_id':'synthetic'},[])['status'],'PASS')
  self.assertTrue(all(not p.startswith(('http:', 'https:')) for p in calls))
  return calls
 def test_good_isolated_sequence_and_restored_policy_denials(self):self.exercise()
 def test_wrong_cluster_fails_before_canary(self):
  calls=self.exercise(wrong_cluster=True);self.assertNotIn('unilogistix/data/bootstrap/health',calls)
 def test_missing_scope_denial_fails_and_revokes_probe(self):
  self.assertEqual(self.exercise(allow_denied=True)[-1],'auth/token/revoke')
 def test_cleanup_refuses_unowned_container(self):
  with patch.object(host.subprocess,'run',return_value=subprocess.CompletedProcess([],0,b'other-run\n')),patch.object(host,'command') as command:
   with self.assertRaises(ValueError):host.cleanup('uni-restore-owned','expected')
   command.assert_not_called()
 def test_profile_rejects_secrets_duplicates_and_arbitrary_paths(self):
  import copy
  b={'role':'synthetic-reader','path':'unilogistix/data/example/dev/app','expected_version':2,'expected_fields':{'environment':'dev'},'denials':[{'path':'unilogistix/data/example/prod/app','method':None},{'path':'unilogistix/data/example/admin/app','method':None},{'path':'unilogistix/metadata/example','method':'LIST'}]}
  self.assertEqual(host.validate_profile([b]),[b])
  for change in [{'path':'http://attacker.invalid'},{'expected_fields':{'password':'secret'}},{'expected_version':True}]:
   value=copy.deepcopy(b);value.update(change)
   with self.assertRaises(ValueError):host.validate_profile([value])
  with self.assertRaises(ValueError):host.validate_profile([b,b])
 def test_diagnostics_drop_untrusted_payload(self):
  value={'stage':'original_custody_unseal','code':'http_failure','seal_metadata':{'sealed':False,'n':5,'t':3,'progress':'private-value','token':'private-value'},'unseal_step':3,'http_status':429}
  self.assertNotIn('private-value',str(host.safe_diagnostic(value)))
 def test_cli_preserves_only_validated_driver_diagnostics(self):
  secret='synthetic-private-body-token'
  diagnostic={'stage':'original_custody_unseal','code':'disposable_not_ready','seal_metadata':{'sealed':False,'n':5,'t':3,'progress':0,'token':secret},'unseal_step':3,'http_status':429,'body':secret,'log_categories':{'audit_error':True,'permission_denied':secret,'token':secret,'post_unseal_error':False}}
  for value,expected_stage in [(diagnostic,'original_custody_unseal'),(diagnostic|{'stage':secret},None),(diagnostic|{'code':secret},None)]:
   # Real subprocess exercises argparse, bounded stdin, main's handler and exit.
   # Only the restore operation is replaced; no credential files or Docker used.
   program="import sys,restore_qualification as h\n"+"def fail(*args):raise h.DriverFailure("+repr(value)+")\n"+"h.run=fail\nsys.exit(h.main())\n"
   result=subprocess.run([sys.executable,'-c',program,'--archive','/synthetic/archive','--receipt','/synthetic/receipt','--config','/synthetic/config'],cwd=Path(__file__).parent,input=json.dumps({'shares':['synthetic']*3,'operator_token':secret}).encode(),capture_output=True,timeout=10)
   self.assertEqual(result.returncode,1);self.assertNotIn(secret.encode(),result.stdout+result.stderr)
   output=json.loads(result.stdout)
   self.assertEqual(output.get('stage'),expected_stage)
   if expected_stage:
    self.assertEqual(output['log_categories'],{'audit_error':True,'post_unseal_error':False})
    self.assertEqual(output['seal_metadata'],{'sealed':False,'n':5,'t':3,'progress':0})
    self.assertEqual(output['http_status'],429)
   else:self.assertEqual(output,{'status':'FAIL','code':'isolated_restore_failed_or_cleanup_required'})
 def test_no_redirects_and_bad_custody(self):
  with self.assertRaises(ValueError):worker.NoRedirect().redirect_request()
  with patch.object(worker,'api') as api:
   with self.assertRaises(ValueError):worker.qualify({'shares':[],'operator_token':'no'}, {},[])
   api.assert_not_called()

if __name__=='__main__':unittest.main()
