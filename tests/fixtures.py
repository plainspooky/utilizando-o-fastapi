"""
Fixtures usados nos testes.
"""
import pytest
from faker import Faker

from .datatypes import StudentType

# instancia o 'Faker' definindo-o para gerar dados falsos em português
# brasileiro
fake = Faker(["pt-BR"])


@pytest.fixture(scope="function")
def student() -> StudentType:
    """
    Cria um conjunto completo de dados de estudante toda vez que uma
    função/método de testes for executado (`scope="function"`).
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
    Cria um novo nome de estudante cada vez que uma função/método de
    testes for executado (`scope="function"`).
    """
    return {
        "name": fake.name(),
    }
