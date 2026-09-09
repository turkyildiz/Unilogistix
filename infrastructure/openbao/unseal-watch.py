#!/usr/bin/env python3
"""Fixed-target unseal watcher; shares stay in process memory, never logs/files."""
import json,os,pathlib,subprocess,urllib.request,urllib.error
base=os.environ['BAO_ADDR'].rstrip('/')+'/v1/'
expected=os.environ['BAO_CLUSTER_ID']
def api(path,data=None):
 q=urllib.request.Request(base+path,data=None if data is None else json.dumps(data).encode(),headers={'Content-Type':'application/json'})
 try:
  with urllib.request.urlopen(q,timeout=8) as r:return json.load(r)
 except urllib.error.HTTPError as e:
  if path=='sys/health' and e.code==503:return json.loads(e.read())
  raise
def run():
 h=api('sys/health');assert h.get('initialized'),'Uninitialized vault; automatic initialization forbidden'
 r=subprocess.run(['tailscale','ssh',os.environ['BAO_SSH_HOST'],"if sudo -n test -f /var/lib/unilogistix/PAUSED; then echo PAUSED; else sudo -n docker inspect --format '{{.State.StartedAt}}' truxon-openbao; fi"],capture_output=True,text=True,timeout=10)
 assert r.returncode==0,'Cannot verify operator pause and process state'
 started=r.stdout.strip();assert started
 if started=='PAUSED':
  print('operator_pause_preserved=true');return
 state=pathlib.Path.home()/'.local/state/unilogistix/vault-process.json'
 state.parent.mkdir(mode=0o700,parents=True,exist_ok=True)
 if not h.get('sealed'):
  assert h.get('cluster_id')==expected,'Unexpected cluster'
  fd=os.open(state,os.O_WRONLY|os.O_CREAT|os.O_TRUNC,0o600)
  with os.fdopen(fd,'w') as f:json.dump({'started':started,'cluster':expected},f)
  print('vault_unsealed=true recovery_needed=false');return
 previous=json.loads(state.read_text()) if state.exists() else {}
 if previous.get('cluster')!=expected or previous.get('started')==started or not previous.get('started'):
  print('sealed_state_preserved=true restart_evidence=false');return
 s=api('sys/seal-status');assert s['t']==3 and s['n']==5 and s['progress']==0,'Unexpected seal or concurrent recovery'
 custodians=json.loads(os.environ['BAO_CUSTODIANS'])
 assert len(custodians)==3
 shares=[]
 for host,path in custodians:
  r=subprocess.run(['ssh','-o','BatchMode=yes','-o','StrictHostKeyChecking=yes','-o','ConnectTimeout=5',host,'cat '+path],capture_output=True,text=True,timeout=10)
  assert r.returncode==0,'Custodian unavailable'
  key=r.stdout.strip();assert len(key)==44;shares.append(key)
 assert len(set(shares))==3
 try:
  for key in shares:api('sys/unseal',{'key':key})
  h=api('sys/health');assert not h['sealed'] and h['cluster_id']==expected
 except Exception:
  api('sys/unseal',{'reset':True});raise
 print('vault_unsealed=true recovery_completed=true')
if __name__=='__main__':
 try:run()
 except Exception as e:
  print(json.dumps({'recovery':'FAILED','error_type':type(e).__name__}));raise SystemExit(1)
