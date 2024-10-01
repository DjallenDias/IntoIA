def acao(destino:str, custo:int):
    return {"destino": destino, "custo": custo}

cidades_acoes = [
    {"estado": "Arad", "acoes": [acao("Zerind", 75), acao("Sibiu", 140), acao("Timisoara", 118)]},
    {"estado": "Zerind", "acoes": [acao("Arad", 75), acao("Oradea", 71)]},
    {"estado": "Timisoara", "acoes": [acao("Arad", 118), acao("Lugoj", 111)]},
    {"estado": "Sibiu", "acoes": [acao("Arad", 140), acao("Fagaras", 99), acao("Râmnicu Vâlcea", 80)]},
    {"estado": "Oradea", "acoes": [acao("Zerind", 71), acao("Sibiu", 151)]},
    {"estado": "Lugoj", "acoes": [acao("Timisoara", 118), acao("Mehadia", 75)]},
    {"estado": "Mehadia", "acoes": [acao("Lugoj", 70), acao("Drobeta", 75)]},
    {"estado": "Drobeta", "acoes": [acao("Mehadia", 75), acao("Craiova", 120)]},
    {"estado": "Râmnicu Vâlcea", "acoes": [acao("Sibiu", 80), acao("Pitesti", 97), acao("Craiova", 146)]},
    {"estado": "Fagaras", "acoes": [acao("Sibiu", 99), acao("Bucharest", 211)]},
    {"estado": "Craiova", "acoes": [acao("Drobeta", 120), acao("Râmnicu Vâlcea", 146), acao("Pitesti", 138)]},
    {"estado": "Pitesti", "acoes": [acao("Craiova", 138), acao("Râmnicu Vâlcea", 97), acao("Bucharest", 101)]},
    {"estado": "Bucharest", "acoes": [acao("Fagaras", 211), acao("Pitesti", 101), acao("Giurgiu", 90), acao("Urziceni", 85)]},
    {"estado": "Giurgiu", "acoes": [acao("Bucharest", 90)]},
    {"estado": "Urziceni", "acoes": [acao("Bucharest", 85), acao("Hirsova", 98), acao("Vaslui", 142)]},
    {"estado": "Hirsova", "acoes": [acao("Urziceni", 98), acao("Eforie", 86)]},
    {"estado": "Vaslui", "acoes": [acao("Urziceni", 142), acao("Iasi", 92)]},
    {"estado": "Eforie", "acoes": [acao("Hirsova", 86)]},
    {"estado": "Iasi", "acoes": [acao("Vaslui", 92), acao("Neamt", 87)]},
    {"estado": "Neamt", "acoes": [acao("Iasi", 87)]},
]

cidades_coord = {
    'Arad': (46.1753793, 21.3196342),
    'Bucharest': (44.4361414, 26.1027202),
    'Craiova': (44.3190159, 23.7965614),
    'Drobeta': (44.6257835, 22.6531975),
    'Eforie': (44.0278741, 28.650451),
    'Fagaras': (45.8449433, 24.9703224),
    'Giurgiu': (44.12162085, 26.045927956436923),
    'Hirsova': (44.6845557, 27.9513766),
    'Iasi': (47.1615598, 27.5837814),
    'Lugoj': (45.6862542, 21.9063162),
    'Mehadia': (44.9043893, 22.3654341),
    'Neamt': (46.99100824999999, 26.513481254011523),
    'Oradea': (47.0549163, 21.9285231),
    'Pitesti': (44.8572343, 24.8719422),
    'Râmnicu Vâlcea': (45.1031731, 24.3647209),
    'Sibiu': (45.7973912, 24.1519202),
    'Timisoara': (45.7538355, 21.2257474),
    'Urziceni': (44.717002, 26.6324066),
    'Vaslui': (46.496847, 27.803675149742553),
    'Zerind': (46.6235188, 21.5169819)
}