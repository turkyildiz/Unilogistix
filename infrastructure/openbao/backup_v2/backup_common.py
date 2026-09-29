"""Single-source backup protocol. Hash/structure validation is not a restore proof."""
import contextlib,datetime,fcntl,gzip,hashlib,json,os,re,stat,tarfile,tempfile
from pathlib import Path
SOURCE='shared-fleet'
MAX_ARCHIVE=64*1024*1024
MAX_EXPANDED=512*1024*1024
MEMBERS={'meta.json','state.bin','SHA256SUMS','SHA256SUMS.sealed'}
class Refuse(ValueError):pass

def utcnow():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def timestamp(value):
 try:d=datetime.datetime.fromisoformat(value)
 except (ValueError,TypeError):raise Refuse('invalid timestamp')
 if d.tzinfo is None or d.utcoffset()!=datetime.timedelta(0):raise Refuse('timestamp must be UTC')
 return d

def no_symlinks(path):
 path=Path(path)
 if not path.is_absolute():raise Refuse('absolute path required')
 for p in [path,*path.parents]:
  if p.is_symlink():raise Refuse('symlinked path refused')
 return path

def private_directory(path):
 path=no_symlinks(path);path.mkdir(parents=True,mode=0o700,exist_ok=True)
 mode=path.stat().st_mode
 if not stat.S_ISDIR(mode) or mode&0o077:raise Refuse('private directory permissions required')
 return path

def trusted_json(path,trusted_uid=0):
 path=no_symlinks(path);s=path.stat()
 if not stat.S_ISREG(s.st_mode) or s.st_uid!=trusted_uid or s.st_mode&0o022 or s.st_size>32768:raise Refuse('untrusted control file')
 return json.loads(path.read_text())

def config(path,trusted_uid=0):
 c=trusted_json(path,trusted_uid)
 if c.get('source_id')!=SOURCE or not isinstance(c.get('cluster_id'),str) or not c['cluster_id'] or len(c['cluster_id'])>128:raise Refuse('invalid fixed source')
 versions=c.get('allowed_versions')
 if not isinstance(versions,list) or not versions or any(not isinstance(v,str) or not re.fullmatch(r'\d+\.\d+\.\d+(?:[-+][\w.-]+)?',v) for v in versions):raise Refuse('explicit versions required')
 for key in ('storage_root','capture_root'):no_symlinks(c[key])
 if c.get('retain_candidates',28)!=28:raise Refuse('unsupported retention policy')
 return c

def manifest(data,c):
 fields={'protocol','source_id','cluster_id','source_version','capture_id','captured_at','bytes','sha256'}
 if not isinstance(data,dict) or set(data)!=fields or type(data['protocol']) is not int or data['protocol']!=1:raise Refuse('invalid manifest shape')
 if data['source_id']!=SOURCE or data['cluster_id']!=c['cluster_id'] or data['source_version'] not in c['allowed_versions']:raise Refuse('wrong source identity/version')
 if not isinstance(data['capture_id'],str) or not re.fullmatch('[0-9a-f]{32}',data['capture_id']):raise Refuse('invalid capture identity')
 if type(data['bytes']) is not int or not 0<data['bytes']<=MAX_ARCHIVE:raise Refuse('invalid archive size')
 if not isinstance(data['sha256'],str) or not re.fullmatch('[0-9a-f]{64}',data['sha256']):raise Refuse('invalid digest')
 if timestamp(data['captured_at'])>datetime.datetime.now(datetime.timezone.utc)+datetime.timedelta(seconds=60):raise Refuse('future capture timestamp')
 return data

def file_digest(path):
 h=hashlib.sha256();size=0
 with Path(path).open('rb') as f:
  while b:=f.read(65536):h.update(b);size+=len(b)
 return h.hexdigest(),size

