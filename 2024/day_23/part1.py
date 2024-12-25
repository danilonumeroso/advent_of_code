import re
from collections import defaultdict


def read_file(file_path):
    with open(file_path, "r") as file:
        return [re.findall(r"(\w+)", line.strip()) for line in file.readlines()]


def main(connection_list):
    res = 0
    connections = defaultdict(list)

    for connection in connection_list:
        connections[connection[0]].append(connection[1])
        connections[connection[1]].append(connection[0])

    # Find cliques of size 3 in the graph described by the connections
    triples = set()
    for node in connections:
        if not node.startswith("t"):
            continue

        neighbors = connections[node]
        for neighbor1 in neighbors:
            for neighbor2 in connections[neighbor1]:
                if neighbor2 in connections[node]:
                    triples.add(frozenset({node, neighbor1, neighbor2}))

    return len(triples)


if __name__ == "__main__":
    file_path = "input.txt"
    inp = read_file(file_path)
    result = main(inp)
    print("Result:", result)
