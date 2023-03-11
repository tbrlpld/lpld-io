#!/usr/bin/env bash
# Bash "strict mode"
set -euo pipefail
IFS=$'\n\t'

CMD="gunicorn --bind 0.0.0.0:$PORT lpld.wsgi:application"

echo "Restoring the SQLite database from bucket."
litestream restore -config litestream.yml -if-db-not-exists -if-replica-exists "$DB_DIR/db.sqlite3"

# The release and the start script are running in different containers.
# This means the original run of the release script does not take effect in the run container.
echo "Running release commands."
./manage.py check --deploy --fail-level WARNING
./manage.py createcachetable
./manage.py migrate --noinput

echo "Wrapping the command in the litestream exec to replicate database."
CMD="litestream replicate -config litestream.yml --exec '$CMD'"

echo "Running: $CMD"
exec $(eval $CMD)
