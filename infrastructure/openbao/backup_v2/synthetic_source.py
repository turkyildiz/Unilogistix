"""Synthetic-only fixture inside an isolated throwaway source vault."""
import base64
import json
import urllib.request
import restore_worker as w

init=w.api('sys/init',{'secret_shares':5,'secret_threshold':3})
shares=init['keys_base64'][:3];operator=init['root_token']
for share in shares:w.api('sys/unseal',{'key':share})
health=w.ready()
w.api('sys/mounts/unilogistix',{'type':'kv','options':{'version':'2'}},operator)
w.api('sys/auth/unilogistix-approle',{'type':'approle'},operator)
roles={'bootstrap-reader':('unilogistix-bootstrap-read','unilogistix/data/bootstrap/health')}
for service in ('db-api','db-worker'):
 role='vakf-staging-us-'+service;roles[role]=(role,'unilogistix/data/vakf/staging/us/'+service)
for role,(policy,path) in roles.items():
 text='path "'+path+'" { capabilities = ["read"] }\npath "auth/token/revoke-self" { capabilities = ["update"] }'
 if role=='bootstrap-reader':text='path "unilogistix/data/bootstrap/health" { capabilities = ["read"] }\npath "secret/*" { capabilities = ["deny"] }'
 w.api('sys/policies/acl/'+policy,{'policy':text},operator)
 w.api('auth/unilogistix-approle/role/'+role,{'token_policies':[policy],'token_no_default_policy':True,'secret_id_num_uses':1,'token_ttl':120},operator)
w.api('unilogistix/data/bootstrap/health',{'data':{'status':'ready'}},operator)
for service,kind in (('db-api','api'),('db-worker','worker')):
 path='unilogistix/data/vakf/staging/us/'+service
 bundle={'project_ref':'synthetic-project','role':'vakf_staging_'+kind+'_runtime','environment':'staging','cell':'us','status':'pending','password':'synthetic-only'}
 w.api(path,{'data':bundle},operator);bundle['status']='active';w.api(path,{'data':bundle},operator)
request=urllib.request.Request(w.BASE+'sys/storage/raft/snapshot',headers={'X-Vault-Token':operator})
with urllib.request.urlopen(request,timeout=30) as response:archive=response.read(64*1024*1024+1)
if len(archive)>64*1024*1024:raise ValueError('bound')
# This stdout is captured by the parent in memory; never relayed to logs/console.
print(json.dumps({'custody':{'shares':shares,'operator_token':operator},'archive':base64.b64encode(archive).decode(),'cluster_id':health['cluster_id']}))
