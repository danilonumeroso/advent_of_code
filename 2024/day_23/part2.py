import re

import networkx as nx


def read_file(file_path):
    with open(file_path, "r") as file:
        return [re.findall(r"(\w+)", line.strip()) for line in file.readlines()]


def main(connection_list):
    res = 0
    G = nx.Graph()
    G.add_edges_from(connection_list)
    cliques = list(nx.find_cliques(G))
    return ",".join(sorted(max(cliques, key=len)))


if __name__ == "__main__":
    file_path = "input.txt"
    inp = read_file(file_path)
    result = main(inp)
    print("Result:", result)
