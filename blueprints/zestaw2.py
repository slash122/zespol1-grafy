from flask import Blueprint, render_template, request
from utils.parse import parse_array
from utils.plot import get_plot_as_img
from utils.zestaw2.graphseq import degree_seq, create_graph

import networkx as nx
import json

zestaw2 = Blueprint('zestaw2', __name__, template_folder='../templates/zestaw2')


@zestaw2.route('/')
def get_zestaw2():
    return render_template('zestaw2.html')


# Maciej Witkowski
@zestaw2.route('/graphicseq', methods=['POST'])
def graphic_seq():
    try:
        seq = request.form['graphSequence']
        seqArr = parse_array(seq)
        G = create_graph(seqArr)
        return json.dumps({"graphImage": get_plot_as_img(G)}), 200    
    except Exception as e:
        return json.dumps({"exceptionMsg": str(e)}), 400
        
            
