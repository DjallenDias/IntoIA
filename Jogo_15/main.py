import classes

estado = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,0,14,15],
]

estado_objetivo = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,0],
]

no = classes.No(estado, None, None, None)
problema = classes.Problema(no, lambda no: no.estado == estado_objetivo)
buscaL = classes.BuscaLargura(problema)
buscaP = classes.BuscaProfundidade(problema)

