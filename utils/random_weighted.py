from random import randrange
from utils.graphseq import degree_seq, rand_graph_edges

import networkx as nx


def generate_random_weighted_graph():
    # Losujemy nasz ciąg liczb do momentu aż będzie ciągiem graficznym
    seq = [randrange(1, 8, 1) for _ in range(randrange(1, 12, 1))]
    while not (degree_seq(seq)):
        seq = [randrange(1, 8, 1) for _ in range(randrange(1, 12, 1))]

    print(seq)
    # Losujemy nasz graf i nadajemy mu losowe wagi krawędziom
    G = rand_graph_edges(seq,100)
    for u,v in G.edges():
        weight = randrange(1,10,1)
        G[u][v]['weight'] = weight

    weight_matrix = nx.adjacency_matrix(G, weight='weight').todense()
    return G, weight_matrix