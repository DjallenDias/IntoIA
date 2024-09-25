from geopy.distance import geodesic

def distancia(cidade1, cidade2):
    return int(geodesic(cidade1, cidade2).km)