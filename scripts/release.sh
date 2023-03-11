#!/usr/bin/env bash
# Bash "strict mode"
set -euo pipefail
IFS=$'\n\t'

echo "Restoring the SQLite database from bucket."
litestream restore -config litestream.yml -if-db-not-exists -if-replica-exists "$DB_DIR/db.sqlite3"

./manage.py check --deploy --fail-level WARNING
./manage.py createcachetable
./manage.py migrate --noinput
