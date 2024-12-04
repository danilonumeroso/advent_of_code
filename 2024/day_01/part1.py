import csv
import re


def read_file(file_path):
    with open(file_path, "r") as file:
        return [l.strip() for l in file.readlines()]


def find_total_distance(list_1, list_2):
    total_distance = 0
    for x1, x2 in zip(sorted(list_1), sorted(list_2)):
        total_distance += abs(x1 - x2)
    return total_distance


def main(input_data):
    # 1. Trasform ["1  2"] -> ([1], [2])
    lists = [list(map(int, re.split(r"\s+", line))) for line in input_data]

    # 2. Split the lists into the two columns
    col_1 = [l[0] for l in lists]
    col_2 = [l[1] for l in lists]

    # 3. Find the total distance
    return find_total_distance(col_1, col_2)


if __name__ == "__main__":
    file_path = "input.txt"
    lines = read_file(file_path)

    total_distance = main(lines)
    print("Total distance:", total_distance)
