import networkx as nx
import random
import matplotlib.pyplot as plt
import base64
import io


def generate_random_flow_network(N):
    if N < 2:
        raise Exception("Za mała liczba N")

    G = nx.DiGraph()

    # Dodajemy warstwy
    G.add_node('s', layer=0)
    source = [node for node, data in G.nodes(
        data=True) if data['layer'] == 0][0]

    for i in range(1, N+1):
        num_nodes = random.randint(2, N)
        for j in range(num_nodes):
            G.add_node((i, j), layer=i)

    G.add_node('t', layer=N+1)
    sink = [node for node, data in G.nodes(
        data=True) if data['layer'] == N+1][0]

    # Dodajemy łuki
    for i in range(0, N+1):
        layer_i_nodes = [node for node, data in G.nodes(
            data=True) if data['layer'] == i]
        layer_iplus_nodes = [node for node, data in G.nodes(
            data=True) if data['layer'] == i+1]

        lin = [i for i in range(len(layer_i_nodes))]
        lipn = [i for i in range(len(layer_iplus_nodes))]

        while lin:
            e1 = lin.pop(0)
            if lipn:
                e2 = random.choice(lipn)
                G.add_edge(
                    layer_i_nodes[e1], layer_iplus_nodes[e2], capacity=random.randint(1, 10))
                lipn.remove(e2)
            else:
                e2 = random.randint(0, len(layer_iplus_nodes)-1)
                G.add_edge(
                    layer_i_nodes[e1], layer_iplus_nodes[e2], capacity=random.randint(1, 10))

        for e2 in lipn:
            e1 = random.randint(0, len(layer_i_nodes)-1)
            G.add_edge(
                layer_i_nodes[e1], layer_iplus_nodes[e2], capacity=random.randint(1, 10))

    # Dodajemy dodatkowe łuki
    for _ in range(2*N):
        while True:
            source = random.choice(list(G.nodes()))
            target = random.choice(list(G.nodes()))
            if source != 't' and target != 's' and source != target and not G.has_edge(source, target) and not G.has_edge(target, source):
                capacity = random.randint(1, 10)
                G.add_edge(source, target, capacity=capacity)
                break

    return G


# def draw_flow_network(G):
#     pos = {}
#     layers = set(nx.get_node_attributes(G, 'layer').values())
#     for layer in layers:
#         layer_nodes = [node for node, data in G.nodes(
#             data=True) if data['layer'] == layer]
#         for i, node in enumerate(layer_nodes):
#             pos[node] = (layer, -i)

#     labels = nx.get_edge_attributes(G, 'capacity')
#     labels = nx.get_edge_attributes(G, 'capacity')
#     for edge, capacity in labels.items():
#         if '6' in str(capacity) or '9' in str(capacity):
#             labels[edge] = str(capacity) + '.'
#         else:
#             labels[edge] = str(capacity)
#     nx.draw(G, pos, with_labels=True, node_size=500,
#             node_color='skyblue', font_size=10)
#     nx.draw_networkx_edge_labels(
#         G, pos, edge_labels=labels, label_pos=0.75)
#     plt.show()


def get_flow_network_as_img(G):
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111)
    
    pos = {}
    layers = set(nx.get_node_attributes(G, 'layer').values())
    for layer in layers:
        layer_nodes = [node for node, data in G.nodes(
            data=True) if data['layer'] == layer]
        for i, node in enumerate(layer_nodes):
            pos[node] = (layer, -i)

    labels = nx.get_edge_attributes(G, 'capacity')
    labels = nx.get_edge_attributes(G, 'capacity')
    for edge, capacity in labels.items():
        if '6' in str(capacity) or '9' in str(capacity):
            labels[edge] = str(capacity) + '.'
        else:
            labels[edge] = str(capacity)
    nx.draw(G, pos, ax=ax, with_labels=True, node_size=1000,
            node_color='skyblue', font_size=17, arrowsize=17) 
    nx.draw_networkx_edge_labels(
        G, pos, ax=ax, edge_labels=labels, font_weight='bold', font_size=17, label_pos=0.75)
    
    my_stringIObytes = io.BytesIO()
    plt.savefig(my_stringIObytes, dpi=360, format='png')
    my_stringIObytes.seek(0)
    img = base64.b64encode(my_stringIObytes.read()).decode()
    return img


def get_network_circular_as_img(G: nx.Graph):
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111)
    
    pos = nx.circular_layout(G)  # positions for all nodes
    nx.draw(G, pos, ax=ax, with_labels=True, font_weight='bold')

    # Add edge labels
    edge_labels = nx.get_edge_attributes(G, "capacity")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_weight='bold', font_size=17, ax=ax)
    
    my_stringIObytes = io.BytesIO()
    plt.savefig(my_stringIObytes, dpi=360, format='png')
    my_stringIObytes.seek(0)
    img = base64.b64encode(my_stringIObytes.read()).decode()
    return img