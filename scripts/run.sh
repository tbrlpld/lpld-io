#!/usr/bin/env bash
# Bash "strict mode"
set -euo pipefail
IFS=$'\n\t'

CMD="gunicorn --bind 0.0.0.0:$PORT lpld.wsgi:application"

# The release and the start script are running in different containers.
# This means the original run of the release script does not take effect in the run container.
# Therefore, we need to run the release commands again.
echo "Running release commands."
$(dirname $0)/release.sh

echo "Wrapping the command in the litestream exec to replicate database."
CMD="litestream replicate -config litestream.yml --exec '$CMD'"

echo "Running: $CMD"
#exec $(eval $CMD)
