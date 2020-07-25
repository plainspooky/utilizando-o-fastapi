"""
Arquivo principal da API.
"""
import json
from datetime import datetime
from typing import Dict, List, Optional, Union

from fastapi import FastAPI, HTTPException, status

app = FastAPI()

# tipos customizados usados neste módulo
StudentType = Dict[str, Union[float, int, str]]
StudentListType = List[StudentType]

# carrega o "Banco de Dados" (basicamente lê o arquivo JSON)
students: StudentListType = json.load(open("students.json", "r"))


def retrieve_student(student_id: int) -> Optional[StudentType]:
    """
    Recupera no "Banco de Dados" um estudante específico, recebe o _id_
    em `student_id`.
    """
    result: StudentListType = list(
        filter(lambda i: i.get("id") == student_id, students)
    )
    return result[0] if result else None


@app.get("/health/")
def alive() -> Dict[str, datetime]:
    """
    Retorna a data e hora atuais do servidor (use para verificar se o serviço
    está no ar; consulte regularmente e terá ideia de quando ele deixou de
    funcionar).
    """
    return {"timestamp": datetime.now()}


@app.get("/students/")
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


@app.get("/students/{student_id}/")
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
def delete_student(student_id: int):
    """
    Remove um estudante do banco de dados, recebe o _id_ do estudante em
    `student_id` e retorna uma mensagem de sucesso, caso contrário gera uma
    exceção de não encontrado.
    """
    if student := retrieve_student(student_id):
        del students[students.index(student)]
        return {"success": True}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Estudante de 'id={student_id}' não encontrado.",
    )
