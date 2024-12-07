import re
from copy import deepcopy

from tqdm import tqdm


def read_file(file_path):
    with open(file_path, "r") as file:
        return [list(l.strip()) for l in file.readlines()]


def rotate_right(direction):
    # Rotate the direction 90 degrees clockwise
    x, y = direction
    return (y, -x)


def sum_tuples(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def is_out_of_bounds(grid, node):
    i, j = node
    return i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0])


def find_loops(grid, node):
    direction = (-1, 0)
    path = set()

    pos = node

    while True:
        path.add((pos, direction))
        if is_out_of_bounds(grid, sum_tuples(pos, direction)):
            return False

        if grid[pos[0] + direction[0]][pos[1] + direction[1]] == "#":
            direction = (direction[1], -direction[0])
        else:
            pos = sum_tuples(pos, direction)

        if (pos, direction) in path:
            return True

    return False


def get_start(grid, symbol):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == symbol:
                return (i, j)
    return None


def print_map(grid):
    print("\n".join(["".join(g) for g in grid]))


def main(grid):
    start = get_start(grid, "^")

    occlusions = set()

    for i in tqdm(range(len(grid))):
        for j in range(len(grid[0])):
            if (i, j) == start:
                continue
            if grid[i][j] == "#":
                continue

            grid_tmp = deepcopy(grid)
            grid_tmp[i][j] = "#"
            if find_loops(grid_tmp, start):
                occlusions.add((i, j))

    return len(occlusions)


if __name__ == "__main__":
    file_path = "input.txt"
    grid = read_file(file_path)
    result = main(grid)
    print("Result:", result)
