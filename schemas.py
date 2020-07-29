"""
Leiaute dos dados (schema.py)
"""
import re
from typing import Any

from pydantic import BaseModel, validator

from enumerators import StatesBrEnum as StatesEnum

POSTAL_CODE_REGEX = re.compile("[0-9]{5}\\-[0-9]{3}")


class StudentBaseSchema(BaseModel):
    """
    Define a estrura de dados que armazena as informações dos estudantes.
    """

    name: str
    address: str
    neighbour: str
    city: str
    postal_code: str

    @validator("postal_code")
    def validate_postal_code(cls, v: str, **kwargs: int) -> str:
        """
        Verifica se o CEP tem cinco números, hífen e três números.
        """

        if not POSTAL_CODE_REGEX.match(postal_code := v.rjust(9, "0")):
            raise ValueError("O CEP informado é inválido!")

        return postal_code


class CreateStudentSchema(StudentBaseSchema):
    """
    Esquema de dados para ser usado na criação de novos estudantes.
    """

    state: StatesEnum


class StudentSchema(StudentBaseSchema):
    """
    Esquema de dados para ser usado para visualização dos estudantes.
    """

    id: int
    state: StatesEnum


class UpdateStudentSchema(StudentBaseSchema):
    """
    Esquema de dados para a atualização dos dados dos estudantes.
    """

    name: str = ""
    address: str = ""
    neighbour: str = ""
    city: str = ""
    state: str = ""
    postal_code: str = ""

    @validator("state")
    def validate_state(cls, v: Any, **kwargs: int) -> str:
        """
        Valida a unidade da faderação, rem
        """
        try:
            return v if StatesEnum(v) else ""

        except ValueError:
            raise ValueError(f"O valor '{v}' não é válido!")
