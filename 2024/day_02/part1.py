import csv
import re


def read_file(file_path):
    with open(file_path, "r") as file:
        return [l.strip() for l in file.readlines()]


def is_report_safe(report):
    """A report only counts as safe if both of the following are true:
    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.
    """
    assert len(report) > 2

    check_for_increasing = report[0] < report[1]

    for l1, l2 in zip(report, report[1:]):
        if (l1 < l2) != check_for_increasing:
            return False

        if abs(l1 - l2) > 3 or abs(l1 - l2) < 1:
            return False

    return True


def main(input_data):
    # 1. Trasform ["n1 n2 n3 ..."] -> ([n1], [n2], [n3], ...)
    reports = [list(map(int, re.split(r"\s+", line))) for line in input_data]

    # 2. Find the number of safe reports
    return sum(1 for report in reports if is_report_safe(report))


if __name__ == "__main__":
    file_path = "input.txt"
    lines = read_file(file_path)

    result = main(lines)
    print("Result:", result)
