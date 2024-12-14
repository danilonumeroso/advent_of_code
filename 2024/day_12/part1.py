import re
from collections import defaultdict

from tqdm import tqdm


def read_file(file_path):
    with open(file_path, "r") as file:
        return [list(line.strip()) for line in file.readlines()]


def is_out_of_bounds(x, y, garden):
    return x < 0 or y < 0 or x >= len(garden) or y >= len(garden[0])


def find_regions(garden):
    regions = defaultdict(list)
    visited = set()

    def visit(plot, x, y, r):
        if is_out_of_bounds(x, y, garden):
            return r

        if (x, y) in visited:
            return r

        if garden[x][y] != plot:
            return r

        visited.add((x, y))
        r.append((x, y))

        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dx, dy = direction
            visit(plot, x + dx, y + dy, r)

        return r

    for x, row in enumerate(garden):
        for y, cell in enumerate(row):
            r = visit(cell, x, y, [])
            if len(r) > 0:
                regions[cell].append(r)

    return regions


def find_area(region):
    return len(region)


def find_perimeter(region, garden):
    perimeter = 0
    for x, y in region:
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dx, dy = direction
            if (
                is_out_of_bounds(x + dx, y + dy, garden)
                or garden[x + dx][y + dy] != garden[x][y]
            ):
                perimeter += 1
    return perimeter


def main(garden):
    res = 0

    regions = find_regions(garden)

    for plot, regions in regions.items():
        for region in regions:
            res += find_area(region) * find_perimeter(region, garden)

    return res


if __name__ == "__main__":
    file_path = "input.txt"
    garden = read_file(file_path)
    result = main(garden)
    print("Result:", result)
