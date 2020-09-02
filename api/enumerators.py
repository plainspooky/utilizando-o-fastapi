"""
As enumerações que não precisam estar no banco de dados estão aqui.
"""
from enum import Enum


class StatesAoEnum(str, Enum):
    """
    Lista das províncias angolanas com suas respectivas siglas.

    fonte: [Wikipédia](https://pt.wikipedia.org/wiki/Prov%C3%ADncias_de_Angola)
    """

    bgo = "Bengo"
    bgu = "Benguela"
    bie = "Bié"
    cab = "Cabinda"
    ccu = "Cuando-Cubango"
    cno = "Cuanza Norte"
    cus = "Cuanza Sul"
    cnn = "Cunene"
    hua = "Huambo"
    hui = "Huíla"
    lua = "Luanda"
    lno = "Lunda Norte"
    lsu = "Lunda Sul"
    mal = "Malanje"
    mox = "Moxico"
    nam = "Namibe"
    uig = "Uíge"
    zai = "Zaire"


class StatesBrEnum(str, Enum):
    """
    Lista dos estados brasileiros e suas respectivas siglas.
    """

    ac = "Acre"
    al = "Alagoas"
    ap = "Amapá"
    am = "Amazonas"
    ba = "Bahia"
    ce = "Ceará"
    df = "Distrito Federal"
    es = "Espírito Santo"
    go = "Goiás"
    ma = "Maranhão"
    mt = "Mato Grosso"
    ms = "Mato Grosso do Sul"
    mg = "Minas Gerais"
    pa = "Pará"
    pb = "Paraíba"
    pr = "Paraná"
    pe = "Pernambuco"
    pi = "Piauí"
    rj = "Rio de Janeiro"
    rn = "Rio Grande do Norte"
    rs = "Rio Grande do Sul"
    ro = "Rondônia"
    rr = "Roraima"
    sc = "Santa Catarina"
    sp = "São Paulo"
    se = "Sergipe"
    to = "Tocantins"
