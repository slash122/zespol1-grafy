import networkx as nx
import numpy as np
# from draw import draw_with_circle
# from cohesive import create_graph, rand_graph_edges


# Sprawdza czy graf jest hamiltonowski.
# Za paramentr przyjmuje Graf w postaci nx
def hamilton(G):
    S = []
    visited = [False for _ in range(len(G))]
    # Przekrztałcamy graf na liste sąsiedztwa
    adj_list_dict = nx.to_dict_of_lists(G)
    adj_list = [neighbors for vertex, neighbors in adj_list_dict.items()]
    # print(adj_list)
    # Iterujemy po wszystkich wierzchołkach czyli sprawdzamy wszystkie możliwości
    for i in range(len(adj_list)):
        path = dfs(i,adj_list,visited,S)
        if path:
            path.append(path[0])
            break

    return path


def dfs(v,adj_list,visited,S):
    S.append(v+1)
    visited[v] = True
    # print(S)

    # Zmienna 'i' przyda nam się do sprawdzenia warunku czy przeslismy wszystkich sąsiadów
    for i,neighbor in enumerate(adj_list[v]):
        if len(S) == len(adj_list):
            # Warunek sprawdzający czy istnieje krawędź między pierwszym a ostatnim wierzchołkiem w stosie
            if S[0] in adj_list[v]:
                break
            # Jeśli nie to ściągamy wierzchołek
            else:
                visited[len(S)-1] = False
                S.pop(len(S)-1)
                break
        if not visited[neighbor-1]:
            dfs(neighbor-1,adj_list,visited,S)

        # Tu kolejny warunek czy osiągnęliśmy wszystkie wierzchołki ze względu na to że rekurencja jest 'w środku' kodu
        if len(S) == len(adj_list):
            break
        # Sprawdzamy czy przeszliśmy wszystkich sąsiadów którzy są odwiedzeni
        if i != len(adj_list[v])-1:
            continue
        # Jeśli doszliśmy przez wszystkich sąsiadów i są odwiedzeni to zdejmujemy wierzchołek ze stosu
        else:
            visited[len(S)-1] = False
            S.pop(len(S)-1)
            break

    return S



def fixed_hamilton(G):
    res = None
    
    for node in G.nodes:
        res = hamiltonian(G, node)
        if res:
            break
    
    return res


def hamiltonian(G, start_node):
    N = len(G.nodes)
    path = [start_node]

    def visit(node):
        if len(path) == N:
            return path

        for neighbor in G.neighbors(node):
            if neighbor not in path:
                path.append(neighbor)
                result = visit(neighbor)
                if result:
                    return result
                path.remove(neighbor)

        return None

    return visit(start_node)