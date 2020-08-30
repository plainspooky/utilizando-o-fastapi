"""
Estabelece a conexão do SQLAlchemy com banco de dados, para
alterar a _string_ de conexão vá em `config.py`.

Baseado em [exemplo](https://fastapi.tiangolo.com/tutorial/sql-databases/)
do próprio FastAPI.
"""
from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore

from .config import SQLALCHEMY_DATABASE_ARGS, SQLALCHEMY_DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args=SQLALCHEMY_DATABASE_ARGS
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
