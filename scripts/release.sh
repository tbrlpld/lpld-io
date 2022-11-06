#!/usr/bin/env bash
# Bash "strict mode"
set -euo pipefail
IFS=$'\n\t'

mkdir -p "$DB_DIR"

# Allow missing envar
set +u
if [[ -z "$DATABASE_URL" ]]; then
    echo "DATABASE_URL env var not specified - Using the SQLite database"

    echo "Replicating the SQLite database from bucket"
    litestream restore -config litestream.yml -if-db-not-exists -if-replica-exists "$DB_DIR/db.sqlite3"
fi
# Disallow missing envar
set -u

chmod -R a+rwX "$DB_DIR"

./manage.py check --deploy --fail-level WARNING
./manage.py createcachetable
./manage.py migrate --noinput
