#!/usr/bin/env bash
# new_link.sh <id>: make one secret link for a person, register its hash with the Worker, print the link once.
# The key never leaves this machine except inside the printed URL that Oscar hands over himself.
# Needs: RUNNER_TOKEN_FILE (chmod 600, the runner token), BASE (default https://digest-preview.projetrefonte.com).
set -euo pipefail
id="${1:?usage: new_link.sh <id>}"
case "$id" in [a-z0-9]*) ;; *) echo "id must be lowercase letters, digits, dashes" >&2; exit 1;; esac
BASE="${BASE:-https://digest-preview.projetrefonte.com}"
tok="$(cat "${RUNNER_TOKEN_FILE:?set RUNNER_TOKEN_FILE}")"
key="$(openssl rand -base64 32 | tr '+/' '-_' | tr -d '=')"
hash="$(printf '%s' "$key" | sha256sum | cut -d' ' -f1)"
code="$(curl -sS -o /dev/null -w '%{http_code}' -X PUT "$BASE/r/links/$id" \
  -H "authorization: Bearer $tok" -H 'content-type: application/json' \
  --data "{\"hash\":\"$hash\"}")"
if [ "$code" != "200" ]; then echo "Worker answered $code" >&2; exit 1; fi
echo "$BASE/s/$key"
