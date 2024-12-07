grid = list(map(list, open("input.txt").read().splitlines()))

rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "^":
            break
    else:
        continue
    break


def loops(grid, r, c):
    dr = -1
    dc = 0

    seen = set()

    while True:
        seen.add((r, c, dr, dc))
        if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols:
            return False
        if grid[r + dr][c + dc] == "#":
            dc, dr = -dr, dc
        else:
            r += dr
            c += dc
        if (r, c, dr, dc) in seen:
            return True


def rotate_right(direction):
    # Rotate the direction 90 degrees clockwise
    x, y = direction
    return (y, -x)


def sum_tuples(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def is_out_of_bounds(grid, node):
    i, j = node
    return i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0])


def find_loops(grid, node):
    direction = (-1, 0)
    path = set()

    pos = node

    while True:
        path.add((pos, direction))
        if is_out_of_bounds(grid, sum_tuples(pos, direction)):
            return False

        if grid[pos[0] + direction[0]][pos[1] + direction[1]] == "#":
            direction = (direction[1], -direction[0])
        else:
            pos = sum_tuples(pos, direction)

        if (pos, direction) in path:
            return True

    return False


count = 0
from tqdm import tqdm

for cr in tqdm(range(rows)):
    for cc in range(cols):
        if grid[cr][cc] != ".":
            continue
        grid[cr][cc] = "#"
        if find_loops(grid, (r, c)):
            count += 1
        grid[cr][cc] = "."

print(count)
