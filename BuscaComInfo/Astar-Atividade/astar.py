from heapq import heappush, heappop

import estados
import heuristica

class No:
    def __init__(self, estado:str, custo, pai, acao):
        self.estado = estado
        self.custo = custo
        self.pai = pai
        self.acao = acao

    def __str__(self):
        return f'({self.estado}, {self.custo})'

    def __repr__(self):
        return self.__str__()
    
    def __lt__(self, other:"No"):
        return self.custo < other.custo

    def filhos(self, problema:"Problema"):
        espaco_acoes = next(e for e in problema.espaco_estados if e['estado'] == self.estado)

        resultado:list[No] = []

        for acao in espaco_acoes['acoes']: # type: ignore
            filho = No(acao['destino'], acao['custo'] + heuristica.heu[acao["destino"]],
                        self, acao['destino'])
            
            resultado.append(filho)

        return resultado

    def constroi_solucao(self):
        no_atual = self
        solucao = [no_atual]

        while no_atual.pai != None:
            no_atual = no_atual.pai
            solucao.insert(0, no_atual)

        return solucao

class Problema:
    def __init__(self, espaco_estados:"list[dict[str, int]]", inicial:No, objetivo):
        self.espaco_estados = espaco_estados
        self.inicial = inicial
        self.objetivo = objetivo

BUSCA_INICIANDO = 0
BUSCA_FALHOU = 1
BUSCA_SUCESSO = 2
BUSCA_EM_CURSO = 3

class Astar:
    def __init__(self, problema:Problema):
        self.problema = problema
        self.fronteira = [problema.inicial]
        self.visitados = [problema.inicial.estado]
        self.solucao = []
        self.situacao = BUSCA_INICIANDO

    def executar(self):
        while self.situacao != BUSCA_FALHOU and self.situacao != BUSCA_SUCESSO:
            self.passo_busca()

        if self.situacao == BUSCA_FALHOU:
            print("Busca falhou")

        elif self.situacao == BUSCA_SUCESSO:
            print("Busca teve sucesso")
            print(f"Solucao: {self.solucao}")

        return

    def passo_busca(self):
        if (self.situacao == BUSCA_FALHOU):
            print("Busca falhou")
            return

        if (self.situacao == BUSCA_SUCESSO):
            print("Busca chegou ao objetivo com sucesso")
            return

        try:
            no = heappop(self.fronteira)

        except IndexError:
            self.situacao = BUSCA_FALHOU
            return

        #if self.problema.objetivo(no):
            #self.situacao = BUSCA_SUCESSO
            #self.solucao = no.constroi_solucao()

            return

        for filho in no.filhos(self.problema):
            if not (filho.estado in self.visitados):
                heappush(self.fronteira, filho)
                self.visitados.append(filho.estado)

        print(self.fronteira)

        return
    

no_arad = No('A', 0, None, None)

problema_romenia = Problema(estados.estados, no_arad,
                            lambda no: no.estado == 'A')

busca = Astar(problema_romenia)
busca.executar()
