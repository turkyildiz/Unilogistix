import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
import urllib.error
from unittest.mock import patch
import snapshot_backup as s

SECRET='synthetic-token-secret-response-body'

class DiagnosticsTests(unittest.TestCase):
 def test_error_codes_do_not_copy_messages(self):
  cases=[(urllib.error.HTTPError('https://'+SECRET,403,SECRET,{},io.BytesIO(SECRET.encode())),'http_403'),
   (urllib.error.HTTPError(SECRET,418,SECRET,{},None),'http_error'),
   (urllib.error.URLError(SECRET),'transport_error'),(TimeoutError(SECRET),'timeout'),
   (s.Refuse(SECRET),'validation_refused'),(ValueError(SECRET),'invalid_data'),
   (OSError(SECRET),'io_error'),(RuntimeError(SECRET),'internal_error')]
  for error,expected in cases:self.assertEqual(s.failure_code(error),expected)

 def exercise(self, failing):
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory)
   protected=root/'last-known-restorable.snap';protected.write_bytes(b'preserved')
   c={'base_url':'https://synthetic.invalid','token_file':str(root/'token'),
      'ssh_identity':str(root/'identity'),'ssh_known_hosts':str(root/'known_hosts'),
      'ssh_target':'test@synthetic.invalid','capture_root':str(root/'captures'),
      'cluster_id':'synthetic','allowed_versions':['2.6.2'],'source_id':'shared-fleet'}
   identities=0
   def identity(*_):
    nonlocal identities
    identities+=1
    if failing==('source_health' if identities==1 else 'source_recheck'):raise ValueError(SECRET)
    return '2.6.2'
   def token(_):
    if failing=='token_file':raise OSError(SECRET)
    return SECRET
   class Opener:
    def open(self, req, **_):
     stage='token_renewal' if req.full_url.endswith('renew-self') else 'snapshot_download'
     if failing==stage:raise urllib.error.HTTPError(SECRET,403,SECRET,{},io.BytesIO(SECRET.encode()))
     return io.BytesIO(b'{}' if stage=='token_renewal' else b'synthetic-snapshot')
   def validate(_):
    if failing=='snapshot_validation':raise s.Refuse(SECRET)
    return 'a'*64,18
   def runner(command, **kw):
    self.assertIn('StrictHostKeyChecking=yes',command)
    self.assertEqual(kw['stderr'],subprocess.DEVNULL)
    if failing=='delivery_transport':return subprocess.CompletedProcess(command,1,b'',SECRET.encode())
    if failing=='delivery_receipt':return subprocess.CompletedProcess(command,0,SECRET.encode())
    m=json.loads(kw['input'].split(b'\n',1)[0])
    return subprocess.CompletedProcess(command,0,json.dumps({'status':'stored_unverified','manifest':m,'received_at':s.utcnow()}).encode())
   original_link=s.os.link
   def link(*args):
    if failing=='local_persistence':raise OSError(SECRET)
    return original_link(*args)
   with patch.object(s,'check_ssh_identity',lambda _:None),patch.object(s,'read_token',token),patch.object(s,'identity',identity),patch.object(s,'validate_snapshot',validate),patch.object(s.os,'link',link):
    if failing:
     with self.assertRaises(Exception):s.capture(c,opener=Opener(),run=runner)
    else:s.capture(c,opener=Opener(),run=runner)
   status=json.loads((root/'captures/shared-fleet/status.json').read_text())
   self.assertNotIn(SECRET,json.dumps(status))
   self.assertEqual(status['last_attempt'],'FAIL' if failing else 'PASS')
   if failing:self.assertEqual(status['stage'],failing)
   self.assertEqual(protected.read_bytes(),b'preserved')
   self.assertEqual(list((root/'captures/shared-fleet/candidates').glob('.incoming-*')),[])

 def test_all_failure_stages(self):
  for stage in ('token_file','source_health','token_renewal','snapshot_download','snapshot_validation','source_recheck','delivery_transport','delivery_receipt','local_persistence'):
   with self.subTest(stage=stage):self.exercise(stage)

 def test_ssh_permission_regression(self):
  from types import SimpleNamespace
  for mode,uid,accepted in ((0o100600,0,True),(0o100640,0,False),(0o100600,1000,False),(0o040600,0,False)):
   with patch.object(s.Path,'stat',return_value=SimpleNamespace(st_mode=mode,st_uid=uid)):
    if accepted:s.check_ssh_identity('/synthetic')
    else:
     with self.assertRaises(s.Refuse) as caught:s.check_ssh_identity('/synthetic')
     self.assertEqual(s.failure_code(caught.exception),'ssh_identity_permissions')

 def test_invalid_key_replaces_prior_pass_and_preserves_archives(self):
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory);key=root/'key';key.write_text('synthetic-unused');key.chmod(0o640)
   c={'base_url':'https://synthetic.invalid','token_file':str(root/'never-read'),
      'ssh_identity':str(key),'ssh_known_hosts':str(root/'known_hosts'),'ssh_target':'test@synthetic.invalid',
      'capture_root':str(root/'captures')}
   source=s.source_root(c,'capture_root');archive=s.candidates(c,'capture_root')/'previous.snap'
   archive.write_bytes(b'preserved');s.atomic_json(source/'status.json',{'last_attempt':'PASS'})
   with patch.object(s,'read_token',side_effect=AssertionError('must not read credentials')):
    with self.assertRaises(s.Refuse):s.capture(c)
   result=json.loads((source/'status.json').read_text())
   self.assertEqual(result['last_attempt'],'FAIL');self.assertEqual(result['stage'],'ssh_identity_permissions')
   self.assertEqual(result['error_code'],'ssh_identity_permissions');self.assertEqual(archive.read_bytes(),b'preserved')

 def test_success_still_records_exact_receipt(self):self.exercise(None)

if __name__=='__main__':unittest.main()
