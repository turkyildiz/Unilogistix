#!/usr/bin/env python3
"""Metadata-only vault readiness monitor. Nonzero exit means intervention needed."""
import datetime,json,os,pathlib,shutil,time,urllib.request
checks={}
try:
 with urllib.request.urlopen(os.environ['BAO_ADDR'].rstrip('/')+'/v1/sys/health',timeout=5) as r:d=json.load(r)
 checks['vault_unsealed']=d.get('initialized') and not d.get('sealed')
except Exception:checks['vault_unsealed']=False
p=pathlib.Path('/run/unilogistix/bootstrap.token')
checks['credential_fresh']=p.exists() and time.time()-p.stat().st_mtime<240
p=pathlib.Path('/var/lib/unilogistix/backups/status.json')
try:
 d=json.loads(p.read_text());age=(datetime.datetime.now(datetime.timezone.utc)-datetime.datetime.fromisoformat(d['last_success'])).total_seconds()
 checks['secondary_backup_fresh']=age<8*3600 and d['delivery']=='PASS'
except Exception:checks['secondary_backup_fresh']=False
p=pathlib.Path(os.environ['AUDIT_LOG_PATH'])
checks['audit_fresh']=p.exists() and time.time()-p.stat().st_mtime<300
usage=shutil.disk_usage('/var/lib/unilogistix');checks['disk_capacity']=usage.free/usage.total>.2
print(json.dumps(checks,sort_keys=True))
raise SystemExit(0 if all(checks.values()) else 1)
