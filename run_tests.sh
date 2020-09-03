#!/usr/bin/env bash
tempfile=$( tempfile -s ".sqlite3" )

FASTAPI__DATABASE="sqlite:///${tempfile}" \
    pytest --cov=api --cov-report=html -vv ./tests.py && rm -f "$tempfile"

