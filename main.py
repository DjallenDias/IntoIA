import classes

estado = [
    [1,2,3],
    [4,5,0],
    [6,7,8],
]

estado_objetivo = [
    [1,2,3],
    [4,5,6],
    [7,8,0],
]

no = classes.No(estado, None, None, None)
problema = classes.Problema(no, lambda no: no.estado == estado_objetivo)
buscaL = classes.BuscaLargura(problema)
buscaP = classes.BuscaProfundidade(problema)

