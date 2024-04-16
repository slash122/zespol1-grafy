from utils.sort import sort_dict_by_keys
import networkx as nx
import numpy as np


def matrix_to_string(matrix):
    return "\n".join([" ".join(map(str, row)) for row in matrix])


def adjlist_to_string(adjlist):
    return "\n".join([str(node) + " " + " ".join(map(str, adjlist[node])) for node in adjlist])


def get_graph_representations(G : nx.Graph):
    adjmatrix_string = matrix_to_string( nx.to_numpy_array(G).astype(int).tolist() )
    adjlist_string = adjlist_to_string( sort_dict_by_keys(nx.to_dict_of_lists(G)) )
    incmatrix_string = matrix_to_string( nx.incidence_matrix(G).todense().astype(int).tolist() )
    return {"adjmatrix": adjmatrix_string, "adjlist": adjlist_string, "incmatrix": incmatrix_string} 


def from_adj_matrix_to_adj_list(matrix):
    adj_list = []
    for row in matrix:
        list_row = []
        for j,el in enumerate(row):
            if el == 1:
                list_row.append(j+1)
        adj_list.append(list_row)
    return adj_list