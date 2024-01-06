from heapq import heappush, heappop

UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

DIRECTIONS = [UP, DOWN, RIGHT, LEFT]


def inverse_direction(direction):
    return tuple(map(lambda x: -x, direction))


def sum_t(t1, t2):
    return tuple(map(lambda x, y: x + y, t1, t2))

def get_allowed_directions(last_direction, num_repetitions):

    if num_repetitions < 4:
        return [last_direction]
    
    allowed_directions = DIRECTIONS.copy()

    allowed_directions.remove(inverse_direction(last_direction))

    if num_repetitions == 10:
        allowed_directions.remove(last_direction)

    return allowed_directions


def is_out_of_bounds(grid, coord):
    return coord[0] < 0 or coord[0] >= len(grid) \
        or coord[1] < 0 or coord[1] >= len(grid[0])


def l1_distance(coord1, coord2):
    """
        This function computes the Manhattan distance between two coordinates.
        This will be used as a heuristic in the find_path function to speed up
        the search. The heuristic is admissible, meaning that it never
        overestimates the cost of reaching the target. This is a very well
        known strategy commonly used in pathfinding (A*).
    """
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def find_path(grid, start, end):
    """Dijkstra-like algorithm to find the shortest path from start to end"""
    frontier = []

    s_1, s_2 = sum_t(start, RIGHT), sum_t(start, DOWN)
    c_1, c_2 = grid[s_1[0]][s_1[1]], grid[s_2[0]][s_2[1]]

    heappush(frontier, (c_1 + l1_distance(s_1, end), c_1, s_1, RIGHT, 1))
    heappush(frontier, (c_2 + l1_distance(s_1, end), c_2, s_2, DOWN, 1))

    visited = set()

    while len(frontier) > 0:
        node = heappop(frontier)
        _, cost, coord, last_direction, num_repetitions = node
        if coord == end and num_repetitions == 4:
            return cost

        if (coord, last_direction, num_repetitions) in visited:
            continue

        visited.add((coord, last_direction, num_repetitions))
        allowed_directions = get_allowed_directions(last_direction,
                                                    num_repetitions)

        for direction in allowed_directions:
            if is_out_of_bounds(grid, (coord[0] + direction[0], 
                                       coord[1] + direction[1])):
                continue

            neighbour = (coord[0] + direction[0], coord[1] + direction[1])
            new_cost = cost + grid[neighbour[0]][neighbour[1]]
            heappush(
                frontier,
                (new_cost + l1_distance(neighbour, end),
                 new_cost, neighbour, direction,
                 1 if direction != last_direction else num_repetitions + 1))

    raise Exception("No path found")


with open('input.txt', 'r') as f:
    grid = [list(map(int, line.rstrip())) for line in f.readlines()]

print(find_path(grid, (0, 0), (len(grid) - 1, len(grid[0]) - 1)))
