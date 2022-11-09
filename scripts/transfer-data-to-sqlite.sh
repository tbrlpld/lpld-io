# Bash "strict mode"
set -euo pipefail
IFS=$'\n\t'

echo "Transfer data from PostgreSQL to SQLite"

$DUMP_FILE=$DB_DIR/dbdump.json

echo "Migrate SQLite database..."
USE_SQLITE=true ./manage.py migrate --no-input

echo "Flush SQLite database to remove data created during migrations..."
USE_SQLITE=true ./manage.py flush --no-input

echo "Dump PostgreSQL database..."
./manage.py dumpdata --natural-foreign --natural-primary --exclude "wagtailcore.PageLogEntry" --indent 4 > $DUMP_FILE

echo "Load database dump into SQLite..."
USE_SQLITE=true ./manage.py loaddata $DUMP_FILE

echo "Done."

