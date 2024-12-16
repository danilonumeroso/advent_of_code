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
    new_grid = []
    for x in range(len(grid)):
        new_grid.append([])
        for y in range(len(grid[0])):
            if grid[x][y] == "#":
                new_grid[-1].extend(["#", "#"])
            elif grid[x][y] == ".":
                new_grid[-1].extend([".", "."])
            elif grid[x][y] == "@":
                new_grid[-1].extend(["@", "."])
            elif grid[x][y] == "O":
                new_grid[-1].extend(["[", "]"])
    print_grid(new_grid, -1, -1)

    ops = "".join(ops.split("\n"))
    return new_grid, ops


def start_pos(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "@":
                return i, j

    raise ValueError("No start position found")


def find_clashing_boxes(grid, x, y, dx, dy, sym):
    pos = [
        (x + dx, y + dy, sym),
        (
            (x + dx + RIGHT[0], y + dy + RIGHT[1], "]")
            if sym == "["
            else (x + dx + LEFT[0], y + dy + LEFT[1], "[")
        ),
    ]

    queue = [pos[0], pos[1]]
    # clash_with_wall = False

    while queue:
        x, y, _ = queue.pop(0)

        if grid[x + dx][y + dy] == "#":
            # clash_with_wall = True
            return None, True

        if grid[x + dx][y + dy] == ".":
            continue

        if grid[x + dx][y + dy] in ["[", "]"]:
            start, end = (x + dx, y + dy, grid[x + dx][y + dy]), (
                (x + dx + RIGHT[0], y + dy + RIGHT[1], "]")
                if grid[x + dx][y + dy] == "["
                else (x + dx + LEFT[0], y + dy + LEFT[1], "[")
            )

            if start not in pos:
                pos.append(start)
                queue.append(start)

            if end not in pos:
                pos.append(end)
                queue.append(end)

    return pos, False


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

        if grid[x + dx][y + dy] in ["[", "]"]:
            pos, clash_with_wall = find_clashing_boxes(
                grid, x, y, dx, dy, grid[x + dx][y + dy]
            )
            if clash_with_wall:
                continue

            for o_x, o_y, sym in reversed(pos):
                grid[o_x + dx][o_y + dy] = sym
                grid[o_x][o_y] = "."

            # first_start = pos[0]
            # grid[first_start[0]][first_start[1]] = "."

        x += dx
        y += dy

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == "[":
                res += 100 * x + y

    return res


if __name__ == "__main__":
    file_path = "input.txt"
    inp = read_file(file_path)
    result = main(inp)
    print("Result:", result)
