#!/usr/bin/env python3
"""Snapshot-only identity; strict SSH delivery to a forced receiver."""
import datetime,json,os,pathlib,subprocess,tarfile,urllib.request
root=pathlib.Path('/var/lib/unilogistix')
identity=root/'backup-identity'
k=(identity/'bao.token').read_text().strip()
base=os.environ['BAO_ADDR'].rstrip('/')+'/v1/'
def request(path,data=None):
 q=urllib.request.Request(base+path,headers={'X-Vault-Token':k},data=None if data is None else json.dumps(data).encode())
 return urllib.request.urlopen(q,timeout=30)
with request('auth/token/renew-self',{}) as r:r.read()
out=root/'backups';out.mkdir(mode=0o700,exist_ok=True)
p=out/('scheduled-'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'.snap')
fd=os.open(p,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
with request('sys/storage/raft/snapshot') as r,os.fdopen(fd,'wb') as f:
 size=0
 while b:=r.read(65536):
  size+=len(b)
  if size>64*1024*1024:raise ValueError('Snapshot exceeds configured limit')
  f.write(b)
with tarfile.open(p) as t:assert {'meta.json','state.bin'}.issubset(t.getnames())
with p.open('rb') as f:
 r=subprocess.run(['ssh','-o','BatchMode=yes','-o','StrictHostKeyChecking=yes','-o','IdentitiesOnly=yes','-o','ConnectTimeout=10','-o','UserKnownHostsFile='+str(identity/'known_hosts'),'-i',str(identity/'id_ed25519'),os.environ['BACKUP_SSH_TARGET']],stdin=f,capture_output=True,timeout=45)
assert r.returncode==0 and b'snapshot_received=PASS' in r.stdout,'Backup delivery failed'
for old in sorted(out.glob('scheduled-*.snap'))[:-28]:old.unlink()
status={'last_success':datetime.datetime.now(datetime.timezone.utc).isoformat(),'bytes':size,'delivery':'PASS'}
(out/'status.json').write_text(json.dumps(status))
print('snapshot_capture=PASS secondary_delivery=PASS')
