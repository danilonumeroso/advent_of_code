# crappy code
import re
from collections import defaultdict

from tqdm import tqdm

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


def read_file(file_path):
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    grid = []
    grid_og = [list(line) for line in lines]
    for line in lines:
        line = "".join(map(lambda x: f"{x}{x}{x}", line))
        grid.append(list(line))
        grid.append(list(line))
        grid.append(list(line))

    return grid_og, grid


def print_grid(grid):
    for row in grid:
        print("".join(row))


def is_out_of_bounds(x, y, garden):
    return x < 0 or y < 0 or x >= len(garden) or y >= len(garden[0])


def get_neighbors(x, y, garden):
    neighbors = []
    for dx, dy in [
        (0, 1),
        (1, 0),
        (-1, 0),
        (0, -1),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]:
        neighbors.append(
            garden[x + dx][y + dy]
            if not is_out_of_bounds(x + dx, y + dy, garden)
            else None
        )

    return neighbors


def find_regions(garden, boundary_only=False):
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
        # if boundary_only:
        #     print(r)
        #     input()

        for direction in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            dx, dy = direction
            if boundary_only:
                neighbors = get_neighbors(x + dx, y + dy, garden)
                # check if all neighbors are the same as the current plot
                if all(n == plot for n in neighbors):
                    visited.add((x + dx, y + dy))
                    continue

            visit(plot, x + dx, y + dy, r)

        return r

    for x, row in enumerate(garden):
        for y, cell in enumerate(row):
            r = visit(cell, x, y, [])
            if len(r) > 0:
                regions[cell].append(r)
                regions[cell] = list(
                    reversed(sorted(regions[cell], key=lambda x: len(x)))
                )

    return regions


def find_area(region):
    return len(region)


def find_number_of_sides(region):
    turns = 0
    direction = RIGHT

    # print(region)
    region = region + [region[0]]
    for i in range(len(region) - 1):
        x1, y1 = region[i]
        x2, y2 = region[i + 1]

        # print(f"Checking {(x1, y1)} -> {(x2, y2)}")
        new_direction = (x2 - x1, y2 - y1)
        # print(f"Direction: {direction} -> {new_direction}")

        if new_direction != direction:
            # breakpoint()
            # print(
            # f"Turn detected : {(x1, y1)} -> {(x2, y2)}, {direction} -> {new_direction}"
            # )
            turns += 1
            # print(f"Turns: {turns}")

        direction = new_direction

    # breakpoint()
    return turns + 1


def find_boundary(region, garden):
    boundary = []
    for x, y in region:
        for dx, dy in [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1),
        ]:
            if (
                is_out_of_bounds(x + dx, y + dy, garden)
                or garden[x + dx][y + dy] != garden[x][y]
            ):
                boundary.append((x, y))
                break

    return boundary


def main(garden):
    res = 0
    garden_og, garden = garden
    print_grid(garden)
    regions_og = find_regions(garden_og)
    boundaries = find_regions(garden, boundary_only=True)
    for plot, regions in regions_og.items():
        boundary = boundaries[plot]

        # assert len(regions) == len(
        # boundary
        # ), f"{plot}: {len(regions)} != {len(boundary)}"
        # print(regions, boundary)
        # breakpoint()

        for region, b in zip(regions, boundary):
            # boundary = find_boundary(region, garden)
            # breakpoint()
            # print(region, boundary)
            # print(region, b)
            print(plot, find_area(region), find_number_of_sides(b))
            a, s = find_area(region), find_number_of_sides(b)
            res += a * s
            print(res)

    breakpoint()
    return res


if __name__ == "__main__":
    file_path = "input.txt"
    garden = read_file(file_path)
    result = main(garden)
    print("Result:", result)
