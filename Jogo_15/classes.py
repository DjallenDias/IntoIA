from copy import deepcopy
from time import sleep

class No:
    def __init__(self, estado, custo, pai, acao):
        self.estado = estado
        "Matriz 4x4"
        self.custo = custo
        self.pai = pai
        self.acao = acao

    def __str__(self):
        return '\n'.join([' '.join(map(str, linha)) for linha in self.estado])

    def __repr__(self):
        return f"Matriz({self.estado})" 

    def achar_espaco_vazio(self):
        for i in range(4):
            for j in range(4):
                if self.estado[i][j] == 0:
                    return i, j

    def filhos(self):
        filhos = []
        x, y = self.achar_espaco_vazio()

        movimentos = [
            (x - 1, y),  # Mover para cima
            (x + 1, y),  # Mover para baixo
            (x, y - 1),  # Mover para a esquerda
            (x, y + 1)   # Mover para a direita
        ]

        for i, j in movimentos:
            if (0 <= i < 4) and (0 <= j < 4):
                novo_estado = deepcopy(self.estado)
                novo_estado[x][y], novo_estado[i][j] = novo_estado[i][j], novo_estado[x][y]
                n_no = No(novo_estado, None, self, None)
                filhos.append(n_no)

        return filhos
    
    def constroi_solucao(self):
        no_atual = self
        solucao = [no_atual]

        while no_atual.pai != None:
            no_atual = no_atual.pai
            solucao.insert(0, no_atual)

        return solucao

class Problema:
    def __init__(self, inicial:No, objetivo):
        self.inicial = inicial
        self.objetivo = objetivo

BUSCA_INICIANDO = 0
BUSCA_FALHOU = 1
BUSCA_SUCESSO = 2
BUSCA_EM_CURSO = 3

class BuscaLargura:
    def __init__(self, problema:Problema):
        self.problema = problema
        self.fronteira = [problema.inicial]
        self.visitados = [problema.inicial.estado]
        self.situacao = BUSCA_INICIANDO
        self.solucao = []

    def verifica_possivel(self):
        numeros = []
        substituicoes = 0

        for linha in self.problema.inicial.estado:
            for item in linha:
                if item != 0: numeros.append(item)

        while len(numeros) > 0:
            num_ant = numeros.pop(0)

            for num in numeros:
                if num_ant > num:
                    substituicoes += 1

        return (substituicoes%2) == 0

    def executar(self):
        while self.situacao != BUSCA_FALHOU and self.situacao != BUSCA_SUCESSO:
            self.busca_passo()

        if self.situacao == BUSCA_FALHOU:
            print("Busca falhou")

        elif self.situacao == BUSCA_SUCESSO:
            print("Busca teve sucesso")
            print(f"Solucao: {self.solucao}")

        return


    def busca_passo(self):
        if not self.verifica_possivel():
            print("Nao eh posivel achar a solucao")
            self.situacao = BUSCA_FALHOU
            return
        
        if (self.situacao == BUSCA_FALHOU):
            print("Busca falhou")
            return

        if (self.situacao == BUSCA_SUCESSO):
            print("Busca chegou ao objetivo")
            return
        
        try:
            no = self.fronteira.pop(0)
        
        except IndexError:
            self.situacao = BUSCA_FALHOU
            return
        
        if self.problema.objetivo(no):
            self.situacao = BUSCA_SUCESSO
            self.solucao = no.constroi_solucao()
            return
        
        for filho in no.filhos():
            if not (filho in self.fronteira) and not (filho.estado in self.visitados):
                self.fronteira.append(filho)
                self.visitados.append(filho.estado)

        return

class BuscaProfundidade:
    def __init__(self, problema:Problema):
        self.problema = problema
        self.fronteira = [problema.inicial]
        self.visitados = [problema.inicial.estado]
        self.situacao = BUSCA_INICIANDO
        self.solucao = []

    def verifica_possivel(self):
        numeros = []
        substituicoes = 0
        for linha in self.problema.inicial.estado:
            for item in linha:
                if item != 0: numeros.append(item)

        while len(numeros) > 0:
            num_ant = numeros.pop(0)

            for num in numeros:
                if num_ant > num:
                    substituicoes += 1

        return (substituicoes%2) == 0

    def executar(self):
        while self.situacao != BUSCA_FALHOU and self.situacao != BUSCA_SUCESSO:
            self.busca_passo()

        if self.situacao == BUSCA_FALHOU:
            print("Busca falhou")

        elif self.situacao == BUSCA_SUCESSO:
            print("Busca teve sucesso")
            print(f"Solucao: {self.solucao}")

        return


    def busca_passo(self):
        if not self.verifica_possivel():
            print("Nao eh posivel achar a solucao")
            self.situacao = BUSCA_FALHOU
            return
        
        if (self.situacao == BUSCA_FALHOU):
            print("Busca falhou")
            return

        if (self.situacao == BUSCA_SUCESSO):
            print("Busca chegou ao objetivo")
            return
        
        try:
            no = self.fronteira.pop(0)
        
        except IndexError:
            self.situacao = BUSCA_FALHOU
            return
        
        if self.problema.objetivo(no):
            self.situacao = BUSCA_SUCESSO
            self.solucao = no.constroi_solucao()
            return
        
        for filho in no.filhos():
            if not (filho in self.fronteira) and not (filho.estado in self.visitados):
                self.fronteira.insert(0, filho)
                self.visitados.append(filho.estado)

        return
        