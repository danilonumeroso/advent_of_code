import os
import re
import time

from sympy import Eq, linsolve, symbols

WIDTH = 101
HEIGHT = 103
SECONDS = 100_000


def read_file(file_path):
    """p=0,4 v=3,-3
    p=6,3 v=-1,-3
    p=10,3 v=-1,2
    p=2,0 v=2,-1
    p=0,0 v=1,3
    p=3,0 v=-2,-2
    p=7,6 v=-1,-3
    p=3,0 v=-1,-2
    p=9,3 v=2,3
    p=7,3 v=-1,2
    p=2,4 v=2,-3
    p=9,5 v=-3,-3"""

    with open(file_path, "r") as file:
        lines = file.readlines()

    p, v = [], []

    for line in lines:
        p.append(list(map(int, re.findall(r"-?\d+", line)[:2])))
        v.append(list(map(int, re.findall(r"-?\d+", line)[2:])))

    return p, v


def quadrant(pos, width, height):
    w, h = width // 2, height // 2

    if pos[0] < w and pos[1] < h:
        return 1
    elif pos[0] > w and pos[1] < h:
        return 2
    elif pos[0] > w and pos[1] > h:
        return 3
    elif pos[0] < w and pos[1] > h:
        return 4

    return 0


def print_grid(pos, width, height, suffix):
    grid = [["." for _ in range(width)] for _ in range(height)]
    for x, y in pos:
        grid[y % height][x % width] = "#"

    open(f"grid_{suffix}.txt", "w").write("\n".join(["".join(row) for row in grid]))
    for row in grid:
        print("".join(row))


def update_one_second(pos, velocity):
    for p, v in zip(pos, velocity):
        x, y = p
        dx, dy = v

        x += dx
        y += dy

        p[0] = x
        p[1] = y

    return pos, velocity


def main(inp):
    pos, velocity = inp
    res = 1
    quadrants = [0, 0, 0, 0, 0]
    print(len(pos))
    for _ in range(SECONDS):
        print_grid(pos, WIDTH, HEIGHT, str(_))
        pos, velocity = update_one_second(pos, velocity)

    print_grid(pos, WIDTH, HEIGHT)

    return res


if __name__ == "__main__":
    # part 2 is a pile of ... prints. Do not run it.
    file_path = "input.txt"
    inp = read_file(file_path)
    result = main(inp)
    print("Result:", result)
