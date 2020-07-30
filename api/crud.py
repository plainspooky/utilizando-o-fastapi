"""
Funções para acesso ao bando de daados via SQLAlchemy (crud.py)
"""
from typing import Generator

from sqlalchemy.orm import Session

from . import models, schemas

#
students = models.Student


def create_student(
    db: Session, student: schemas.CreateStudentSchema
) -> schemas.StudentSchema:
    """
    Cria um novo estudante a partir dos dados enviados via API.
    """
    fields = {k: v for k, v in student}

    new_student = models.Student(**fields)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


def retrieve_all_students(db: Session) -> Generator:
    """
    Retorna todos os registros dos estudantes.
    """
    return db.query(students).all()


def retrieve_student(db: Session, student_id: int):
    """
    Retorna o registro de um estudate a partir do seu _id_.
    """
    return db.query(students).filter(students.id == student_id).first()


#
#
# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()
#
#
# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
