import re

from sympy import Eq, linsolve, symbols

WIDTH = 101
HEIGHT = 103
SECONDS = 100


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


def main(input):
    pos, velocity = input
    res = 1
    quadrants = [0, 0, 0, 0, 0]
    for p, v in zip(pos, velocity):
        x, y = p
        dx, dy = v

        x += dx * SECONDS
        y += dy * SECONDS

        q = quadrant((x % WIDTH, y % HEIGHT), WIDTH, HEIGHT)
        quadrants[q] += 1

    for q in quadrants[1:]:
        res *= q

    return res


if __name__ == "__main__":
    file_path = "input.txt"
    inp = read_file(file_path)
    result = main(inp)
    print("Result:", result)
