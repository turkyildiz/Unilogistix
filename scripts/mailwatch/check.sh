#!/usr/bin/env bash
# Print inbox messages for the watched mailboxes not seen in a previous run.
# maestro@dqfile.ai added 2026-09-18 for Team DQF vendor replies (F-045: same Workspace).
set -euo pipefail
GAM=~/.local/bin/gam
STATE=~/.local/state/unilogistix-mailwatch; mkdir -p "$STATE"
for addr in maestro@unilogistix.com ilker@unilogistix.com maestro@dqfile.ai; do
  case "$addr" in *@unilogistix.com) u="${addr%@*}";; *) u="$addr";; esac
  seen="$STATE/$u.seen"; touch "$seen"
  $GAM user "$addr" print messages query 'in:inbox newer_than:3d' max_to_print 50 2>/dev/null \
    | python3 -c '
import csv,sys
seen=set(open(sys.argv[1]).read().split())
rows=[r for r in csv.DictReader(sys.stdin) if r["id"] not in seen]
for r in rows: print(f"{sys.argv[2]}\t{r['"'"'id'"'"']}\t{r['"'"'Date'"'"']}\t{r['"'"'From'"'"']}\t{r['"'"'Subject'"'"']}")
open(sys.argv[1],"a").write("".join(r["id"]+"\n" for r in rows))
' "$seen" "$u"
done
