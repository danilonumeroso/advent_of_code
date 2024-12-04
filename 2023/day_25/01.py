import re
import networkx as nx
from collections import defaultdict

def assert_bidirectional(adj_list):
    for node in adj_list:
        for neighbour in adj_list[node]:
            assert node in adj_list[neighbour]

def make_adj_list(lines):
    adj_list = defaultdict(list)

    for line in lines:
        node, *neighbours = re.findall('\w+', line)
        adj_list[node].extend(neighbours)

        for n in neighbours:
            adj_list[n].append(node)

    assert_bidirectional(adj_list)
    return adj_list


def cut_graph(adj_list):
    """This functions selects edges whose removal disconnects the graph in two components"""
    G = nx.Graph(adj_list)
    cuts = nx.minimum_edge_cut(G)
    G.remove_edges_from(cuts)
    return G

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]
                 
    adj_list = make_adj_list(lines)
    G = cut_graph(adj_list)
    S, T = list(nx.connected_components(G))
    print(len(S) * len(T))