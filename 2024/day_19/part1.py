import heapq
import re


def read_file(file_path):
    with open(file_path, "r") as file:
        return re.findall(r"\w+", file.readline()), re.findall(r"\w+", file.read())


def backtrack(towels, design, sol=""):
    if len(sol) > len(design):
        return False

    if len(sol) == len(design):
        return sol == design

    for towel in towels:
        if design.startswith(sol + towel):
            if backtrack(towels, design, sol + towel):
                return True


def main(inp):
    res = 0
    towels, designs = inp

    for design in designs:
        if backtrack(towels, design):
            res += 1

    return res


if __name__ == "__main__":
    file_path = "input.txt"
    inp = read_file(file_path)
    result = main(inp)
    print("Result:", result)
