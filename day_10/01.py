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

with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]


print(len(find_main_loop(lines)) // 2)

