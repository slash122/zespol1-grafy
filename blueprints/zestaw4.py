from flask import Blueprint, render_template, request
from utils.zest4.digraph import generate_digraph, kosaraju, get_subgraphs, bellman_ford
from utils.plot import get_weighted_plot_as_img

import networkx as nx
import json
import matplotlib.pyplot as plt
import numpy as np

zestaw4 = Blueprint('zestaw4', __name__, template_folder='../templates/zestaw4')

@zestaw4.route('/')
def get_zestaw4():
    return render_template('zestaw4.html')

@zestaw4.route('/randomdigraph', methods=['POST'])
def process_randdigraph():
    try:
        param1 = int(request.form['param1'])
        param2 = float(request.form['param2'])
        G = generate_digraph(param1, param2)
        components = kosaraju(G)

        if len(components) == 1:
            source_node = 0
            distances = bellman_ford(G, source_node)
            
            return json.dumps({"graphImage": get_weighted_plot_as_img(G), "components": str(components), "distances": str(distances)}), 200
        else:
            return json.dumps({"graphImage": get_weighted_plot_as_img(G), "components": str(components), "distances": None}), 200

    except Exception as e:
        if( str(e) == "Graf zawiera cykl o ujemnej sumie wag."):
            return json.dumps({"graphImage": get_weighted_plot_as_img(G), "components": components, "distances": "Graf zawiera cykl o ujemnej sumie wag."}), 200

        return json.dumps({"exceptionMsg": str(e)}), 400