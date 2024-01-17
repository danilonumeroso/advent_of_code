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

def get_allowed_directions(grid, pos):
    # Check adjacent cells and returns those not being '#'

    if grid[pos[0]][pos[1]] == '>':
        return [RIGHT]
    
    if grid[pos[0]][pos[1]] == '<':
        return [LEFT]
    
    if grid[pos[0]][pos[1]] == '^':
        return [UP]
    
    if grid[pos[0]][pos[1]] == 'v':
        return [DOWN]
    

    allowed = []
    for direction in DIRECTIONS:
        new_pos = sum_t(pos, direction)
        if grid[new_pos[0]][new_pos[1]] != '#' and not is_out_of_bounds(grid, new_pos):
            allowed.append(direction)

    return allowed


def is_out_of_bounds(grid, coord):
    return coord[0] < 0 or coord[0] >= len(grid) \
        or coord[1] < 0 or coord[1] >= len(grid[0])


def find_path(grid, start, end):
    frontier = []

    s_1 = sum_t(start, DOWN)

    heappush(frontier, (1, s_1, {start, s_1}))
    solutions = []

    while len(frontier) > 0:
        step, pos, visited = heappop(frontier)

        if pos == end:
            solutions.append(step)
            continue

        allowed_directions = get_allowed_directions(grid, pos)

        for direction in allowed_directions:
            neighbour = sum_t(pos, direction)

            if neighbour in visited:
                continue

            visited.add(neighbour)
            heappush(frontier, (step + 1, neighbour, visited | {neighbour}))

    return solutions

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        grid = [line.rstrip() for line in f.readlines()]

    source = (0, grid[0].find('.'))
    end = (len(grid) - 1, grid[-1].find('.'))

    sols = find_path(grid, source, end)
    print(max(sols))