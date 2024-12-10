import re


def read_file(file_path):
    with open(file_path, "r") as file:
        lines = [list(map(int, list(l.strip()))) for l in file.readlines()]
    return lines


def get_trailheads(grid):
    trailheads = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 0:
                trailheads.append((i, j))
    return trailheads


def is_out_of_bounds(grid, pos):
    x, y = pos
    return x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0])


def compute_score(grid, trailhead):
    x, y = trailhead
    visited = set()

    stack = [(x, y, 0)]
    score = 0
    while stack:

        x, y, height = stack.pop()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if grid[x][y] == 9:
            score += 1
            continue

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if (
                not is_out_of_bounds(grid, (new_x, new_y))
                and grid[new_x][new_y] == height + 1
            ):
                stack.append((new_x, new_y, height + 1))

    return score


def main(grid):
    trailheads = get_trailheads(grid)
    scores = [compute_score(grid, trailhead) for trailhead in trailheads]
    return sum(scores)


if __name__ == "__main__":
    file_path = "input.txt"
    grid = read_file(file_path)
    result = main(grid)
    print("Result:", result)
