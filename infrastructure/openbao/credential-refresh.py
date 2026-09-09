#!/usr/bin/env python3
"""Root-owned local broker: only issues the bootstrap canary reader."""
import json, os, pathlib, urllib.request
BASE=os.environ['BAO_ADDR'].rstrip('/')+'/v1/'
root=pathlib.Path('/var/lib/unilogistix/identity')
run=pathlib.Path('/run/unilogistix')
def api(path,data=None,token=None):
 h={'Content-Type':'application/json'}
 if token:h['X-Vault-Token']=token
 req=urllib.request.Request(BASE+path,headers=h,data=None if data is None else json.dumps(data).encode())
 with urllib.request.urlopen(req,timeout=10) as r:return json.load(r)
def save(p,value):
 tmp=p.with_suffix('.tmp')
 fd=os.open(tmp,os.O_WRONLY|os.O_CREAT|os.O_TRUNC,0o600)
 with os.fdopen(fd,'w') as f:f.write(value)
 os.replace(tmp,p)
run.mkdir(mode=0o700,exist_ok=True)
out=run/'bootstrap.token'
try:
 issuer=(root/'issuer.token').read_text().strip()
 api('auth/token/renew-self',{},issuer)
 role='auth/unilogistix-approle/role/bootstrap-reader/'
 rid=api(role+'role-id',token=issuer)['data']['role_id']
 sid=api(role+'secret-id',{},issuer)['data']['secret_id']
 auth=api('auth/unilogistix-approle/login',{'role_id':rid,'secret_id':sid})['auth']
 token=auth['client_token']
 assert api('unilogistix/data/bootstrap/health',token=token)['data']['data']['status']=='ready'
 save(out,token)
 print('credential_delivery=PASS canary=PASS')
except Exception:
 out.unlink(missing_ok=True)
 print('credential_delivery=FAILED credential_file_removed=true')
 raise SystemExit(1)
