# Bash "strict mode"
set -euo pipefail
IFS=$'\n\t'

echo "Transfer data from PostgreSQL to SQLite"

# Create the database directory for the SQLite file
mkdir -p "$DB_DIR"

echo "Migrate SQLite database..."
USE_SQLITE=true ./manage.py migrate --no-input

echo "Flush SQLite database to remove data created during migrations..."
USE_SQLITE=true ./manage.py flush --no-input

echo "Dump PostgreSQL database..."
mkdir -p ./dbdump
./manage.py dumpdata --natural-foreign --natural-primary --exclude "wagtailcore.PageLogEntry" --indent 4 > ./dbdump/dbdump.json

echo "Load database dump into SQLite..."
USE_SQLITE=true ./manage.py loaddata ./dbdump/dbdump.json

echo "Done."

