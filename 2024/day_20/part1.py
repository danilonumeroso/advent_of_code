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


def get_neighbors(grid, pos):
    """Get valid neighbors of a position"""
    i, j = pos
    neighbors = []
    # if i > 0 and (grid[i - 1][j] != "#"):
    if i > 0:
        neighbors.append((i - 1, j))
    # if i < len(grid) - 1 and (grid[i + 1][j] != "#"):
    if i < len(grid) - 1:
        neighbors.append((i + 1, j))
    # if j > 0 and (grid[i][j - 1] != "#"):
    if j > 0:
        neighbors.append((i, j - 1))
    # if j < len(grid[0]) - 1 and (grid[i][j + 1] != "#"):
    if j < len(grid[0]) - 1:
        neighbors.append((i, j + 1))
    return neighbors


def get(set):
    try:
        return next(iter(set))
    except StopIteration:
        return None


def shortest_path(grid, start, end, enable_collisions=False):
    """Dijkstra's algorithm"""
    direction = (0, 1)
    queue = [(0, start)]
    visited = set()

    while queue:
        cost, current = heapq.heappop(queue)

        if grid[current[0]][current[1]] == "#":
            continue

        if current == end:
            return cost

        if (current) in visited:
            continue

        visited.add((current))

        neighbors = get_neighbors(grid, current)
        for neighbor in neighbors:

            heapq.heappush(
                queue,
                (
                    cost + 1,
                    neighbor,
                ),
            )

    raise ValueError("No path found")


def main(grid):
    best_cost = shortest_path(
        grid, start_pos(grid), end_pos(grid), enable_collisions=False
    )

    cheat_costs = []
    from tqdm import tqdm

    for i in tqdm(range(len(grid))):  # Bruteforce
        if i == 0 or i == len(grid) - 1:
            continue
        for j in range(len(grid[0])):
            if j == 0 or j == len(grid[0]) - 1:
                continue

            if grid[i][j] == "#":
                grid[i][j] = "."
                cheat_costs.append(
                    shortest_path(
                        grid, start_pos(grid), end_pos(grid), enable_collisions=False
                    )
                )
                grid[i][j] = "#"

    return sum(1 for cost in cheat_costs if cost <= best_cost - 100)


if __name__ == "__main__":
    file_path = "input.txt"
    inp = read_file(file_path)
    result = main(inp)
    print("Result:", result)
