import numpy as np

def get_starting_position(map_):
    for i, line in enumerate(map_):
        if 'S' in line:
            return i, line.index('S')
        
    raise ValueError('No starting position found')

def is_out_of_bounds(map_, pos):
    return pos[0] < 0 or pos[0] >= len(map_) or pos[1] < 0 or pos[1] >= len(map_[0])

def get_neighbours(map_, pos):

    neighbours = [
        (pos[0] - 1, pos[1]),
        (pos[0] + 1,pos[1]),
        (pos[0], pos[1] - 1),
        (pos[0], pos[1] + 1)
    ]

    return list(filter(lambda x: not is_out_of_bounds(map_, x) and map_[x[0]][x[1]] != '#', neighbours))

def flatten_idx(pos, map_):
    return pos[0] * len(map_[0]) + pos[1]

def bfs(map_, source, max_steps=64):
    visited = set()
    queue = [(source, 0)]

    num_garden_plots = 0
    while queue:
        node = queue.pop(0)
        
        if node in visited:
            continue

        visited.add(node)

        coords, steps = node

        if steps == max_steps:
            num_garden_plots += 1
            continue
        
        queue.extend([(v, steps+1) for v in get_neighbours(map_, coords)])

    return visited, num_garden_plots


if __name__ == "__main__":
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]

    # Get position of the 'S' symbol
    S = get_starting_position(lines)

    visited, num_garden_plots = bfs(lines, S, max_steps=67)
    print(num_garden_plots)



    