import re


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


def visit_dfs(grid, node):

    stack = [node]
    visited = set()

    direction = (-1, 0)

    while stack:
        curr = stack.pop()
        visited.add(curr)

        nxt = sum_tuples(curr, direction)

        if is_out_of_bounds(grid, nxt):
            break

        if grid[nxt[0]][nxt[1]] == "#":
            direction = rotate_right(direction)
            nxt = sum_tuples(curr, direction)

        stack.append(nxt)

    return visited


def get_start(grid, symbol):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == symbol:
                return (i, j)
    return None


def main(grid):
    start = get_start(grid, "^")
    visited = visit_dfs(grid, start)
    return len(visited)


if __name__ == "__main__":
    file_path = "input.txt"
    grid = read_file(file_path)
    result = main(grid)
    print("Result:", result)
