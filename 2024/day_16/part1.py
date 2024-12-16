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
    if i > 0 and grid[i - 1][j] != "#":
        neighbors.append((i - 1, j))
    if i < len(grid) - 1 and grid[i + 1][j] != "#":
        neighbors.append((i + 1, j))
    if j > 0 and grid[i][j - 1] != "#":
        neighbors.append((i, j - 1))
    if j < len(grid[0]) - 1 and grid[i][j + 1] != "#":
        neighbors.append((i, j + 1))
    return neighbors


def shortest_path(grid, start, end):
    """Dijkstra's algorithm"""
    direction = (0, 1)
    queue = [(0, start, direction, [])]
    visited = set()

    costs = []
    while queue:
        cost, current, direction, path = heapq.heappop(queue)

        if current == end:
            return cost

        if current in visited:
            continue

        visited.add(current)

        neighbors = get_neighbors(grid, current)
        for neighbor in neighbors:
            new_direction = (neighbor[0] - current[0], neighbor[1] - current[1])
            if new_direction != direction:
                new_cost = cost + 1001
            else:  # Same direction
                new_cost = cost + 1

            new_path = path + [current]
            heapq.heappush(queue, (new_cost, neighbor, new_direction, new_path))

    raise ValueError("No path found")


def main(grid):
    return shortest_path(grid, start_pos(grid), end_pos(grid))


if __name__ == "__main__":
    file_path = "input.txt"
    inp = read_file(file_path)
    result = main(inp)
    print("Result:", result)
