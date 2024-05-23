import networkx as nx
import random
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
import math

def draw_digraph_with_weights(G):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    pos = nx.circular_layout(G)  # positions for all nodes
    nx.draw(G, pos, ax=ax, with_labels=True, font_weight='bold')

    # Add edge labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_weight='bold', font_size=17, ax=ax)

    # wyświetlenie grafu i okręgu
    plt.show()
    

def generate_digraph(n, p):
    G = nx.DiGraph()

    for i in range(n):
        G.add_node(i)

    for i in range(n):
        for j in range(n):
            if i != j:
                if random.random() < p:
                    G.add_edge(i, j, weight=20)
    return G

def kosaraju(G):
    def dfs_visit(G, u, visited, stack):
        visited.add(u)
        for v in G.neighbors(u):
            if v not in visited:
                dfs_visit(G, v, visited, stack)
        stack.append(u)

    def dfs_reverse(G, u, visited, component):
        visited.add(u)
        component.append(u)
        for v in G.neighbors(u):
            if v not in visited:
                dfs_reverse(G, v, visited, component)

    visited = set()
    stack = []
    for node in G.nodes():
        if node not in visited:
            dfs_visit(G, node, visited, stack)

    G_reverse = G.reverse()
    visited.clear()
    components = []
    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            dfs_reverse(G_reverse, node, visited, component)
            components.append(component)

    return components

def get_subgraphs(G, components):
    subgraphs = []
    for component in components:
        subgraph = G.subgraph(component).copy()
        subgraphs.append(subgraph)
    return subgraphs


def print_components(components):
    for i, component in enumerate(components):
        print(f"Silnie spójna składowa {i+1}:")
        print(component)


def assign_edge_weights(subgraph, lower_bound, upper_bound):
    for u, v in subgraph.edges():
        weight = random.randint(lower_bound, upper_bound)
        subgraph[u][v]['weight'] = weight
    return subgraph




def bellman_ford(graph, source):
    graph = assign_edge_weights(graph, -5, 10)

    distance = {node: float('inf') for node in graph.nodes()}
    distance[source] = 0

    # Relaksacja wszystkich krawędzi |V| - 1 razy.
    for _ in range(len(graph.nodes()) - 1):
        for u, v in graph.edges():
            if distance[u] + graph[u][v]['weight'] < distance[v]:
                distance[v] = distance[u] + graph[u][v]['weight']

    # Sprawdzenie obecności cykli o ujemnej sumie wag.
    for u, v in graph.edges():
        if distance[u] + graph[u][v]['weight'] < distance[v]:
            raise Exception("Graf zawiera cykl o ujemnej sumie wag.")
            return None

    return distance

# if __name__ == "__main__":
    
#     n = 4
#     p = 0.6
    
#     G = generate_digraph(n, p)
#     components = kosaraju(G)
#     print_components(components)
#     # subgraphs = get_subgraphs(G, components)
    
#     if len(components) == 1:
#         source_node = 0
#         distances = bellman_ford(G, source_node)
#         print("Najkrótsze odległości od źródła:")
#         print(distances)
    
#         draw_digraph_with_weights(G)