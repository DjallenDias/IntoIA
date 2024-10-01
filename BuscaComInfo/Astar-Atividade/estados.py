def acao(destino:str, custo:int):
    return {"destino": destino, "custo": custo}

estados = [
    {"estado": "A", "acoes": [acao("B", 1), acao("C", 2)]},
    {"estado": "B", "acoes": [acao("A", 1), acao("C", 5), acao("D", 3)]},
    {"estado": "C", "acoes": [acao("A", 2), acao("B", 5), acao("E", 4)]},
    {"estado": "D", "acoes": [acao("B", 3), acao("E", 6), acao("F", 1)]},
    {"estado": "E", "acoes": [acao("C", 4), acao("D", 6), acao("F", 1)]},
    {"estado": "F", "acoes": [acao("D", 1), acao("E", 1)]},
]

LEN_ESTADOS = len(estados)