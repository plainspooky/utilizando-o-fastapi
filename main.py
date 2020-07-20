"""
Arquivo principal da API.
"""
import json
from datetime import datetime
from typing import Dict, List, Union

from fastapi import FastAPI, HTTPException, status

app = FastAPI()

# carrega o "Banco de Dados" (basicamente um arquivo JSON)
students = json.load(open("students.json", "r"))


@app.get("/health/")
def alive() -> Dict[str, datetime]:
    """
    Retorna a data e hora atuais do servidor (use para verificar se o serviço
    está no ar; consulte regularmente e terá ideia de quando ele deixou de
    funcionar).
    """
    return {"timestamp": datetime.now()}


@app.get("/students/")
def get_all_students() -> List[Dict[str, Union[float, int, str]]]:
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
def get_student(student_id: int) -> Dict[str, Union[float, int, str]]:
    """
    Retorna os dados do estudante, recebe o _id_ do estudante em `student_id`
    e retorna as informações armazenadas ou gera uma exceção caso não seja
    encontrado.
    """
    if response := list(filter(lambda i: i.get("id") == student_id, students)):
        return response[0]

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Estudante de 'id={student_id}' não encontrado.",
    )


@app.delete("/students/{student_id}/")
def delete_student(student_id: int) -> Dict[str, bool]:
    """
    Remove um estudante do banco de dados, erecebe o _id_ do estudante em
    `student_id` e retorna uma mensagem de sucesso, caso contrário gera uma
    exceção de não encontrado.
    """
    if response := list(filter(lambda i: i.get("id") == student_id, students)):
        del students[students.index(response[0])]
        return {"success": True}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Estudante de 'id={student_id}' não encontrado.",
    )
