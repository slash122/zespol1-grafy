import networkx as nx

def prim_algorithm(graph):
    # Tworzymy nowy graf który będzie drzewem
    spanningTree = nx.Graph()

    # Wybieramy wierzchołek startowy (w tym wypadku o indeksie 0)
    first_node = list(graph.nodes())[0]

    # Lista wierzchołków, które zostały już dodane do drzewa
    added_nodes = [first_node]

    # Wykonujemy dopóki wszystkie wirzchołki nie zostały dodane do drzewa
    while len(added_nodes) < len(graph.nodes()):
        min_edge = None
        min_weight = float('inf')

        for u in added_nodes:
            for v in graph.neighbors(u):
                if v not in added_nodes:
                    # Jeśli waga krawędzi pomiędzy wierzchołkami jest mniejsza niż aktualna minimalna waga
                    if graph[u][v]['weight'] < min_weight:
                        min_edge = (u, v)
                        min_weight = graph[u][v]['weight']

        # Dodanie wierzchołka i krawędzi do drzewa
        spanningTree.add_edge(min_edge[0], min_edge[1], weight=min_weight)
        added_nodes.append(min_edge[1])

    return spanningTree