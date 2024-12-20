import heapq


def read_file(file_path):
    with open(file_path, "r") as file:
        lines = [list(line.strip()) for line in file.readlines()]

    return lines


def start_pos(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "S":
                return i, j

    raise ValueError("No start position found")


def end_pos(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "E":
                return i, j

    raise ValueError("No end position found")


# def compute_manhattan_distance(a, b):
#     return abs(a[0] - b[0]) + abs(a[1] - b[1])


# def points_within_manhattan_distance(x, y, radius):
#     points = set()

#     for dx in range(-radius, radius + 1):
#         for dy in range(-radius, radius + 1):
#             if dx == 0 and dy == 0:
#                 continue

#             if abs(dx) + abs(dy) <= radius:
#                 points.add((x + dx, y + dy))

#     return points


# def get(set):
#     try:
#         return next(iter(set))
#     except StopIteration:
#         return None


# def shortest_path(grid, start, end, max_distance=1, best_known_cost=9999999):
#     """Dijkstra's algorithm"""
#     direction = (0, 1)
#     NO_CHEAT_NODE = (-1, -1)
#     queue = [(0, start, NO_CHEAT_NODE, NO_CHEAT_NODE)]
#     visited = set()
#     costs = []

#     IT = 0

#     while queue:
#         IT += 1
#         cost, current, cheat_from, cheat_to = heapq.heappop(queue)
#         if cost >= best_known_cost:
#             continue

#         if current == end:
#             costs.append(cost)
#             continue

#         if (current, cheat_from, cheat_to) in visited:
#             continue

#         visited.add((current, cheat_from, cheat_to))

#         neighbors = get_neighbors(
#             grid,
#             current,
#             max_distance=1 if cheat_from != NO_CHEAT_NODE else max_distance,
#         )

#         for neighbor in neighbors:
#             distance = compute_manhattan_distance(current, neighbor)
#             new_cheat_from = (
#                 cheat_from
#                 if cheat_from != NO_CHEAT_NODE
#                 else (current if distance > 1 else NO_CHEAT_NODE)
#             )

#             new_cheat_to = (
#                 cheat_to
#                 if cheat_to != NO_CHEAT_NODE
#                 else (neighbor if distance > 1 else NO_CHEAT_NODE)
#             )
#             heapq.heappush(
#                 queue,
#                 (
#                     cost + distance,
#                     neighbor,
#                     new_cheat_from,
#                     new_cheat_to,
#                 ),
#             )

#     print("IT", IT)
#     return costs
# raise ValueError("No path found")


def compute_distances_from_source(grid, source):
    end = end_pos(grid)

    rows, cols = len(grid), len(grid[0])

    distance_matrix = [[-1 for _ in range(cols)] for _ in range(rows)]
    distance_matrix[source[0]][source[1]] = 0

    x, y = source
    while (x, y) != end:
        for n_x, n_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if n_x < 0 or n_x >= rows or n_y < 0 or n_y >= cols:
                continue

            if grid[n_x][n_y] == "#":
                continue

            if distance_matrix[n_x][n_y] != -1:
                continue

            distance_matrix[n_x][n_y] = distance_matrix[x][y] + 1
            x, y = n_x, n_y

    return distance_matrix


def main(grid):
    res = 0
    rows, cols = len(grid), len(grid[0])

    dist = compute_distances_from_source(grid, start_pos(grid))

    MAX_RADIUS = 20

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == "#":
                continue
            for r in range(2, MAX_RADIUS + 1):
                for dx in range(r + 1):
                    dy = r - dx
                    for n_x, n_c in {
                        (x + dx, y + dy),
                        (x + dx, y - dy),
                        (x - dx, y + dy),
                        (x - dx, y - dy),
                    }:
                        if n_x < 0 or n_c < 0 or n_x >= rows or n_c >= cols:
                            continue
                        if grid[n_x][n_c] == "#":
                            continue
                        if dist[x][y] - dist[n_x][n_c] >= 100 + r:
                            res += 1

    return res


if __name__ == "__main__":
    file_path = "input.txt"
    inp = read_file(file_path)
    result = main(inp)
    print("Result:", result)
