"""Single-source capture/delivery. Never follows HTTP redirects or asserts restore validity."""
import urllib.error
import json,os,signal,stat,subprocess,sys,tempfile,urllib.request,urllib.parse,uuid
from pathlib import Path
from backup_common import *

class NoRedirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,*args,**kwargs):raise Refuse('HTTP redirect refused')

def check_ssh_identity(path):
 s=Path(path).stat()
 if not stat.S_ISREG(s.st_mode) or s.st_uid!=0 or s.st_mode&0o077:
  raise Refuse('unsafe SSH identity permissions')

def sender_config(c):
 u=urllib.parse.urlsplit(c['base_url'])
 if u.scheme!='https' or not u.hostname or u.username or u.password or u.query or u.fragment or u.path not in ('','/'):raise Refuse('exact HTTPS origin required')
 for k in ('token_file','ssh_identity','ssh_known_hosts'):no_symlinks(c[k])
 if not re.fullmatch(r'[a-z_][a-z0-9_-]*@[A-Za-z0-9.-]+',c['ssh_target']):raise Refuse('fixed SSH target required')
 return c

def identity(opener,c):
 with opener.open(c['base_url'].rstrip('/')+'/v1/sys/health',timeout=30) as r:
  body=r.read(65537)
  if len(body)>65536:raise Refuse('health response too large')
  h=json.loads(body)
 if h.get('cluster_id')!=c['cluster_id'] or h.get('version') not in c['allowed_versions'] or h.get('sealed') is not False or h.get('initialized') is not True:raise Refuse('source health/identity mismatch')
 return h['version']

def read_token(c):
 tokenpath=Path(c['token_file']);s=tokenpath.stat()
 if not stat.S_ISREG(s.st_mode) or s.st_uid!=0 or s.st_mode&0o077:raise Refuse('unsafe token file')
 token=tokenpath.read_text().strip()
 if not token or '\n' in token or '\r' in token:raise Refuse('invalid token')
 return token

# Only fixed codes leave this process: never exception text, URLs or response bodies.
def failure_code(exc):
 if isinstance(exc,urllib.error.HTTPError):
  try:exc.close()
  except Exception:pass
  return 'http_'+str(exc.code) if exc.code in (400,401,403,404,429,500,502,503,504) else 'http_error'
 if isinstance(exc,(TimeoutError,subprocess.TimeoutExpired)):return 'timeout'
 if isinstance(exc,urllib.error.URLError):return 'transport_error'
 if isinstance(exc,Refuse):
  return 'ssh_identity_permissions' if str(exc)=='unsafe SSH identity permissions' else 'validation_refused'
 if isinstance(exc,(ValueError,TypeError,KeyError)):return 'invalid_data'
 if isinstance(exc,OSError):return 'io_error'
 return 'internal_error'

def capture(c,opener=None,run=subprocess.run):
 sender_config(c);root=source_root(c,'capture_root');directory=candidates(c,'capture_root')
 with lock(root):
  tmp=None;stage='ssh_identity_permissions'
  try:
   check_ssh_identity(c['ssh_identity'])
   stage='token_file'
   token=read_token(c)
   opener=opener or urllib.request.build_opener(NoRedirect())
   stage='source_health'
   version=identity(opener,c)
   base=c['base_url'].rstrip('/')
   stage='token_renewal'
   req=urllib.request.Request(base+'/v1/auth/token/renew-self',data=b'{}',headers={'X-Vault-Token':token,'Content-Type':'application/json'},method='POST')
   with opener.open(req,timeout=30) as response:response.read(65536)
   stage='snapshot_download'
   fd,name=tempfile.mkstemp(prefix='.incoming-',dir=directory);tmp=Path(name)
   req=urllib.request.Request(base+'/v1/sys/storage/raft/snapshot',headers={'X-Vault-Token':token})
   with os.fdopen(fd,'wb') as out,opener.open(req,timeout=60) as response:
    size=0
    while b:=response.read(65536):
     size+=len(b)
     if size>MAX_ARCHIVE:raise Refuse('snapshot too large')
     out.write(b)
    out.flush();os.fsync(out.fileno())
   stage='snapshot_validation'
   digest,size=validate_snapshot(tmp)
   stage='source_recheck'
   if identity(opener,c)!=version:raise Refuse('source version changed during capture')
   m=manifest({'protocol':1,'source_id':SOURCE,'cluster_id':c['cluster_id'],'source_version':version,'capture_id':uuid.uuid4().hex,'captured_at':utcnow(),'bytes':size,'sha256':digest},c)
   # Packet is bounded to64MiB; only synthetic tests replace the subprocess runner.
   packet=json.dumps(m,sort_keys=True).encode()+b'\n'+tmp.read_bytes()
   command=['ssh','-T','-o','BatchMode=yes','-o','StrictHostKeyChecking=yes','-o','IdentitiesOnly=yes','-o','ConnectTimeout=15','-o','ServerAliveInterval=15','-o','ServerAliveCountMax=2','-o','UserKnownHostsFile='+c['ssh_known_hosts'],'-i',c['ssh_identity'],c['ssh_target']]
   stage='delivery_transport'
   result=run(command,input=packet,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,timeout=150,check=False)
   if result.returncode or len(result.stdout)>16384:raise Refuse('delivery failed')
   stage='delivery_receipt'
   receipt=json.loads(result.stdout)
   if set(receipt)!={'status','manifest','received_at'} or receipt['status']!='stored_unverified' or receipt['manifest']!=m:raise Refuse('unmatched durable receipt')
   if timestamp(receipt['received_at'])>datetime.datetime.now(datetime.timezone.utc):raise Refuse('future receipt timestamp')
   stage='local_persistence'
   dest=directory/(m['capture_id']+'.snap');os.link(tmp,dest);fsync_dir(directory)
   atomic_json(directory/(m['capture_id']+'.receipt.json'),receipt);prune(directory)
   atomic_json(root/'status.json',{'last_attempt':'PASS','at':utcnow(),'receipt':receipt})
   return receipt
  except Exception as exc:
   atomic_json(root/'status.json',{'last_attempt':'FAIL','at':utcnow(),'category':'capture_or_delivery_failed','stage':stage,'error_code':failure_code(exc)})
   raise
  finally:
   if tmp is not None:tmp.unlink(missing_ok=True)

def main():
 signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(Refuse('operation deadline')));signal.alarm(600)
 try:capture(config('/etc/unilogistix/backup-source.json'));print('snapshot_delivery=PASS status=stored_unverified');return 0
 except Exception as exc:print('snapshot_delivery=FAIL error_code='+failure_code(exc),file=sys.stderr);return 1
 finally:signal.alarm(0)
if __name__=='__main__':sys.exit(main())
