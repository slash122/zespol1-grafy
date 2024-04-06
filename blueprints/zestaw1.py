from flask import Blueprint, render_template, url_for, request
from utils.parse import graph_from_string
from utils.representations import get_graph_representations, matrix_to_string
from utils.plot import get_plot_as_img
from utils.random import generate_random_graph, generate_probability_graph

import networkx as nx
import json

zestaw1 = Blueprint('zestaw1', __name__, template_folder='../templates/zestaw1')


@zestaw1.route('/')
def get_zestaw1():
    return render_template('zestaw1.html', word = "Hello World!")


@zestaw1.route('/process', methods=['POST'])
def process():
    try:
        code_type = request.form['graphCodeType']
        graph_string = request.form['graphCode']
        G = graph_from_string(graph_string, code_type)
        graph_representations = get_graph_representations(G)
        graph_image = get_plot_as_img(G)
        return json.dumps({"graphImage": graph_image, "graphRepresentations": graph_representations}), 200
    except Exception as e:
        return json.dumps({"exceptionMsg": str(e)}), 400
    

@zestaw1.route('/random', methods=['POST'])
def random_graph():
    random_type = request.form['randomType']
    param1 = int(request.form['param1'])
    param2 = request.form['param2']
    try:
        G: nx.Graph
        if random_type == "random":
            param2 = int(param2)
            inc_matrix = generate_random_graph(param1, param2)
            G = graph_from_string(matrix_to_string(inc_matrix), "incmatrix")
        elif random_type == "probability":
            param2 = float(param2)
            rg = generate_probability_graph(param1, param2)
            G = nx.Graph(rg)
        else:
            raise ValueError("Unknown random_type")
        
        graph_representations = get_graph_representations(G)
        graph_image = get_plot_as_img(G)
        return json.dumps({"graphImage": graph_image, "graphRepresentations": graph_representations}), 200
    except Exception as e:
        return json.dumps({"exceptionMsg": str(e)}), 400



