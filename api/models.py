"""
Os modelos do banco de dados utilizando a descrição do SQLAlchemy.
"""
from sqlalchemy import Column, Integer, String

from .database import Base


class Student(Base):
    """
    Modelo de dados para persistir as informações dos estudantes.
    """

    # nome da tabela
    __tablename__ = "students"

    # campos (tal qual definidos em "schemas.py")
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    neighbour = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)
