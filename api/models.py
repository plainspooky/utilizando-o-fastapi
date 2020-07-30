"""
Modelos de Dados (models.py)
"""
from sqlalchemy import Column, Integer, String

from .database import Base


class Student(Base):
    """
    Modelo de dados para persistir as informações dos estudantes.
    """

    # nome da tabela
    __tablename__ = "students"

    # campos (como definidos em "schemas.py")
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    neighbour = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)
