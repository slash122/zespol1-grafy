import numpy as np
import networkx as nx
import random

def pagerank_to_string(pr_result):
    result = ''
    for node, pr in pr_result:
        result += str(node)  + ": " + str(pr) + "\n"
    return result


def pagerank_custom(graph, d=0.15, max_iters=10000, tolerance=1.0e-6):
    # Tworzenie macierzy sąsiedztwa A
    n = len(graph)
    nodes = list(graph.nodes())
    node_to_index = {node: idx for idx, node in enumerate(nodes)}
    A = np.zeros((n, n))

    # Tworzenie macierzy sąsiedztwa
    for edge in graph.edges():
        A[node_to_index[edge[0]], node_to_index[edge[1]]] = 1

    # Obliczanie stopni wyjściowych
    degrees = np.sum(A, axis=1)

    # Obliczanie macierzy stochastycznej P
    P = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if degrees[i] == 0:
                P[i, j] = 1 / n
            else:
                P[i, j] = (1 - d) * A[i, j] / degrees[i] + d / n

    # Iteracyjne obliczanie PageRank dla każdego wierzchołka osobno
    pagerank_dict = {}
    for i in range(n):
        p_prev = np.ones(n) / n
        for _ in range(max_iters):
            p = np.dot(p_prev, P)
            if np.linalg.norm(p - p_prev, ord=1) < tolerance:
                break
            p_prev = p
        pagerank_dict[nodes[i]] = p[i]

    # Sortowanie
    sorted_pagerank = sorted(pagerank_dict.items(), key=lambda x: x[1], reverse=True)

    return sorted_pagerank



def pagerank_random_walk(graph, d=0.15, N=10000):
    n = len(graph)
    nodes = list(graph.nodes())
    node_to_index = {node: idx for idx, node in enumerate(nodes)}

    # Inicjalizacja wektora odwiedzin
    visits = np.zeros(n)

    # Wybór losowego wierzchołka startowego
    current_node = random.choice(nodes)
    current_index = node_to_index[current_node]

    for _ in range(N):
        visits[current_index] += 1

        if random.random() < (1 - d):
            # Przechodzenie do sąsiedniego wierzchołka
            neighbors = list(graph.neighbors(current_node))
            if len(neighbors) > 0:
                next_node = random.choice(neighbors)
                current_node = next_node
                current_index = node_to_index[current_node]
        else:
            # Teleportacja do losowego wierzchołka
            current_node = random.choice(nodes)
            current_index = node_to_index[current_node]

    # Obliczanie PageRank jako częstość odwiedzin danego wierzchołka
    pagerank = {node: visits[node_to_index[node]] / N for node in nodes}

    # Sortowanie
    sorted_pagerank = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)

    return sorted_pagerank


# G = nx.DiGraph()
# edges = [
#     (1,6),
#     (1,5),
#     (1,9),
#     (2,1),
#     (2,3),
#     (2,6),
#     (3,2),
#     (3,4),
#     (3,5),
#     (3,12),
#     (4,3),
#     (4,5),
#     (4,8),
#     (4,9),
#     (4,11),
#     (5,3),
#     (5,7),
#     (5,8),
#     (5,9),
#     (6,2),
#     (6,7),
#     (7,5),
#     (7,6),
#     (7,8),
#     (8,4),
#     (8,5),
#     (8,9),
#     (8,12),
#     (9,4),
#     (9,5),
#     (9,8),
#     (9,10),
#     (10,9),
#     (11,4),
#     (11,9),
#     (12,1),
#     (12,8)
# ]
# G.add_edges_from(edges)

# sorted_pagerank_result = pagerank_custom(G, d=0.15)
# sorted_pagerank_random_result = pagerank_random_walk(G, d=0.15)
# print("PageRank - iteracja wektora obciazen:\n")
# for node, pr in sorted_pagerank_result:
#     print(f"PageRank dla wierzchołka {node}: {pr}")

# print("PageRank - bladzenie losowe:\n")
# for node, pr in sorted_pagerank_random_result:
#     print(f"PageRank dla wierzchołka {node}: {pr}")
