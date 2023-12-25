import networkx as nx
from math import prod

def read_input(file_path):
    with open(file_path) as f:
        return [line.strip().split(": ") for line in f]

def build_graph(data):
    G = nx.Graph()
    for v, adj in data:
        for a in adj.split(" "):
            G.add_edge(v, a)
    return G

input_file = "AoC_Day25_Input.txt"
data = read_input(input_file)
graph = build_graph(data)

graph.remove_edges_from(nx.minimum_edge_cut(graph))
connected_components_sizes = [len(c) for c in nx.connected_components(graph)]

result = nx.convert_node_labels_to_integers(graph)  # Przykładowa operacja na grafie

print("Part 1:", prod(connected_components_sizes))
