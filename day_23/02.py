from heapq import heappush, heappop
from collections import defaultdict

UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

DIRECTIONS = [UP, DOWN, RIGHT, LEFT]

def sum_t(t1, t2):
    return tuple(map(lambda x, y: x + y, t1, t2))

def get_allowed_directions(grid, pos):
    allowed = []
    for direction in DIRECTIONS:
        new_pos = sum_t(pos, direction)
        if grid[new_pos[0]][new_pos[1]] != '#' and not is_out_of_bounds(grid, new_pos):
            allowed.append(direction)

    return allowed


def is_out_of_bounds(grid, coord):
    return coord[0] < 0 or coord[0] >= len(grid) \
        or coord[1] < 0 or coord[1] >= len(grid[0])


def find_path(grid, intersections, start, end, first_move=None):
    frontier = []
    solutions = []

    if first_move is None:
        path_lengths = []
        for direction in get_allowed_directions(grid, start):
            neighbour = sum_t(start, direction)

            path_lengths.append(find_path(grid, intersections, start, end, first_move=(1, neighbour, {start, neighbour})))

        return list(filter(lambda x: len(x) > 0, path_lengths))

    heappush(frontier, first_move)

    while len(frontier) > 0:
        step, pos, visited = heappop(frontier)

        if pos == end or pos in intersections:
            return start, pos, step

        allowed_directions = get_allowed_directions(grid, pos)

        for direction in allowed_directions:
            neighbour = sum_t(pos, direction)

            if neighbour in visited:
                continue

            visited.add(neighbour)
            heappush(frontier, (step + 1, neighbour, visited | {neighbour}))

    return solutions

def find_intersections(grid):
    intersections = []
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            num_dots = sum([grid[i - 1][j] == '.', grid[i + 1][j] == '.', 
                            grid[i][j - 1] == '.', grid[i][j + 1] == '.'])
            if grid[i][j] == '.' and num_dots > 2:
                intersections.append((i, j))
    return intersections

def find_edges(grid, source, end, intersections):
    edges = defaultdict(list)
    for s in [source] + intersections:
        for head, tail, cost in find_path(grid, intersections, s, end):
            edges[head].append((tail, cost))

    return edges


def find_max_path(edges, start, end):
    frontier = [(0, start, {start}, [start])]
    solutions = []
    while frontier:
        cost, pos, visited, path = frontier.pop()

        if pos == end:
            solutions.append((cost, path))

        for neighbour, path_cost in edges[pos]:
            if neighbour not in visited:
                frontier.append((cost + path_cost, neighbour, visited | {neighbour}, path + [neighbour]))

    return max(solutions, key=lambda x: x[0])

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        grid = [line.rstrip().replace('>', '.').replace('^', '.').replace('v', '.').replace('<', '.') for line in f.readlines()]

    source = (0, grid[0].find('.'))
    end = (len(grid) - 1, grid[-1].find('.'))

    edges = find_edges(grid, source, end, find_intersections([l for l in grid]))
    print(find_max_path(edges, source, end))