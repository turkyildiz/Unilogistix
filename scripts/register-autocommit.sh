#!/usr/bin/env bash
# Governance auto-commit (housekeeping contract §1: host cron + script).
# Commits and pushes changes under governance/ in the Unilogistix repo so the
# Board register never sits only on Gram's disk. Idempotent: nothing to commit
# means nothing happens. Never touches files outside governance/.
set -euo pipefail
REPO="${UNILOGISTIX_REPO:-$HOME/Unilogistix}"
cd "$REPO"
git add -A governance
if git diff --cached --quiet; then
  exit 0
fi
version=$(sed -n 's/^Version: \([0-9.]*\).*/\1/p' governance/BOARD_REGISTER.md | head -1)
entries=$(git diff --cached governance/BOARD_REGISTER.md | grep -o '^+- F-[0-9]*' | sed 's/^+- //' | sort -u | tr '\n' ' ')
git -c user.name="Unilogistix governance (host cron)" -c user.email="turkyildiz@gmail.com" \
  commit -q -m "Board register v${version:-?}: ${entries:-governance update}" \
  -m "Auto-committed by scripts/register-autocommit.sh on $(hostname). Entries are Maestro-authored; Sherlock review required."
git push -q origin HEAD
logger -t register-autocommit "committed register v${version:-?} (${entries:-governance update})" 2>/dev/null || true
