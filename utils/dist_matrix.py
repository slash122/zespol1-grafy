from utils.random_weighted import generate_random_weighted_graph
from utils.dijkstra import dijkstra

import numpy as np


def center(matrix):
    # zsumuj ścieżki
    sums = np.sum(matrix, axis=1)
    print(sums)
    # znajdź najmniejszą sumę/sumy
    indexes = np.where(sums == np.min(sums))[0]
    return indexes


def minmax(matrix):
    # znajdź najdłuższe ścieżki
    mm = np.max(matrix, axis=1)
    print(mm)
    # sprawdź które wierzchołki mają najkrótsze z najdłuższych ścieżek
    indexes = np.where(mm == np.min(mm))[0]
    return indexes


def dist_matrix(G):
    results = {}
    edge_weights = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    edge_weights.update({(v, u): d['weight']
                        for u, v, d in G.edges(data=True)})

    # dla każdego wierzchołka wykonaj algorytm dijkstry i znajdź odległości do pozostałych wierzchołków
    for node in G.nodes():
        _, results[node] = dijkstra(G, edge_weights, node-1)

    # zamień słownik słowników na macierz dwuwymiarową
    results = results.values()
    matrix = []
    for (index, row) in enumerate(results):
        matrix.append(list(row.values()))
    
    return matrix