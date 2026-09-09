#!/usr/bin/env python3
"""Run on the existing vault host. Secret values never enter output or argv."""
import json
import os
from pathlib import Path
import urllib.error
import urllib.request

BASE = os.environ['BAO_ADDR'].rstrip('/') + '/v1/'
ADMIN = Path(os.environ['BAO_ADMIN_TOKEN_FILE']).read_text().strip()

def call(path, data=None, token=ADMIN, method=None):
    headers = {'Content-Type': 'application/json'}
    if token:
        headers['X-Vault-Token'] = token
    req = urllib.request.Request(BASE + path, headers=headers,
        data=None if data is None else json.dumps(data).encode(), method=method)
    with urllib.request.urlopen(req, timeout=10) as response:
        body = response.read()
        return json.loads(body) if body else {}

def denied(path, token, data=None):
    try:
        call(path, data, token)
    except urllib.error.HTTPError as exc:
        assert exc.code == 403, (path, exc.code)
        return
    raise AssertionError('Expected access denial: ' + path)

mounts = call('sys/mounts')['data']
if 'unilogistix/' not in mounts:
    call('sys/mounts/unilogistix', {'type': 'kv', 'options': {'version': '2'}})
else:
    assert mounts['unilogistix/']['type'] == 'kv'
    assert mounts['unilogistix/']['options']['version'] == '2'
call('unilogistix/config', {'max_versions': 10, 'cas_required': True})
auth = call('sys/auth')['data']
if 'unilogistix-approle/' not in auth:
    call('sys/auth/unilogistix-approle', {'type': 'approle'})
else:
    assert auth['unilogistix-approle/']['type'] == 'approle'
policy = '''path "unilogistix/data/bootstrap/health" {
  capabilities = ["read"]
}
path "secret/*" {
  capabilities = ["deny"]
}
'''
call('sys/policies/acl/unilogistix-bootstrap-read', {'policy': policy})
role_path = 'auth/unilogistix-approle/role/bootstrap-reader'
call(role_path, {'token_policies': ['unilogistix-bootstrap-read'],
    'token_no_default_policy': True, 'token_ttl': '5m', 'token_max_ttl': '15m',
    'secret_id_ttl': '5m', 'secret_id_num_uses': 1, 'bind_secret_id': True})
try:
    call('unilogistix/data/bootstrap/health', {'options': {'cas': 0},
        'data': {'purpose': 'non-sensitive bootstrap verification', 'status': 'ready'}})
except urllib.error.HTTPError as exc:
    if exc.code != 400:
        raise
    # Existing canary must be readable; never overwrite it during a rerun.
    call('unilogistix/data/bootstrap/health')
role_id = call(role_path + '/role-id')['data']['role_id']
secret_id = call(role_path + '/secret-id', {})['data']['secret_id']
login = {'role_id': role_id, 'secret_id': secret_id}
token = call('auth/unilogistix-approle/login', login, token=None)['auth']['client_token']
try:
    assert call('unilogistix/data/bootstrap/health', token=token)['data']['data']['status'] == 'ready'
    denied('secret/data/platform/deploy/probe', token)
    denied('secret/data/freightex/platform/deploy/probe', token)
    denied('unilogistix/data/ventures/other/probe', token)
    denied('unilogistix/data/bootstrap/health', token, {'options': {'cas': 1}, 'data': {'status': 'bad'}})
    denied('sys/mounts', token)
    denied('unilogistix/data/bootstrap/health', None)
    try:
        call('auth/unilogistix-approle/login', login, token=None)
        raise AssertionError('Single-use SecretID was reusable')
    except urllib.error.HTTPError as exc:
        assert exc.code in (400, 403)
finally:
    call('auth/token/revoke', {'token': token})
denied('unilogistix/data/bootstrap/health', token)
print(json.dumps({'mount': 'unilogistix/', 'identity': 'bootstrap-reader',
    'read': 'PASS', 'cross_project_denial': 'PASS', 'write_denial': 'PASS',
    'admin_denial': 'PASS', 'anonymous_denial': 'PASS',
    'single_use_login': 'PASS', 'revocation': 'PASS',
    'provider_credentials_imported': False}))
