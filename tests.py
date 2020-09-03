"""
Testes
"""
from typing import Dict

import pytest
from faker import Faker
from fastapi.testclient import TestClient

from api import app
from api.schemas import CreateStudentSchema, UpdateStudentSchema

StudentType = Dict[str, str]


client = TestClient(app)
fake = Faker(["pt-BR"])


@pytest.fixture(scope="function")
def student() -> StudentType:
    """
    Cria um conjunto completo de dados de estudante.
    """
    # algumas vezes o 'postcode' não põe "-"...
    postcode = fake.postcode()

    return {
        "name": fake.name(),
        "address": fake.street_address(),
        "neighbour": fake.neighborhood(),
        "city": fake.city(),
        "state": fake.state(),
        "postal_code": postcode[0:5] + "-" + postcode[-3:],
    }


@pytest.fixture(scope="function")
def new_student() -> StudentType:
    """
    Cria um novo nome de estudante.
    """
    return {
        "name": fake.name(),
    }


class TestStudentsApi:
    """
    Classe de testes dos métodos HTTP da API que manipulam os dados dos
    estudantes.
    """

    def test_health(self) -> None:
        """
        Verifica se `/health/` retorna um _timestamp_.
        """
        response = client.get("/health/")

        # status do HTTP é 200 e há valor em 'timestamp'?
        assert response.status_code == 200
        assert response.json().get("timestamp") != None

    def test_success_create_student(self, student: StudentType) -> None:
        """
        Verifica se um novo estudante é corretamento criado.
        """
        response = client.post("/students/", json=student)

        # status do HTTP é 201 e há um valor de 'id'?
        assert response.status_code == 201
        assert response.json().get("id")

    def test_success_to_retrieve_student(self, student: StudentType) -> None:
        """
        Vertifica se as informações de um estudante são corretamente
        recuperadas.
        """
        # insere um estudante e recupera seu 'id'...
        data = client.post("/students/", json=student)
        student_id = data.json().get("id")

        response = client.get(f"/students/{student_id}/")

        # status do HTTP é 200 e o que foi inserido é igual ao que voltou?
        assert response.status_code == 200
        assert response.json() == data.json()

    def test_fail_to_retrieve_student(self, student: StudentType) -> None:
        """
        """
        response = client.get(f"/students/0/")
        assert response.status_code == 404

    def test_success_retrieve_all_students(self, student: StudentType) -> None:
        """
        Vertifica se as informações de tofod os estudantes são recuperadas.
        """
        __ = client.post("/students/", json=student)

        response = client.get("/students/")

        assert response.status_code == 200
        assert response.json()

    def test_success_update_student(
        self, student: StudentType, new_student: StudentType
    ) -> None:
        """
        Verifica se as informações do estudante são corretamente alteradas.
        """
        data = client.post("/students/", json=student)
        student_id = data.json().get("id")

        response = client.put(f"/students/{student_id}/", json=new_student)

        assert response.status_code == 201
        assert response.json().get("name") == new_student.get("name")

    def test_fail_update_student(self, new_student: StudentType) -> None:
        """
        Verifica se as informações do estudante são corretamente alteradas.
        """
        response = client.put(f"/students/0/", json=new_student)

        assert response.status_code == 404

    def test_delete_student(self, student: StudentType) -> None:
        """
        Verifica se as informações do estudante são removidas.
        """
        data = client.post("/students/", json=student)
        student_id = data.json().get("id")

        print("->", data)

        pass_response = client.delete(f"/students/{student_id}/")
        assert pass_response.status_code == 204

        fail_response = client.delete(f"/students/{student_id}/")
        assert fail_response.status_code == 404


class TestSchema:
    """
    Testa
    """

    def test_postal_code_validation(self, student: StudentType) -> None:
        """
        """
        try:
            student["postal_code"] = ""
            __ = CreateStudentSchema(**student)
        except ValueError:
            assert True
        else:
            assert False

    def test_state_validation(self, student: StudentType) -> None:
        """
        """
        print(student)
        new_student = CreateStudentSchema(**student)

        try:
            new_student_dict = new_student.dict()
            new_student_dict["state"] = "Guanabara"

            updated_student = UpdateStudentSchema(**new_student_dict)

        except ValueError:
            assert True

        else:
            assert False
