from tail_recursion import tail_recursive, recurse

NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)

class PathException(Exception):
    pass

PIPE_TYPES = {
    "|": {
        NORTH: SOUTH,
        SOUTH: NORTH,
    },
    "-": {
        EAST: WEST,
        WEST: EAST,
    },
    "L": {
        NORTH: EAST,
        EAST: NORTH,
    },
    "J": {
        NORTH: WEST,
        WEST: NORTH,
    },
    "7": {
        SOUTH: WEST,
        WEST: SOUTH,
    },
    "F": {
        SOUTH: EAST,
        EAST: SOUTH,
    }
}

DIRECTIONS = [NORTH, SOUTH, EAST, WEST]

def is_viable(direction, dest_tile):
    if dest_tile == "S":
        return True

    if dest_tile not in PIPE_TYPES:
        return False

    return inverse_direction(direction) in PIPE_TYPES[dest_tile]

def get_starting_position(map_):
    dim = len(map_)
    for i in range(dim):
        for j in range(dim):
            if map_[i][j] == "S":
                return (i, j)

def inverse_direction(direction):
    return tuple(map(lambda x: -x, direction))

def find_main_loop(map_):
    """
        Find the main loop of the map, i.e. the path that goes from the starting 
        position to the starting position.
    """

    @tail_recursive
    def _find_main_loop(pos, last_direction, path=[]):
        i, j = pos
        current_tile = map_[i][j]
        
        if current_tile == "S" and len(path) > 0:
            return path + [pos]
        
        if current_tile == '.' or inverse_direction(last_direction) not in PIPE_TYPES[current_tile]:
            raise PathException("Path not found")

        d_i, d_j = PIPE_TYPES[current_tile][inverse_direction(last_direction)]
        next_tile = map_[i + d_i][j + d_j]
        if is_viable((d_i, d_j), next_tile):
            return recurse((i + d_i, j + d_j), 
                           (d_i, d_j),
                           path + [pos])

        raise PathException("Path not found")

    s_pos = get_starting_position(map_)

    for direction in DIRECTIONS:
        d_i, d_j = direction
        try: 
            return _find_main_loop((s_pos[0] + d_i, s_pos[1] + d_j), direction, path=[s_pos])
        except PathException:
            pass

    return "Ehm..., this shouldn't have happened."

def compute_number_of_interior_points(main_loop):
    """
        Use Pick's theorem to compute the number of interior points of the polygon defined by the main loop:
        i = A - b/2 + 1
            A: area of the polygon (computed with the shoelace formula)
            b: number of boundary points (length of the main loop)
            i: number of interior points (what we want to compute)
    """
    def compute_shoelace_area(boundary):
        # Use the shoelace formula to compute the area of the polygon defined by the main loop.
        n = len(boundary)
        return abs(sum([x2[0] * x1[1] - x2[1] * x1[0] for x1, x2 in zip(boundary, boundary[1:])])) / 2
    
    return int(compute_shoelace_area(main_loop) - len(main_loop[:-1]) / 2 + 1)

with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]


main_loop = find_main_loop(lines)
print(compute_number_of_interior_points(main_loop))