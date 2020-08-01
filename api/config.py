"""
Parâmetros e valores relacionados à configuração da API.

São eles:

* `SQLALCHEMY_DATABASE_URL` : A _string_ contento a
  [URL para conexão](https://docs.sqlalchemy.org/en/13/core/engines.html#database-urls)
  ao banco de dados.
* `SQLALCHEMY_DATABASE_ARGS` : Parâmetros de
  [conexão](https://docs.sqlalchemy.org/en/13/core/engines.html#custom-dbapi-args)
  ao banco de dados.
"""
SQLALCHEMY_DATABASE_URL = "sqlite:///db.sqlite3"
SQLALCHEMY_DATABASE_ARGS = {"check_same_thread": False}
