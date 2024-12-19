import heapq
import re
from functools import cache


def read_file(file_path):
    with open(file_path, "r") as file:
        return re.findall(r"\w+", file.readline()), re.findall(r"\w+", file.read())


@cache
def backtrack(towels, design, sol=""):
    if len(sol) > len(design):
        return 0

    if len(sol) == len(design):
        return 1 if sol == design else 0

    res = 0
    for towel in towels:
        if design.startswith(sol + towel):
            res += backtrack(towels, design, sol + towel)

    return res


def main(inp):
    res = 0
    towels, designs = inp

    for design in designs:
        res += backtrack(frozenset(towels), design)

    return res


if __name__ == "__main__":
    file_path = "input.txt"
    inp = read_file(file_path)
    result = main(inp)
    print("Result:", result)
