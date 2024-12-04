import csv
import re

WORD = "MAS"
N = len(WORD)


def read_file(file_path):
    with open(file_path, "r") as file:
        return [l.strip() for l in file.readlines()]


def is_in_boundaries(x, y, n_rows, n_cols):
    return 0 <= x < n_rows and 0 <= y < n_cols


def find_word(map, x, y, direction, n_rows, n_cols):
    """
    Find the word in the map by following the direction.
    """
    current_word = [map[x][y]]
    for i in range(1, N):
        x = x + direction[0]
        y = y + direction[1]

        if not is_in_boundaries(x, y, n_rows, n_cols):
            return "".join(current_word)

        current_word.append(map[x][y])

    return current_word


def check_diagonal(map, x, y, n_rows, n_cols, direction):
    if not is_in_boundaries(x + direction[0], y + direction[1], n_rows, n_cols):
        return False

    if not is_in_boundaries(x - direction[0], y - direction[1], n_rows, n_cols):
        return False

    current_word = f"{map[x+direction[0]][y+direction[1]]}{map[x][y]}{map[x-direction[0]][y-direction[1]]}"
    return current_word == WORD or current_word[::-1] == WORD


def navigate_and_count(map, n_rows, n_cols):
    count_xmas = 0
    for x in range(n_rows):
        for y in range(n_cols):
            if map[x][y] != "A":
                continue

            if check_diagonal(map, x, y, n_rows, n_cols, (1, 1)) and check_diagonal(
                map, x, y, n_rows, n_cols, (1, -1)
            ):
                count_xmas += 1

    return count_xmas


def main(input_data):
    n_rows, n_cols = len(input_data), len(input_data[0])
    return navigate_and_count(input_data, n_rows, n_cols)


if __name__ == "__main__":
    file_path = "input.txt"
    lines = read_file(file_path)

    result = main(lines)
    print("Result:", result)
