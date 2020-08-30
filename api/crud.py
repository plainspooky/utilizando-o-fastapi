"""
Funções para o acesso ao banco de daados via SQLAlchemy via ORM ao
invés de consultas escritas diretamente em SQL.
"""
from typing import Generator

from sqlalchemy.orm import Session  # type: ignore

from .datatypes import UpdateStudentValuesType
from .models import Student
from .schemas import CreateStudentSchema, StudentSchema

# modelo de dados dos estudantes para SQL
students = Student


def create_student(db: Session, student: CreateStudentSchema):
    """
    Cria um novo estudante a partir dos dados enviados via API.
    """
    # cria um novo registro de estudante e o insere no banco
    new_student = Student(**student.dict())
    db.add(new_student)
    db.commit()

    # recarrega os dados do estudante antes de envi=a-lo de volta
    db.refresh(new_student)

    return new_student


def retrieve_all_students(db: Session) -> Generator:
    """
    Retorna todos os registros dos estudantes.
    """
    # pega tudo o que tem no banco de dados e envia...
    return db.query(students).all()


def retrieve_student(db: Session, student_id: int):
    """
    Retorna o registro de um estudate a partir do seu _id_.
    """
    # pega apenas o estudante com o id correto e o envia
    return db.query(students).filter(students.id == student_id).first()


def update_student(
    db: Session, student_id: int, values: UpdateStudentValuesType
):
    """
    Atualiza o registro de um estudante a partir do seu _id_ usando os
    novos valores em `values`.
    """
    # verifica se o estudante existe...
    if student := retrieve_student(db, student_id):
        # altera os valores e submete as alterações
        db.query(students).filter(students.id == student_id).update(values)
        db.commit()

        # atualiza o conteúdo antes de enviá-lo de volta
        db.refresh(student)

        return student


def remove_student(db: Session, student_id: int) -> bool:
    """
    Remove o registro de um estudate a partir do seu _id_.
    """
    # verifica se o estudante existe...
    if student := retrieve_student(db, student_id):
        # daí o apaga do banco de dados
        db.delete(student)
        db.commit()

        # retorna `True`, estudante exisita e foi apagado
        return True

    # retorna `False`
    return False
