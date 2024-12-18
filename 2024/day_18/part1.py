import heapq
import re


def read_file(file_path):
    """
    5,4
    4,2
    4,5
    3,0
    2,1
    6,3
    2,4
    """
    with open(file_path, "r") as file:
        return [tuple(map(int, re.findall(r"\d+", line))) for line in file.readlines()]


MAX_DIM = 71
SIMULATE_FIRST_N = 1024


def get_neighbors(pos, corrupted):
    """Get valid neighbors of a position"""
    i, j = pos
    neighbors = []
    if i > 0 and (i - 1, j) not in corrupted:
        neighbors.append((i - 1, j))
    if i < MAX_DIM - 1 and (i + 1, j) not in corrupted:
        neighbors.append((i + 1, j))
    if j > 0 and (i, j - 1) not in corrupted:
        neighbors.append((i, j - 1))
    if j < MAX_DIM - 1 and (i, j + 1) not in corrupted:
        neighbors.append((i, j + 1))

    return neighbors


def shortest_path(start, end, corrupted):
    """Dijkstra's algorithm"""
    direction = (0, 1)
    queue = [(0, start, [])]
    visited = set()
    costs = []
    while queue:
        cost, current, path = heapq.heappop(queue)
        if current == end:
            return cost

        if current in visited:
            continue

        visited.add(current)

        neighbors = get_neighbors(current, corrupted)
        for neighbor in neighbors:
            new_path = path + [current]
            heapq.heappush(queue, (cost + 1, neighbor, new_path))

    raise ValueError("No path found")


def main(inp):
    res = 0
    corrupted = set(inp[:SIMULATE_FIRST_N])

    res = shortest_path(
        start=(0, 0), end=(MAX_DIM - 1, MAX_DIM - 1), corrupted=corrupted
    )

    return res


if __name__ == "__main__":
    file_path = "input.txt"
    inp = read_file(file_path)
    result = main(inp)
    print("Result:", result)
