#!/usr/bin/env bash
# Bash "strict mode"
set -euo pipefail
IFS=$'\n\t'

CMD="gunicorn --bind 0.0.0.0:$PORT lpld.wsgi:application"

# Allow missing envar
set +u
if [[ -z "$DATABASE_URL" ]]; then
    echo "DATABASE_URL env var not specified - using the SQLite database."

    mkdir -p "$DB_DIR"
    chmod -R a+rwX "$DB_DIR"

    echo "Restoring the SQLite database from bucket."
    litestream restore -config litestream.yml -if-db-not-exists -if-replica-exists "$DB_DIR/db.sqlite3"

    echo "Wrapping the command in the litestream exec to replicate database."
    CMD="litestream replicate -config litestream.yml --exec '$CMD'"
fi
# Disallow missing envar
set -u

echo "Running: $CMD"
exec $(eval $CMD)
