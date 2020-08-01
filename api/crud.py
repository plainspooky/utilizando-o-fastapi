"""
Funções para o acesso ao banco de daados via SQLAlchemy via ORM ao
invés de consultas escritas diretamente em SQL.
"""
from typing import Generator

from sqlalchemy.orm import Session

from .datatypes import UpdateStudentValuesType
from .models import Student
from .schemas import CreateStudentSchema, StudentSchema

# modelo de dados dos estudantes para SQL
students = Student


def create_student(db: Session, student: CreateStudentSchema) -> StudentSchema:
    """
    Cria um novo estudante a partir dos dados enviados via API.
    """
    # cria um novo registro de estudante e o insere no banco
    new_student = Student(**student.dict())
    db.add(new_student)
    db.commit()

    # recarrega os dados do estudante e envia de volta...
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
    Atualiza o registro de um estui
    """
    # pega o estudante com o id informado
    if student := db.query(students).filter(students.id == student_id).first():
        db.query(students).filter(students.id == student_id).update(values)
        db.commit()
        db.refresh(student)

        return student


def remove_student(db: Session, student_id: int) -> bool:
    """
    Remove o registro de um estudate a partir do seu _id_.
    """
    # pega o estudante com o id informado, se existe o apaga
    if student := db.query(students).filter(students.id == student_id).first():
        db.delete(student)
        db.commit()

        # retorna `True`, estudante exisita e foi apagado
        return True

    # retorna ``
    return False
