from flask import Blueprint, render_template, request
from utils.representations import matrix_to_string
from utils.parse import parse_array, parse_matrix_any, inc_matrix_by_one, graph_from_string
from utils.plot import get_plot_as_img
from utils.graphseq import create_graph, rand_graph_edges
from utils.cohesive import components
from utils.euler import generate_Euler_graph, fixed_euler_path, fixed_random_euler
from utils.kregular import generate_regular_graph
from utils.hamilton import hamilton, fixed_hamilton

import networkx as nx
import json

zestaw2 = Blueprint('zestaw2', __name__, template_folder='../templates/zestaw2')


@zestaw2.route('/')
def get_zestaw2():
    return render_template('zestaw2.html')


@zestaw2.route('/graphicseq', methods=['POST'])
def graphic_seq():
    try:
        seq = request.form['graphSequence']
        seqArr = parse_array(seq)
        G = create_graph(seqArr)
        return json.dumps({"graphImage": get_plot_as_img(G)}), 200    
    except Exception as e:
        return json.dumps({"exceptionMsg": str(e)}), 400
    

@zestaw2.route('/randgraphicseq', methods=['POST'])
def rand_edges():
    try:
        seq = request.form['graphSequence']
        rand_val = int(request.form['randVal'])
        seqArr = parse_array(seq)
        G = rand_graph_edges(seqArr, rand_val)
        return json.dumps({"graphImage": get_plot_as_img(G)}), 200    
    except Exception as e:
        return json.dumps({"exceptionMsg": str(e)}), 400

    
@zestaw2.route('/cohesive', methods=['POST'])
def max_cohesive():
    try:
        adj_list = request.form['adjacencyList']
        adj_list = parse_matrix_any(adj_list)
        result = components(inc_matrix_by_one(adj_list))
        return json.dumps({"maxCohesive": result}), 200    
    except Exception as e:
        return json.dumps({"exceptionMsg": str(e)}), 400
    

@zestaw2.route('/euler', methods=['POST'])
def rand_euler():
    try:
        rand_num = request.form['eulerRandNum']
        # adj_matrix = generate_Euler_graph(int(rand_num))
        # matrix_str = matrix_to_string(adj_matrix)
        # G = graph_from_string(matrix_str, "adjmatrix")
        
        G = fixed_random_euler(int(rand_num))
        adj_matrix = nx.to_numpy_array(G).astype(int).tolist()
        
        Gc = G.copy()
        path = fixed_euler_path(Gc)
        # for i in range(len(path)):
        #     path[i] -= 1
        
        return json.dumps({"graphImage": get_plot_as_img(G), "adjMatrix": matrix_to_string(adj_matrix), "path": str(path)}), 200    
    except Exception as e:
        return json.dumps({"exceptionMsg": str(e)}), 400
    

@zestaw2.route('/randomkregular', methods=['POST'])
def rand_k_regular():
    try:
        param1 = int(request.form['param1'])
        param2 = int(request.form['param2'])
        G = generate_regular_graph(param1, param2)
        return json.dumps({"graphImage": get_plot_as_img(G)}), 200
    except Exception as e:
        return json.dumps({"exceptionMsg": str(e)}), 400


@zestaw2.route('/hamilton', methods=['POST'])
def rand_hamilton():
    try:
        rand_num = request.form['randNum']
        # adj_matrix = generate_Euler_graph(int(rand_num))
        # matrix_str = matrix_to_string(adj_matrix)
        # G = graph_from_string(matrix_str, "adjmatrix")
        G = fixed_random_euler(int(rand_num))
        path = fixed_hamilton(G)
        
        return json.dumps({"graphImage": get_plot_as_img(G), "path": str(path)}), 200    
    except Exception as e:
        return json.dumps({"exceptionMsg": str(e)}), 400
            
