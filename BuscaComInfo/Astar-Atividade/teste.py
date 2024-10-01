from itertools import permutations

from estados import estados

# Presumindo que 'estados' e 'heuristica' já estejam importados

def custo_caminho(caminho):
    custo_total = 0
    for i in range(len(caminho) - 1):
        # Procurando a ação entre os estados adjacentes no caminho
        for acao in next(e for e in estados if e['estado'] == caminho[i])['acoes']:
            if acao['destino'] == caminho[i + 1]:
                custo_total += acao['custo']
                break
            
    return custo_total

def melhor_rota(estado_inicial):
    estados_permitidos = [estado['estado'] for estado in estados if estado['estado'] != estado_inicial]
    melhor_custo = float('inf')
    melhor_caminho = []

    # Gerar todas as permutações dos estados
    for perm in permutations(estados_permitidos):
        # Formar o caminho com o estado inicial no início e no fim
        caminho = [estado_inicial] + list(perm) + [estado_inicial]
        custo_atual = custo_caminho(caminho)
        
        if custo_atual < melhor_custo:
            melhor_custo = custo_atual
            melhor_caminho = caminho

    return melhor_caminho, melhor_custo

# Usando a função para encontrar a melhor rota a partir do estado A
caminho, custo = melhor_rota('A')
print(f"A melhor rota é: {caminho} com custo total: {custo}")
