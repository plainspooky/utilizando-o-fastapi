"""
Testes unitários do _schema_ de dados da API.
"""
from api.schemas import CreateStudentSchema, UpdateStudentSchema

from .datatypes import StudentType
from .fixtures import student


class TestStudentchema:
    """
    Como a validação dos estudantes está por conta do `pydantic` é bom
    acrescentar testes para verificar se está tudo certo por lá (caso
    contrário os testes que passaram para a API não valerão de muita
    coisa).
    """

    invalid_state = "Guanabara"
    valid_postal = ["99999-999"]
    invalid_postal = ["99999", "999-999", ""]

    def test_sucess_student_validation(self, student: StudentType) -> None:
        """
        Verifica a validação de dados para um novo estudante.
        """
        try:
            new_student = CreateStudentSchema(**student)

        except ValueError:
            assert False

        else:
            assert True

    def test_fail_student_validation(self, student: StudentType) -> None:
        """
        Verifica a validação de dados para um novo estudante.
        """
        try:
            student["postal_code"] = "99999"
            student["state"] = self.invalid_state
            new_student = CreateStudentSchema(**student)

        except ValueError:
            assert True

        else:
            assert False

    def test_postal_code_validation(self, student: StudentType) -> None:
        """
        Valida que o CEP está sempre dentro do padrão de "99999-999".
        """
        try:
            for postal_code in self.valid_postal + self.invalid_postal:
                student["postal_code"] = postal_code
                __ = CreateStudentSchema(**student)

        except ValueError:
            assert True

        else:
            assert False

    def test_state_validation(self, student: StudentType) -> None:
        """
        Faz a validação do nome do estado, a tentativa de usar um nome
        de estado que não existe deve retornar a exceção `ValueError`.

        Grátis uma pequena aula de história... :grinning:
        """
        new_student = CreateStudentSchema(**student)

        try:
            # Em 1960, com a mudança da Capital para Brasília, o antigo
            # do Distrito Federal, composto apenas pela cidade do Rio
            # de Janeiro, se tornou o estado da Guanabara (GB) e assim
            # permaneceu até o ano de 1975 quando se fundiu ao estado
            # do Rio de Janeiro e tornando-se a capital deste.

            # Logo, é um bom nome para usar no teste...
            new_student_dict = new_student.dict()
            new_student_dict["state"] = self.invalid_state

            updated_student = UpdateStudentSchema(**new_student_dict)

        except ValueError:
            assert True

        else:
            assert False
