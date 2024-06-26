import base64
import io
import matplotlib
matplotlib.use('agg') 
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def get_plot_as_img(G: nx.Graph):
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111)
    nx.draw_circular(G, ax=ax, with_labels=True, font_weight='bold')
    my_stringIObytes = io.BytesIO()
    plt.savefig(my_stringIObytes, dpi=360, format='png')
    my_stringIObytes.seek(0)
    img = base64.b64encode(my_stringIObytes.read()).decode()
    return img
    
    # with io.BytesIO() as buff:
    #     fig.savefig(buff, format='raw')
    #     buff.seek(0)
    #     data = np.frombuffer(buff.getvalue(), dtype=np.uint8)
    # w, h = fig.canvas.get_width_height()
    # im = data.reshape((int(h), int(w), -1))
    # return im.tolist()

   
def get_weighted_plot_as_img(G: nx.Graph):
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111)
    
    pos = nx.circular_layout(G)  # positions for all nodes
    nx.draw(G, pos, ax=ax, with_labels=True, font_weight='bold')

    # Add edge labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_weight='bold', font_size=17, ax=ax)
    
    my_stringIObytes = io.BytesIO()
    plt.savefig(my_stringIObytes, dpi=360, format='png')
    my_stringIObytes.seek(0)
    img = base64.b64encode(my_stringIObytes.read()).decode()
    return img