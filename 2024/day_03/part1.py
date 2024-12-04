import csv
import re


def read_file(file_path):
    with open(file_path, "r") as file:
        return [l.strip() for l in file.readlines()]


def multiply_and_sum(lists):
    res = 0
    for l in lists:
        res += sum(x * y for x, y in l)
    return res


def main(input_data):
    # 1. Find all mul(X, Y) where X and Y are two numbers in the same line
    multiplications = [
        list(
            map(
                lambda x: (int(x[0]), int(x[1])),
                re.findall(r"mul\((\d+),(\d+)\)", line),
            )
        )
        for line in input_data
    ]
    return multiply_and_sum(multiplications)


if __name__ == "__main__":
    file_path = "input.txt"
    lines = read_file(file_path)

    result = main(lines)
    print("Result:", result)
