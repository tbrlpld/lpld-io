# Bash "strict mode"
set -euo pipefail
IFS=$'\n\t'

# Unsetting the DATABASE_URL (with `env -u DATABASE_URL`) will make the sqlite database the active one for the command.
# I could not make it work with `--database sqlite`.

echo "Transfer data from PostgreSQL to SQLite"

echo "Migrate SQLite database..."
env -u DATABASE_URL ./manage.py migrate --no-input

echo "Flush SQLite database to remove data created during migrations..."
env -u DATABASE_URL ./manage.py flush --no-input

echo "Dump PostgreSQL database..."
./manage.py dumpdata --natural-foreign --natural-primary --exclude "wagtailcore.PageLogEntry" --indent 4 > ./dbdump/dbdump.json

echo "Load database dump into SQLite..."
env -u DATABASE_URL ./manage.py loaddata ./dbdump/dbdump.json

echo "Done."

