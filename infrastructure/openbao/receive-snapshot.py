#!/usr/bin/env python3
"""Forced SSH command: accept only bounded snapshot archives, never shell commands."""
import datetime,os,pathlib,sys,tarfile,tempfile
root=pathlib.Path.home()/'.local/share/unilogistix-backups'
root.mkdir(mode=0o700,parents=True,exist_ok=True)
fd,name=tempfile.mkstemp(dir=root,prefix='.incoming-')
p=pathlib.Path(name)
try:
 size=0
 with os.fdopen(fd,'wb') as f:
  while b:=sys.stdin.buffer.read(65536):
   size+=len(b)
   if size>64*1024*1024:raise ValueError('Snapshot exceeds configured limit')
   f.write(b)
 with tarfile.open(p) as t:
  names=t.getnames()
  assert 'meta.json' in names and 'state.bin' in names
 dest=root/('openbao-'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'.snap')
 p.rename(dest)
 for old in sorted(root.glob('openbao-*.snap'))[:-28]:old.unlink()
 print('snapshot_received=PASS')
finally:p.unlink(missing_ok=True)
