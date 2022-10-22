set -euo pipefail
IFS=$'\n\t'
# Unsetting the DATABASE_URL will make the sqlite database the active one for the commnd.
# I could not make it work with `--database sqlite`.
env -u DATABASE_URL ./manage.py migrate && \
env -u DATABASE_URL ./manage.py flush && \
./manage.py dumpdata --natural-foreign --natural-primary --exclude "wagtailcore.PageLogEntry" --indent 4 > ./dbdump/dbdump.json && \
env -u DATABASE_URL ./manage.py loaddata ./dbdump/dbdump.json

