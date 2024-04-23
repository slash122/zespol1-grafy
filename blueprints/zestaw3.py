from flask import Blueprint, render_template, request
from utils.random_weighted import generate_random_weighted_graph
from utils.plot import get_weighted_plot_as_img
from networkx.readwrite import json_graph
from utils.dijkstra import dijkstra
from utils.dist_matrix import dist_matrix, center, minmax
from utils.representations import matrix_to_string, adjlist_to_string
from utils.prim_kruskal import prim_algorithm

import networkx as nx
import json
import matplotlib.pyplot as plt
import numpy as np


# JSON Encoder for numpy types
class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)


zestaw3 = Blueprint('zestaw3', __name__, template_folder='../templates/zestaw3')


@zestaw3.route('/')
def get_zestaw3():
    return render_template('zestaw3.html')


@zestaw3.route('/process', methods=['GET'])
def process_zestaw3():
    try:
        G, weight_matrix = generate_random_weighted_graph()
        
        img = get_weighted_plot_as_img(G)

        matrix = dist_matrix(G)
        
        _center = center(matrix)
        _minmax = minmax(matrix)

        for i in range(0, len(_center)):
            _center[i] += 1

        for i in range(0, len(_minmax)):
            _minmax[i] += 1


        MST = prim_algorithm(G)
        mst_img = get_weighted_plot_as_img(MST)

        data = json_graph.node_link_data(G)
        serialized_graph = json.dumps(data, cls=NpEncoder)
        # serialized_matrix = json.dumps(matrix, cls=NpEncoder)

        return json.dumps({"graphImage": img, "serializedGraph": serialized_graph, "distMatrix": matrix_to_string(matrix), "center": str(_center), "minmax": str(_minmax), 
                           "mstImage": mst_img}), 200  
    except Exception as e:
        return json.dumps({"exceptionMsg": str(e)}), 400
    

@zestaw3.route('/dijkstra', methods=['POST'])
def process_dijkstra():
    try:
        serialized_graph = request.form['serializedGraph']
        vertex_idx = int(request.form['vertexIdx']) - 1

        data = json.loads(serialized_graph)
        G = json_graph.node_link_graph(data)
        
        # w = np.array(json.loads(serialized_weight_matrix))
        
        edge_weights = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
        edge_weights.update({(v, u): d['weight'] for u, v, d in G.edges(data=True)})
        
        paths, ds = dijkstra(G, edge_weights, vertex_idx)
        
        return json.dumps({"paths": paths}), 200
    except Exception as e:
        return json.dumps({"exceptionMsg": str(e)}), 400    
    