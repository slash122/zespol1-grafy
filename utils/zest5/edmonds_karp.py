# from random_network import generate_random_flow_network, draw_flow_network
import networkx as nx
from collections import deque
import matplotlib.pyplot as plt


def edmonds_karp(G, source, sink):
    # Utworzenie grafu rezydualnego R
    R = nx.DiGraph()
    for u, v in G.edges():
        R.add_edge(u, v, capacity=G[u][v]['capacity'], flow=0)
        R.add_edge(v, u, capacity=0, flow=0)

    max_flow = 0

    while True:
        # Wyszukiwanie ścieżki powiększającej w R
        path, capacity = bfs(R, source, sink)

        if path is None:
            break

        # Zwiększanie przepływu wzdłuż ścieżki
        for u, v in zip(path, path[1:]):
            R[u][v]['flow'] += capacity
            R[v][u]['flow'] -= capacity

        max_flow += capacity

    return max_flow


def bfs(G, source, sink):
    # Wyszukiwanie ścieżki powiększającej za pomocą BFS
    queue = deque([(source, [source], float('Inf'))])
    visited = set([source])

    while queue:
        u, path, min_capacity = queue.popleft()

        for v in G.neighbors(u):
            residual_capacity = G[u][v]['capacity'] - G[u][v]['flow']

            if residual_capacity > 0 and v not in visited:
                visited.add(v)
                next_path = path + [v]
                next_capacity = min(min_capacity, residual_capacity)

                if v == sink:
                    return next_path, next_capacity

                queue.append((v, next_path, next_capacity))

    return None, 0