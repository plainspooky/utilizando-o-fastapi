"""
Arquivo principal da API. (main.py)
"""
from datetime import datetime
from typing import Dict, Generator, List

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from .crud import create_student, retrieve_all_students, retrieve_student
from .database import SessionLocal, engine
from .datatypes import StudentListType, StudentType
from .models import Base
from .schemas import CreateStudentSchema, StudentSchema, UpdateStudentSchema

# instancia o FastAPI
app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db() -> Generator:
    """
    Retorna a sessão de conexão do banco de dados.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# carrega o "Banco de Dados" (basicamente lê o arquivo JSON)
# students: StudentListType = json.load(open("students.json", "r"))
#
# def retrieve_student(student_id: int) -> Optional[StudentType]:
#     """
#     (provisório) Recupera no "Banco de Dados" um estudante específico,
#     recebe o _id_ em `student_id`.
#     """
#     if result := list(filter(lambda i: i.get("id") == student_id, students)):
#         return result[0]
#
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail=f"Estudante de 'id={student_id}' não encontrado.",
#     )
#
#
# def get_max() -> int:
#     """
#     (provisório) Retorna o maior valor de _id_ do "Banco de Dados".
#     """
#     max_student = max(students, key=lambda i: i.get("id", 0))
#
#     return max_student.get("id", 0)


@app.get("/health/")
def alive() -> Dict[str, datetime]:
    """
    Retorna a data e hora atuais do servidor (use para verificar se o serviço
    está no ar; consulte regularmente e terá ideia de quando ele deixou de
    funcionar).
    """
    return {"timestamp": datetime.now()}


@app.get("/students/", response_model=List[StudentSchema])
def get_all_students(db: Session = Depends(get_db)) -> StudentListType:
    """
    Retorna todos os estudantes armazenados.
    """
    if response := retrieve_all_students(db):
        return response

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Não existem estudantes cadastrados.",
    )


@app.get("/students/{student_id}/", response_model=StudentSchema)
def get_student(student_id: int, db: Session = Depends(get_db)) -> StudentType:
    """
    Retorna os dados do estudante, recebe o _id_ do estudante em `student_id`
    e retorna as informações armazenadas ou gera uma exceção caso não seja
    encontrado.
    """
    if response := retrieve_student(db, student_id):
        return response

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Estudante de 'id={student_id}' não encontrado.",
    )


@app.delete("/students/{student_id}/")
def delete_student(student_id: int, db: Session = Depends(get_db)) -> None:
    """
    Remove um estudante do banco de dados, recebe o _id_ do estudante em
    `student_id` e retorna uma mensagem de sucesso, caso contrário gera uma
    exceção de não encontrado.
    """
    if response := get_student(db, student_id):
        db.delete(response)
        db.commit()

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Estudante de 'id={student_id}' não encontrado.",
    )


@app.post("/students/", response_model=StudentSchema)
def post_student(
    student: CreateStudentSchema, db: Session = Depends(get_db)
) -> StudentType:
    """
    Insere um novo estudante no banco de dados, recebe todos os campos
    necessários, valida e insere no banco de dados. Retorna o registro
    inserido acrescido do seu `id`.
    """
    if response := create_student(db, student):
        return response

    return response


@app.put("/students/{student_id}", response_model=StudentSchema)
def put_student(student_id: int, student: UpdateStudentSchema) -> StudentType:
    """
    Atualiza os dados de um estudante, recebe o _id_  em `student_id` e a
    lista de campos a modificar dentro do JSON (campos com valor `None`
    serão ignorados).
    """
    ...
    # if old_student := retrieve_student(student_id):
    #     updated_student = {
    #         **old_student,
    #         **{key: value for key, value in student if value},
    #     }
    #
    #     students[students.index(old_student)] = updated_student
    #
    #     return updated_student
    #
    # raise HTTPException(
    #     status_code=status.HTTP_404_NOT_FOUND,
    #     detail=f"Estudante de 'id={student_id}' não encontrado.",
    # )
