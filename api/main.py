"""
Arquivo principal da API contendo os métodos HTTP implementados.
"""
from datetime import datetime
from typing import Dict, Generator

from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session  # type: ignore

from .crud import (
    create_student,
    remove_student,
    retrieve_all_students,
    retrieve_student,
    update_student,
)
from .database import Base, SessionLocal, engine
from .datatypes import StudentType
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


@app.get("/health/")
def alive() -> Dict[str, datetime]:
    """
    Retorna a data e hora atuais do servidor (use para verificar se o serviço
    está no ar; consulte regularmente e terá ideia de quando ele deixou de
    funcionar).
    """
    return {"timestamp": datetime.now()}


@app.get("/students/", status_code=status.HTTP_200_OK)
def get_all_students(db: Session = Depends(get_db)) -> Generator:
    """
    Retorna todos os estudantes armazenados.
    """

    if result := retrieve_all_students(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Não existem estudantes cadastrados.",
    )


@app.get(
    "/students/{student_id}/", status_code=status.HTTP_200_OK,
)
def get_student(student_id: int, db: Session = Depends(get_db)) -> StudentType:
    """
    Retorna os dados do estudante, recebe o _id_ do estudante em `student_id`
    e retorna as informações armazenadas ou gera uma exceção caso não seja
    encontrado.
    """
    if result := retrieve_student(db, student_id):
        return result

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Estudante de 'id={student_id}' não encontrado.",
    )


@app.delete("/students/{student_id}/", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, db: Session = Depends(get_db)) -> None:
    """
    Remove um estudante do banco de dados, recebe o _id_ do estudante em
    `student_id` e retorna uma mensagem de sucesso, caso contrário gera uma
    exceção de não encontrado.
    """
    if not remove_student(db, student_id):

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Estudante de 'id={student_id}' não encontrado.",
        )


@app.post(
    "/students/", status_code=status.HTTP_201_CREATED,
)
def post_student(
    student: CreateStudentSchema, db: Session = Depends(get_db),
) -> StudentType:
    """
    Insere um novo estudante no banco de dados, recebe todos os campos
    necessários, valida e insere no banco de dados. Retorna o registro
    inserido acrescido do seu `id`.
    """
    if result := create_student(db, student):
        return result

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@app.put(
    "/students/{student_id}", status_code=status.HTTP_201_CREATED,
)
def put_student(
    student_id: int,
    student: UpdateStudentSchema,
    db: Session = Depends(get_db),
) -> StudentType:
    """
    Atualiza os dados de um estudante, recebe o _id_  em `student_id` e a
    lista de campos a modificar dentro do JSON (campos com valor `None`
    serão ignorados).
    """
    if result := update_student(
        db, student_id, {key: value for key, value in student if value}
    ):
        return result

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Estudante de 'id={student_id}' não encontrado.",
    )
