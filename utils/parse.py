import networkx as nx
import numpy as np
import re


def parse_array(array_string: str):
    array = []
    for value in re.split(r",| ", array_string): #Zostawia "" więc trzeba to wykluczyć niżej
        if value == "":
            continue
        array.append(int(value)) 
    return array


# Dla macierzy sąsiedztwa lub incydencji
def parse_matrix(matrix_string: str):
    matrix = []

    for row in matrix_string.splitlines():
        parsed_row = []
        
        for value in re.split(r",| ", row): #Zostawia "" więc trzeba to wykluczyć niżej
            if value == "":
                continue
            if not value.isdigit() or (value != "0" and value != "1"):
                raise ValueError("Wrong value in matrix! Only 0 or 1 are allowed.")
            parsed_row.append(int(value))  
        
        matrix.append(parsed_row)
    
    return matrix


#Dla listy sąsiedztwa
def parse_adjacency_list(list_string: str): 
    adjacency_list = {}
    
    for line in list_string.splitlines():
        vertex, *adjacent_vertices = map(int, re.split(r",| ", line))
        adjacency_list[vertex] = adjacent_vertices
    
    return adjacency_list


# Z macierzy incydencji do macierzy sąsiedztwa
def incidence_to_adjacency(incedence_matrix):
    tmp = np.dot(incedence_matrix, incedence_matrix.T)
    for i in range(tmp.shape[0]):
        tmp[i][i] = 0
    return tmp


def graph_from_string(graph_string: str, graph_type: str):
    G: nx.Graph
    match graph_type:
        case "adjmatrix":
            matrix = parse_matrix(graph_string)
            G = nx.from_numpy_array(np.array(matrix))
        case "adjlist":
            adj_list = parse_adjacency_list(graph_string)
            G = nx.from_dict_of_lists(adj_list)
        case "incmatrix":
            matrix = parse_matrix(graph_string)
            np_matrix = incidence_to_adjacency(np.array(matrix))
            G = nx.from_numpy_array(np.array(np_matrix))
        case _:
            raise ValueError("Unexpected graph type!")
    
    return G


# Dla macierzy sąsiedztwa lub incydencji
def parse_matrix_any(matrix_string: str):
    matrix = []

    for row in matrix_string.splitlines():
        parsed_row = []
        
        for value in re.split(r",| ", row): #Zostawia "" więc trzeba to wykluczyć niżej
            if value == "":
                continue
            parsed_row.append(int(value))  
        
        matrix.append(parsed_row)
    
    return matrix



def inc_matrix_by_one(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += 1
    return matrix