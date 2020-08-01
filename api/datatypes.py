"""
Tipos de dados customizados usados na aplicação.
"""
from typing import Dict, List, Union

StudentType = Dict[str, Union[float, int, str]]
StudentListType = List[StudentType]

UpdateStudentValuesType = Dict[str, Union[int, str]]
