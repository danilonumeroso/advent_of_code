import re


def read_file(file_path):
    with open(file_path, "r") as file:
        content = [list(line.strip()) for line in file.readlines()]

    return content


def find_antennas(grid):
    antennas = {}
    num_rows, num_cols = len(grid), len(grid[0])
    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] != ".":
                if grid[i][j] not in antennas:
                    antennas[grid[i][j]] = []
                antennas[grid[i][j]].append((i, j))

    return antennas


def compute_combinations(a, b):
    comb = []

    for i in range(len(a)):
        for j in range(len(b)):
            if i < j:
                comb.append((a[i], b[j]))
    return comb


def is_out_of_bounds(pos, dim):
    x, y = pos
    return x < 0 or y < 0 or x >= dim or y >= dim


def compute_antinode(antenna, dim):
    antinodes = set()

    combs = compute_combinations(antenna, antenna)

    for a, b in combs:
        dx, dy = a[0] - b[0], a[1] - b[1]

        x1, y1 = a[0] + dx, a[1] + dy
        x2, y2 = b[0] - dx, b[1] - dy

        if not is_out_of_bounds((x1, y1), dim):
            antinodes.add((x1, y1))
        if not is_out_of_bounds((x2, y2), dim):
            antinodes.add((x2, y2))

    return antinodes


def print_grid(grid, antinodes=[]):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if (i, j) in antinodes:
                print("#", end="")
            else:
                print(cell, end="")
        print()


def main(grid):
    dim = len(grid)
    antennas = find_antennas(grid)
    antinodes = set()

    for a in antennas.keys():
        antinodes = antinodes.union(compute_antinode(antennas[a], dim))

    return len(antinodes)


if __name__ == "__main__":
    file_path = "input.txt"
    grid = read_file(file_path)
    result = main(grid)
    print("Result:", result)
