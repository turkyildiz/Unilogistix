import contextlib,importlib.util,io,json,os,pathlib,tempfile,types,unittest
from unittest.mock import patch
os.environ.setdefault('BAO_ADDR','https://vault.invalid')
os.environ.setdefault('BAO_CLUSTER_ID','expected-cluster')
os.environ.setdefault('BAO_SSH_HOST','test-host')
os.environ.setdefault('BAO_CUSTODIANS',json.dumps([['one','/share'],['two','/share'],['three','/share']]))
spec=importlib.util.spec_from_file_location('watch',pathlib.Path(__file__).with_name('unseal-watch.py'))
watch=importlib.util.module_from_spec(spec);spec.loader.exec_module(watch)
class RecoverySafety(unittest.TestCase):
 def scenario(self,started,previous):
  calls=[];ssh=[]
  def api(path,data=None):
   calls.append((path,data))
   if path=='sys/health':return {'initialized':True,'sealed':len([p for p,d in calls if p=='sys/unseal'])<3,'cluster_id':watch.expected}
   if path=='sys/seal-status':return {'t':3,'n':5,'progress':0}
   return {}
  def command(args,**kwargs):
   if args[0]=='tailscale':return types.SimpleNamespace(returncode=0,stdout=started)
   ssh.append(args);return types.SimpleNamespace(returncode=0,stdout=str(len(ssh))*44)
  with tempfile.TemporaryDirectory() as temp:
   home=pathlib.Path(temp)
   if previous:
    p=home/'.local/state/unilogistix/vault-process.json';p.parent.mkdir(parents=True);p.write_text(json.dumps(previous))
   with patch.object(pathlib.Path,'home',return_value=home),patch.object(watch,'api',side_effect=api),patch.object(watch.subprocess,'run',side_effect=command),contextlib.redirect_stdout(io.StringIO()):watch.run()
  return calls,ssh
 def test_operator_pause_never_reads_shares(self):
  calls,ssh=self.scenario('PAUSED',{'started':'old','cluster':watch.expected});self.assertFalse(ssh)
 def test_manual_seal_never_reads_shares(self):
  calls,ssh=self.scenario('same',{'started':'same','cluster':watch.expected});self.assertFalse(ssh)
 def test_no_history_never_reads_shares(self):
  calls,ssh=self.scenario('new',None);self.assertFalse(ssh)
 def test_observed_restart_unseals_with_three_shares(self):
  calls,ssh=self.scenario('new',{'started':'old','cluster':watch.expected});self.assertEqual(len(ssh),3);self.assertEqual(sum(p=='sys/unseal' for p,d in calls),3)
if __name__=='__main__':unittest.main()
