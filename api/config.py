"""
Parâmetros e valores relacionados à configuração da API.

São eles:

* `SQLALCHEMY_DATABASE_URL` : A _string_ contendo a
  [URL para conexão](https://docs.sqlalchemy.org/en/13/core/engines.html#database-urls)
  ao banco de dados que é recuperada da variável de ambiente
  `API__DATABASE` através do [Tomatic](https://github.com/plainspooky/tomatic).
* `SQLALCHEMY_DATABASE_ARGS` : Parâmetros de
  [conexão](https://docs.sqlalchemy.org/en/13/core/engines.html#custom-dbapi-args)
  ao banco de dados.
"""
from tomatic import Tomatic
from tomatic.buckets import EnvironBucket

t = Tomatic(EnvironBucket, static_profile="FASTAPI", raise_if_none=ValueError)

SQLALCHEMY_DATABASE_URL = t.DATABASE__str__

SQLALCHEMY_DATABASE_ARGS = {"check_same_thread": False}
