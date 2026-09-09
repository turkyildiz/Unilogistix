#!/usr/bin/env python3
"""Fixed read-only provider checks. No arbitrary URLs, paths, or request bodies."""
import argparse,json,os,pathlib,urllib.request,urllib.error
PROVIDERS={
 'cloudflare':('platform/deploy/CF_API_TOKEN','https://api.cloudflare.com/client/v4/user/tokens/verify'),
 'vercel':('platform/deploy/VERCEL_TOKEN_INFRA','https://api.vercel.com/v2/user'),
 'supabase':('platform/deploy/SUPABASE_ACCESS_TOKEN','https://api.supabase.com/v1/organizations'),
 'fireworks':('platform/birth/FIREWORKS_API_KEY','https://api.fireworks.ai/v1/accounts'),
}
class NoRedirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,*args,**kwargs):return None
opener=urllib.request.build_opener(NoRedirect)
def req(url,token,data=None,vault=False):
 headers={'X-Vault-Token' if vault else 'Authorization':token if vault else 'Bearer '+token,'Content-Type':'application/json','User-Agent':'Unilogistix-access-verification'}
 q=urllib.request.Request(url,headers=headers,data=None if data is None else json.dumps(data).encode())
 with opener.open(q,timeout=10) as r:
  b=r.read(2*1024*1024)
  return json.loads(b) if b else {}
def main():
 parser=argparse.ArgumentParser();parser.add_argument('provider',choices=PROVIDERS);args=parser.parse_args()
 if pathlib.Path('/var/lib/unilogistix/PAUSED').exists():raise PermissionError('Operator pause')
 base=os.environ['BAO_ADDR'].rstrip('/')+'/v1/'
 issuer=pathlib.Path('/var/lib/unilogistix/identity/provider-issuer.token').read_text().strip()
 req(base+'auth/token/renew-self',issuer,{},True)
 role='auth/unilogistix-approle/role/provider-'+args.provider+'/'
 rid=req(base+role+'role-id',issuer,vault=True)['data']['role_id']
 sid=req(base+role+'secret-id',issuer,{},True)['data']['secret_id']
 token=req(base+'auth/unilogistix-approle/login','',{'role_id':rid,'secret_id':sid},True)['auth']['client_token']
 try:
  path,url=PROVIDERS[args.provider]
  secret=req(base+'secret/data/'+path,token,vault=True)['data']['data']['value']
  result=req(url,secret)
  if args.provider=='cloudflare':ok=result.get('success') is True and result.get('result',{}).get('status')=='active'
  elif args.provider=='vercel':ok=bool(result.get('user',{}).get('id'))
  elif args.provider=='supabase':ok=isinstance(result,list)
  else:ok=isinstance(result.get('accounts'),list)
  print(json.dumps({'provider':args.provider,'read_check':'PASS' if ok else 'FAILED'}))
  return 0 if ok else 1
 finally:req(base+'auth/token/revoke-self',token,{},True)
if __name__=='__main__':
 try:raise SystemExit(main())
 except Exception as e:
  print(json.dumps({'read_check':'FAILED','error_type':type(e).__name__,'http_status':getattr(e,'code',None)}))
  raise SystemExit(1)
