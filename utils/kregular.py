import networkx as nx
import numpy as np
# from draw import draw_with_circle
from utils.graphseq import rand_graph_edges

def generate_regular_graph(n,k):

    if not n > k or (k%2 == 1 and not n%2 == 0):
        raise Exception("błędne dane wejściowe")

    seq = [k for _ in range(n)]
    print(type(seq))
    G = rand_graph_edges(seq,100)
    # draw_with_circle(G)

    return G