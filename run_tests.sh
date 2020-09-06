#!/usr/bin/env bash
#
# Simplifica o processo de executar os testes
#

# arquivo temporário com o banco em SQLite3
tempfile=$( tempfile -s ".sqlite3" )

export PYTHONPATH=$( pwd )
export FASTAPI__DATABASE="sqlite:///${tempfile}"

printf "Using '%s' for test database.\n\n" "${FASTAPI__DATABASE}"

pytest --cov=api --cov-report=html -vv && rm -f "$tempfile"

