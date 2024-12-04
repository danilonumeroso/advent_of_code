UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

TYPES = {
    "|": {
        UP: (UP,),
        DOWN: (DOWN,),
        LEFT: (UP, DOWN),
        RIGHT: (UP, DOWN),
    },
    "-": {
        RIGHT: (RIGHT,),
        LEFT: (LEFT,),
        UP: (RIGHT, LEFT),
        DOWN: (RIGHT, LEFT),
    },
    "\\": {
        DOWN: (RIGHT,),
        LEFT: (UP,),
        UP: (LEFT,),
        RIGHT: (DOWN,),
    },
    "/": {
        DOWN: (LEFT,),
        RIGHT: (UP,),
        UP: (RIGHT,),
        LEFT: (DOWN,),
    },
    '.': {
        UP: (UP,),
        DOWN: (DOWN,),
        LEFT: (LEFT,),
        RIGHT: (RIGHT,),
    },
}


def find_path(map):
    marked = set()

    queue = [(0, 0, RIGHT)]

    while len(queue) > 0:
        i, j, direction = queue.pop(0)
        if i < 0 or i >= len(map) or j < 0 or j >= len(map):
            continue

        if (i, j, direction) in marked:
            continue

        marked.add((i, j, direction))
        current_tile = map[i][j]
        
        for next_direction in TYPES[current_tile][direction]:
            d_i, d_j = next_direction
            queue.append((i + d_i, j + d_j, next_direction))

    marked = set([(i,j) for i, j, _ in marked])
        
    return marked


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]

    marked = find_path(lines)
    print(len(marked))
