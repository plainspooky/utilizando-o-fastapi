"""
Tipos de dados (datatypes.py)
"""
from typing import Dict, List, Union

StudentType = Dict[str, Union[float, int, str]]
StudentListType = List[StudentType]
