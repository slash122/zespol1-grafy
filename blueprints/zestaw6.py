from flask import Blueprint, render_template, request
from utils.parse import digraph_from_adjlist
from utils.zest6.page_rank import pagerank_custom, pagerank_random_walk, pagerank_to_string
from utils.plot import get_weighted_plot_as_img
from utils.zest6.pr_cycles import plot_tsp_to_img, read_data, calculate_distance, solve_tsp

import networkx as nx
import json
import matplotlib.pyplot as plt
import numpy as np

zestaw6 = Blueprint('zestaw6', __name__, template_folder='../templates/zestaw6')

@zestaw6.route('/')
def get_zestaw6():
    return render_template('zestaw6.html')


@zestaw6.route('/pagerank', methods=['POST'])
def process_pagerank():
    try:
        graph_string = request.form['graphCode']
        G = digraph_from_adjlist(graph_string)
        pr_custom = pagerank_custom(G)
        pr_rw = pagerank_random_walk(G)
        return json.dumps({"prCustom": pagerank_to_string(pr_custom), "prRW": pagerank_to_string(pr_rw), "img": get_weighted_plot_as_img(G)}), 200
    except Exception as e:
        return json.dumps({"exceptionMsg": str(e)}), 400
    

@zestaw6.route('/shortest', methods=['GET'])
def process_shortest():
    try:
        file_path = 'utils/zest6/data.csv'
        max_iterations = 1000

        points = read_data(file_path)
        dist1 = calculate_distance(points)
        img1 = plot_tsp_to_img(points, "Dane początkowe")
        
        result, dist2 = solve_tsp(file_path, max_iterations)
        img2 = plot_tsp_to_img(result,"Najlepszy znaleziony cykl")
        
        return json.dumps({"img1": img1, "img2": img2, "dist1": dist1, "dist2": dist2}), 200
    except Exception as e:
        return json.dumps({"exceptionMsg": str(e)}), 400