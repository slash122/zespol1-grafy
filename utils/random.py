import networkx as nx
from random import random
from random import randint
# Generacja randomowego grafu od Adama

def generate_random_graph(n, l):
    if isinstance(n, int) and isinstance(l, int):
        if l >= 0 and l <= (n * (n - 1)) / 2:
            available_pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
            inc_matrix = [[0] * l for _ in range(n)]
            for i in range(l):
                if not available_pairs:
                    raise Exception("Nie można utworzyć więcej krawędzi.")
                    break
                node_1, node_2 = available_pairs.pop(randint(0, len(available_pairs) - 1))
                inc_matrix[node_1][i] = 1
                inc_matrix[node_2][i] = 1
            return inc_matrix
        else:
            raise Exception("Liczba krawędzi musi wynosić (n*(n-1))/2")
    else:
        raise Exception("Niepoprawne dane (muszą to być liczby całkowite)")


def generate_probability_graph(n,p):
    if isinstance(n, int) and isinstance(p, float) or isinstance(p, int):
        if p >=0 and p<=1:
            nodes_index = [i for i in range(n)]
            used_node_index = []
            edge_list = []
            for i in nodes_index:
                for j in range(n):
                    if j != i and j not in used_node_index:
                        if random() <= p:
                            used_node_index.append(i)
                            edge_list.append((i,j))

            return edge_list
        else:
            raise Exception("Prawdopodobnieństwo musi wynosić od 0 do 1")
    else:
        raise Exception("Niepoprawne dane (muszą to być: liczba całkowita dla wierzchołków oraz liczba zmiennoprzecinkowa dla prawdopodobieństwa))")
