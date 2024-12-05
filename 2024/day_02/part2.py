import re


def read_file(file_path):
    with open(file_path, "r") as file:
        return [l.strip() for l in file.readlines()]


def is_report_safe(report):
    """A report only counts as safe if both of the following are true:
    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.

    Safety systems can now tolerate a single bad level in what would otherwise be a safe report.
    Same rules apply as before, except if removing a single level from an unsafe report would make it safe,
    the report instead counts as safe.
    """
    assert len(report) > 2

    check_for_increasing = report[0] < report[1]
    has_violation_occured = False

    for l1, l2 in zip(report, report[1:]):

        if (l1 < l2) != check_for_increasing:
            if has_violation_occured:
                return False
            has_violation_occured = True
            continue

        if abs(l1 - l2) > 3 or abs(l1 - l2) < 1:
            if has_violation_occured:
                return False
            has_violation_occured = True

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
