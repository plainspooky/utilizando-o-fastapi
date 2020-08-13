"""
Arquivo principal da API.
"""
import json
from datetime import datetime
from typing import Dict, List, Optional, Union

from fastapi import FastAPI, HTTPException, status

from schemas import CreateStudentSchema, StudentSchema, UpdateStudentSchema

app = FastAPI()

# tipos customizados usados neste módulo
StudentType = Dict[str, Union[float, int, str]]
StudentListType = List[StudentType]

# carrega o "Banco de Dados" (basicamente lê o arquivo JSON)
students: StudentListType = json.load(open("students.json", "r"))


def retrieve_student(student_id: int) -> Optional[StudentType]:
    """
    (provisório) Recupera no "Banco de Dados" um estudante específico,
    recebe o _id_ em `student_id`.
    """
    if result := list(filter(lambda i: i.get("id") == student_id, students)):
        return result[0]

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Estudante de 'id={student_id}' não encontrado.",
    )


def get_max() -> int:
    """
    (provisório) Retorna o maior valor de _id_ do "Banco de Dados".
    """
    max_student = max(students, key=lambda i: i.get("id", 0))

    return max_student.get("id", 0)


@app.get("/health/")
def alive() -> Dict[str, datetime]:
    """
    Retorna a data e hora atuais do servidor (use para verificar se o serviço
    está no ar; consulte regularmente e terá ideia de quando ele deixou de
    funcionar).
    """
    return {"timestamp": datetime.now()}


@app.get("/students/", response_model=List[StudentSchema])
def get_all_students() -> StudentListType:
    """
    Retorna todos os estudantes armazenados.
    """
    if response := students:
        return response

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Não existem estudantes cadastrados.",
    )


@app.get("/students/{student_id}/", response_model=StudentSchema)
def get_student(student_id: int) -> StudentType:
    """
    Retorna os dados do estudante, recebe o _id_ do estudante em `student_id`
    e retorna as informações armazenadas ou gera uma exceção caso não seja
    encontrado.
    """
    if student := retrieve_student(student_id):
        return student

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Estudante de 'id={student_id}' não encontrado.",
    )


@app.delete("/students/{student_id}/")
def delete_student(student_id: int) -> None:
    """
    Remove um estudante do banco de dados, recebe o _id_ do estudante em
    `student_id` e retorna uma mensagem de sucesso, caso contrário gera uma
    exceção de não encontrado.
    """
    if student := retrieve_student(student_id):
        del students[students.index(student)]

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Estudante de 'id={student_id}' não encontrado.",
    )


@app.post("/students/", response_model=StudentSchema)
def post_student(student: CreateStudentSchema) -> StudentType:
    """
    Insere um novo estudante no banco de dados, recebe todos os campos
    necessários, valida e insere no banco de dados. Retorna o registro
    inserido acrescido do seu `id`.
    """
    new_student: StudentType = {**{"id": get_max() + 1}, **student.dict()}

    students.append(new_student)

    return new_student


@app.put("/students/{student_id}", response_model=StudentSchema)
def put_student(student_id: int, student: UpdateStudentSchema) -> StudentType:
    """
    Atualiza os dados de um estudante, recebe o _id_  em `student_id` e a
    lista de campos a modificar dentro do JSON (campos com valor `None`
    serão ignorados).
    """

    if old_student := retrieve_student(student_id):
        updated_student = {
            **old_student,
            **{key: value for key, value in student if value},
        }

        students[students.index(old_student)] = updated_student

        return updated_student

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Estudante de 'id={student_id}' não encontrado.",
    )
