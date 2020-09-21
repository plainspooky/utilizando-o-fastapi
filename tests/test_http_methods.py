"""
Testes unitários da API.
"""
from datetime import datetime

from fastapi.testclient import TestClient

from api import app

from .datatypes import StudentType
from .fixtures import student, student_name  # noqa: F401

# instancia a API dentro das rotinas de teste do FastAPI
client = TestClient(app)


def test_health() -> None:
    """
    Verifica se `/health/` retorna um _timestamp_ ao ser consultado.
    """
    response = client.get("/health/")

    # status do HTTP é 200 e há valor em 'timestamp'?
    assert response.status_code == 200

    try:
        assert datetime.fromisoformat(response.json().get("timestamp"))
    except ValueError:
        assert False


class TestStudentsApi:
    """
    Classe de testes dos métodos HTTP da API que manipulam os dados dos
    estudantes.
    """

    def test_success_create_student(self, student: StudentType) -> None:
        """
        Verifica se um novo estudante é corretamento criado, os dados do
        estudante devem conter o campo "id".
        """
        response = client.post("/students/", json=student)

        # status do HTTP é 201 e há um valor de 'id'?
        assert response.status_code == 201
        assert response.json().get("id")

    def test_success_retrieve_student(self, student: StudentType) -> None:
        """
        Vertifica se as informações de estudante são corretamente
        recuperadas. Um novo estudante é inserido para eu ter certeza
        de que há ao menos alguém para recuperar.
        """
        # insere um estudante e recupera seu 'id'...
        data = client.post("/students/", json=student)
        student_id = data.json().get("id")

        response = client.get(f"/students/{student_id}/")

        # status do HTTP é 200 e o que foi inserido é igual ao que voltou?
        assert response.status_code == 200
        assert response.json() == data.json()

    def test_fail_retrieve_student(self, student: StudentType) -> None:
        """
        Verifica se a tentativa de recuperar um estudante que não existe
        retorna o status 404 do HTTP.
        """
        response = client.get("/students/0/")

        # o status do HTTP é 404?
        assert response.status_code == 404

    def test_success_retrieve_all_students(self, student: StudentType) -> None:
        """
        Vertifica se todos os estudantes são recuperadas, ao menos um
        estudante é criado para garantir que exista algo na base de dados.
        """
        client.post("/students/", json=student)

        response = client.get("/students/")

        # o status do HTTP é 200 e há alguma coisa dentro de JSON?
        assert response.status_code == 200
        assert response.json()

    def test_success_update_student(
        self, student: StudentType, student_name: StudentType
    ) -> None:
        """
        Verifica se as informações do estudante são corretamente alteradas.
        """
        data = client.post("/students/", json=student)
        student_id = data.json().get("id")

        response = client.put(f"/students/{student_id}/", json=student_name)

        # o status do HTTP é 201 e o JSON da reposta tem um campo 'nome'
        # com mesmo valor que aquele usado para atualizar o registro?
        assert response.status_code == 201
        assert response.json().get("name") == student_name.get("name")

    def test_fail_update_student(self, student_name: StudentType) -> None:
        """
        Verifica se a tentativa de alterar um estudante que não existe
        retorna o status 404 do HTTP. Lembrando que a validação está por
        conta do pydantic.
        """
        response = client.put("/students/0/", json=student_name)

        # o status do HTTP é 404?
        assert response.status_code == 404

    def test_success_delete_student(self, student: StudentType) -> None:
        """
        Verifica se as informações do estudante são removidas
        corretamente.
        """
        data = client.post("/students/", json=student)
        student_id = data.json().get("id")

        response = client.delete(f"/students/{student_id}/")

        # o status do HTTP é 204?
        assert response.status_code == 204

    def test_fail_delete_student(self) -> None:
        """
        Verifica se a tentativa de remoer um estudante que não existe
        retorna o status 404 do HTTP.
        """
        response = client.delete("/students/0/")

        # o status do HTTP é 404?
        assert response.status_code == 404
