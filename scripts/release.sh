#!/usr/bin/env bash
# Bash "strict mode"
set -euo pipefail
IFS=$'\n\t'

if [ $USE_SQLITE != "true" ]; then
    ./manage.py check --deploy --fail-level WARNING
    ./manage.py createcachetable
    ./manage.py migrate --noinput
fi
