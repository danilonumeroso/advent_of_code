import re

from tqdm import tqdm

OPERATORS = ["+", "*", "||"]


def read_file(file_path):
    with open(file_path, "r") as file:
        content = file.readlines()

    targets = [int(l.split(":")[0]) for l in content]
    numbers = [list(map(int, l.split(":")[1].strip().split(" "))) for l in content]

    return targets, numbers


def evaluate_expression(xs, operators):
    res = xs[0]
    for i, x in enumerate(xs[1:]):
        if operators[i] == "+":
            res += x
        elif operators[i] == "*":
            res *= x
        elif operators[i] == "||":
            res = int(str(res) + str(x))
    return res


def backtrack(xs, target, operators=[]):

    if len(operators) == len(xs) - 1:
        return evaluate_expression(xs, operators) == target

    for op in OPERATORS:
        operators.append(op)
        if backtrack(xs, target, operators):
            return True
        operators.pop()

    return False


def main(results, numbers):
    res = 0
    for target, nums in tqdm(zip(results, numbers)):
        if backtrack(nums, target, []):
            res += target

    return res


if __name__ == "__main__":
    file_path = "input.txt"
    targets, numbers = read_file(file_path)
    result = main(targets, numbers)
    print("Result:", result)
