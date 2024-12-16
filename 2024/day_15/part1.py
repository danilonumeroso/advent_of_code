import re

from sympy import Eq, linsolve, symbols

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

MOVES = {"^": UP, "v": DOWN, "<": LEFT, ">": RIGHT}


def read_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    grid, ops = content.split("\n\n")

    grid = list(map(list, grid.split("\n")))
    ops = "".join(ops.split("\n"))
    return grid, ops


def start_pos(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "@":
                return i, j

    raise ValueError("No start position found")


def find_contiguous_O(grid, x, y, dx, dy):
    pos = []
    while grid[x + dx][y + dy] == "O":
        x += dx
        y += dy
        pos.append((x, y))

    return pos


def print_grid(grid, x, y):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if i == x and j == y:
                print("@", end="")
            else:
                print(cell, end="")
        print()


def main(inp):
    grid, ops = inp
    res = 0

    x, y = start_pos(grid)
    grid[x][y] = "."
    for op in ops:
        dx, dy = MOVES[op]
        if grid[x + dx][y + dy] == "#":
            continue

        if grid[x + dx][y + dy] == "O":
            pos = find_contiguous_O(grid, x, y, dx, dy)
            last_x, last_y = pos[-1]

            if grid[last_x + dx][last_y + dy] == "#":
                continue

            first_x, first_y = pos[0]
            grid[first_x][first_y] = "."

            for o_x, o_y in pos:
                grid[o_x + dx][o_y + dy] = "O"

        x += dx
        y += dy

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == "O":
                res += 100 * x + y

    return res


if __name__ == "__main__":
    file_path = "input.txt"
    inp = read_file(file_path)
    result = main(inp)
    print("Result:", result)
