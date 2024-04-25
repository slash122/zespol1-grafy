import networkx as nx
from random import randrange
from utils.representations import from_adj_matrix_to_adj_list
from utils.graphseq import degree_seq, rand_graph_edges
# from draw import draw_with_circle
from utils.cohesive import components
import random


# tworzy losowy graf eulerowski
# jako parametr przyjmuje liczbe wierzchoklow grafu
def generate_Euler_graph(n):
    seq = [randrange(2,n+1,2) for _ in range(n)]
    while not degree_seq(seq):
        seq = [randrange(2, n + 1, 2) for _ in range(n)]

    # print(seq)

    G = rand_graph_edges(seq,100)
    # draw_with_circle(G)

    # tworzymy macierz sąsiedztwa na potrzeby algorytmu znajdowania cyklu Eulera
    adj_matrix = nx.adjacency_matrix(G).todense()
    # for row in adj_matrix:
    #     print(row)

    return adj_matrix
    # euler_path(adj_matrix)



# algorytm znajdujacy ścieżkę Eulera
def euler_path(G):
    # algorytm przyjmuje że zaczynamy scieżkę od wierzchołka 1
    path = [1]

    k=0
    for i in range(len(G)):
        for j in range(i,len(G[i])):
            if G[i][j]==1:
                k+=1
    #długość ścieżki zawsze wynosi k krawędzi + 1
    k+=1
    i = 0
    j = 1
    # pomocnicze zmienne przechowujace informacje o mostach
    bridges = []
    bridges_passed = 0

    # algorytm działa dopóki długość scieżki nie będzie odpowiednia
    while len(path) < k:

        # print(path)
        if G[i][j] == 1:
            G[i][j] = 0
            G[j][i] = 0
            adj_list = from_adj_matrix_to_adj_list(G)
            #sprawdzamy czy usunięta krawędź jest mostem oraz czy nie mamy innej możliwości
            #niż przejść przez most
            if len(components(adj_list)) - bridges_passed > 1:
                # print("Bridge")
                if (i,j) not in bridges:
                    bridges.append((i, j))
                    # sprawdzamy czy wierzchołem ma jeszce jakichś sąsiadów do których możemy pójść
                    if len(adj_list[i]) != 0:
                        G[i][j] = 1
                        G[j][i] = 1
                        j += 1
                        if j == len(G):
                            j = 0
                        continue
                #sprawdzamy czy poprzez usuniecie krawedzi powstal wierzcholek izolowany
                #jesli jest izolowany lub dlugosc sciezki jest mniejsza od maksymalnej to wracamy i wybieramy inną scieżke
                if sum(G[j]) == 0 and len(path) < k-1:
                    G[i][j] = 1
                    G[j][i] = 1
                    j += 1
                    if j == len(G):
                        j = 0
                    continue
                # print("Bridge passed")
                path.append(j + 1)
                i = j
                bridges_passed += 1
                if j == len(G):
                    j = 0
                    continue
                continue
            path.append(j+1)
            i = j
        else:
            j+=1
        if j == len(G):
            j=0

    # print(path)
    return path
    #  


def fixed_random_euler(num_nodes):
    
    def connected_to_all_odd(G, node):    
        _odd_degree_nodes = [node for node, degree in G.degree() if degree % 2 == 1]
        for i in _odd_degree_nodes:
            if not G.has_edge(node, i) and not node == i:
                return False
        return True

    def get_unconnected_even(G, node):
        _even_degree_nodes = [node for node, degree in G.degree() if degree % 2 == 0]
        for i in _even_degree_nodes:
            if not G.has_edge(node, i):
                return i
        return None #Faktycznie funkcja nigdy nie zwroci None

    # Tworzymy losowy graf
    # Hack
    G = nx.random_tree(num_nodes)
    
    # Lista wierzchołków o nieparzystym stopniu
    # odd_degree_nodes = [node for node, degree in G.degree() if degree % 2 == 1]
    # even_degree_nodes = [node for node, degree in G.degree() if degree % 2 == 0]
    odd_degree_nodes = [node for node, degree in G.degree() if degree % 2 == 1]
    
    it = 0
    # Dopóki mamy wierzchołki o nieparzystym stopniu, dodajemy między nimi krawędzie
    while len(odd_degree_nodes) > 0:
        # Wybieramy losowo dwa wierzchołki o nieparzystym stopniu
        
        node1, node2 = random.sample(odd_degree_nodes, 2)
        
        if (connected_to_all_odd(G, node1)):
            node2 = get_unconnected_even(G, node1)

        # Dodajemy krawędź między wybranymi wierzchołkami
        G.add_edge(node1, node2)
        
        # Aktualizujemy listę wierzchołków o nieparzystym stopniu
        it += 1
        
        odd_degree_nodes = [node for node, degree in G.degree() if degree % 2 == 1]
        
        if it > 200:
            raise Exception("Too many iterations")
    
    return G


def fixed_euler_path(G):
    odd_degree_nodes = [node for node, degree in G.degree() if degree % 2 == 1]
    if len(odd_degree_nodes) > 2:
        return None

    start_node = odd_degree_nodes[0] if odd_degree_nodes else list(G.nodes)[0]

    stack, circuit = [start_node], []

    while stack:
        current_node = stack[-1]
        
        if G.degree(current_node) > 0:
            stack.append(list(G.neighbors(current_node))[0])
            G.remove_edge(current_node, stack[-1])
        
        else:
            circuit.append(stack.pop())

    return circuit[::-1]