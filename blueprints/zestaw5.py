from flask import Blueprint, render_template, request
from utils.zest5.random_network import generate_random_flow_network, get_flow_network_as_img, get_network_circular_as_img
# from utils.plot import get_weighted_plot_as_img
from utils.zest5.edmonds_karp import edmonds_karp
import networkx as nx
import json
import matplotlib.pyplot as plt
import numpy as np


zestaw5 = Blueprint('zestaw5', __name__, template_folder='../templates/zestaw5')

@zestaw5.route('/')
def get_zestaw5():
    return render_template('zestaw5.html')

@zestaw5.route('/process', methods=['POST'])
def process_network():
    try:
        layer_num = int(request.form['layerNum'])
        G = generate_random_flow_network(layer_num)
        
        s = [node for node, data in G.nodes(
            data=True) if data['layer'] == 0][0]
        t = [node for node, data in G.nodes(
            data=True) if data['layer'] == layer_num+1][0]
        
        max_flow = edmonds_karp(G, s, t)
        
        return json.dumps({"layeredImg": get_flow_network_as_img(G), "circleImg": get_network_circular_as_img(G), 
                           "maxFlow": max_flow}), 200
    except Exception as e:
        return json.dumps({"exceptionMsg": str(e)}), 400
