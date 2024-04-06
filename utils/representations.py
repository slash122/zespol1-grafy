import networkx as nx
import numpy as np


def matrix_to_string(matrix):
    return "\n".join([" ".join(map(str, row)) for row in matrix])


def adjlist_to_string(adjlist):
    return "\n".join([str(node) + " " + " ".join(map(str, adjlist[node])) for node in adjlist])


def get_graph_representations(G : nx.Graph):
    adjmatrix_string = matrix_to_string(nx.to_numpy_array(G).astype(int).tolist())
    adjlist_string = adjlist_to_string(nx.to_dict_of_lists(G))
    incmatrix_string = matrix_to_string(nx.incidence_matrix(G).todense().astype(int).tolist())
    return {"adjmatrix": adjmatrix_string, "adjlist": adjlist_string, "incmatrix": incmatrix_string} 