def validate_snapshot(path):
 path=Path(path);digest,size=file_digest(path)
 if not 0<size<=MAX_ARCHIVE:raise Refuse('archive size invalid')
 # Fully consume gzip to verify CRC/trailer and cap expansion before parsing tar.
 with path.open('rb') as f:compressed=f.read(2)==b'\x1f\x8b'
 expanded=0
 with (gzip.open(path,'rb') if compressed else path.open('rb')) as f:
  while b:=f.read(65536):
   expanded+=len(b)
   if expanded>MAX_EXPANDED:raise Refuse('expanded archive too large')
 hashes={};small={};seen=set()
 with tarfile.open(path,mode='r|*') as tar:
  for item in tar:
   if item.name not in MEMBERS or item.name in seen or not item.isfile() or item.size<=0:raise Refuse('invalid archive member')
   if item.size>(MAX_EXPANDED if item.name=='state.bin' else 65536):raise Refuse('archive member too large')
   seen.add(item.name);stream=tar.extractfile(item);h=hashlib.sha256();count=0;parts=[]
   while b:=stream.read(65536):
    count+=len(b);h.update(b)
    if item.name!='state.bin':parts.append(b)
   if count!=item.size:raise Refuse('truncated archive member')
   hashes[item.name]=h.hexdigest()
   if item.name!='state.bin':small[item.name]=b''.join(parts)
 if seen!=MEMBERS:raise Refuse('incomplete Raft archive')
 try:meta=json.loads(small['meta.json']);lines=small['SHA256SUMS'].decode('ascii').splitlines()
 except (ValueError,UnicodeError):raise Refuse('invalid archive metadata/checksums')
 if not isinstance(meta,dict) or not meta:raise Refuse('empty Raft metadata')
 expected={}
 for line in lines:
  match=re.fullmatch(r'([0-9a-f]{64}) [ *](meta\.json|state\.bin)',line)
  if not match or match[2] in expected:raise Refuse('invalid checksum list')
  expected[match[2]]=match[1]
 if set(expected)!={'meta.json','state.bin'} or any(hashes[k]!=v for k,v in expected.items()):raise Refuse('internal archive checksum mismatch')
 # SHA256SUMS.sealed remains opaque: only an isolated restore/unseal validates it.
 return digest,size

def fsync_dir(path):
 fd=os.open(path,os.O_RDONLY|os.O_DIRECTORY)
 try:os.fsync(fd)
 finally:os.close(fd)

def atomic_json(path,value):
 path=Path(path);no_symlinks(path)
 fd,name=tempfile.mkstemp(prefix='.json-',dir=path.parent)
 try:
  with os.fdopen(fd,'w') as f:json.dump(value,f,sort_keys=True);f.write('\n');f.flush();os.fsync(f.fileno())
  os.replace(name,path);fsync_dir(path.parent)
 finally:Path(name).unlink(missing_ok=True)

@contextlib.contextmanager
def lock(directory):
 path=Path(directory)/'.lock';fd=os.open(path,os.O_CREAT|os.O_RDWR|os.O_NOFOLLOW,0o600)
 try:
  if not stat.S_ISREG(os.fstat(fd).st_mode):raise Refuse('invalid lock')
  fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB);yield
 except BlockingIOError:raise Refuse('backup source busy')
 finally:os.close(fd)

def source_root(c,kind):return private_directory(private_directory(Path(c[kind]))/SOURCE)
def candidates(c,kind):return private_directory(source_root(c,kind)/'candidates')

def prune(directory):
 # Call only under source lock. Checkpoints and legacy backups are never scanned.
 directory=Path(directory);complete=[]
 for p in directory.glob('*.receipt.json'):
  try:
   if p.is_symlink():raise Refuse('symlink receipt')
   r=json.loads(p.read_text());capture=r['manifest']['capture_id'];f=directory/(capture+'.snap')
   if p.name!=capture+'.receipt.json' or f.is_symlink() or not f.is_file():continue
   complete.append((timestamp(r['received_at']),capture))
  except (KeyError,ValueError,OSError):continue
 for _,capture in sorted(complete)[:-28]:
  (directory/(capture+'.snap')).unlink();(directory/(capture+'.receipt.json')).unlink()
 fsync_dir(directory)
