#!/usr/bin/env bash
# Bash "strict mode"
set -euo pipefail
IFS=$'\n\t'

CMD="gunicorn --bind 0.0.0.0:$PORT lpld.wsgi:application"

# Allow missing envar
set +u
if [[ -z "$DATABASE_URL" ]]; then
    echo "DATABASE_URL env var not specified - Using the SQLite database"

    # Wrap the default command in the litestream exec command to replicate database
    CMD="litestream replicate -config litestream.yml --exec '$CMD'"
fi
# Disallow missing envar
set -u

echo "Running: $CMD"

exec $(eval $CMD)
