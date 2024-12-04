import numpy as np
from collections import deque

def get_starting_position(map_):
    for i, line in enumerate(map_):
        if 'S' in line:
            return i, line.index('S')
        
    raise ValueError('No starting position found')

def bfs(map_, source, max_steps):
    num_rows, num_cols = len(map_), len(map_[0])
    queue = deque([(*source, max_steps, 0, 0)])
    visited = {(*source, 0, 0)}
    num_garden_plots = 0
    while queue:
        x, y, steps, row_wraps, col_wraps = queue.popleft()

        if steps % 2 == 0:
            num_garden_plots += 1

        if steps == 0:
            continue

        for x_next, y_next in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            num_map_v, i = divmod(x_next, num_rows)
            num_map_h, j = divmod(y_next, num_cols)
            num_map_v += row_wraps
            num_map_h += col_wraps

            if (
                lines[i][j] == "#"
                or (i, j, num_map_v, num_map_h) in visited
            ):
                continue

            queue.append((i, j, steps - 1, num_map_v, num_map_h))
            visited.add((i, j, num_map_v, num_map_h))

    return num_garden_plots


def print_coordinates(map_, coordinates):
    for x, y in coordinates:
        print(map_[x][y], end='')
    print()

if __name__ == "__main__":
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]

    # Get position of the 'S' symbol
    S = get_starting_position(lines)

    # print_coordinates(lines, [(S[0], i) for i in range(len(lines))])
    # print_coordinates(lines, [(i, S[0]) for i in range(len(lines))])

    """
        So, it turns out that for the test input, there are no walls ('#') in the same row and column 
        as the starting position (which is exactly the middle of the map). Furthemore, no walls are placed in 
        the path from the center of the map to the corners. This leads to two observations:
        - The area of the garden grows like a rhombus.
        - After len(lines) step in every direction, the elf is back to the middle of the map

        This means that the number of garden plots visited every 65 + n*size lines is a quadratic function
        *from the very beginning of the map*. With that being said, we can find the first three values of the
        function (f(65), f(65 + size), f(65 + 2*size)) and then find the coefficients of the quadratic
        function, like this:

        a = (f(65) - 2*f(65 + size) + f(65 + 2*size)) / 2
        b = (4*f(65 + size) - 3*f(65) - f(65 + 2*size)) / 2
        c = f(65)

        Then, we can just compute f(26501365 // size) and we're done.

        As you may have guessed, this solution only works if several assumptions hold (map is a square, few obstacles, etc.).
        Such assumptions don't even hold for the example input, so you can't even design your algorithm based on it, which is incredibly
        bad. Watch this video by HyperNeutrino for more details: https://www.youtube.com/watch?v=C5wYxR6ZAPM&t=6011s 
    """

    alpha = bfs(lines, S, max_steps=65)
    beta = bfs(lines, S, max_steps=65+len(lines))
    gamma = bfs(lines, S, max_steps=65+2*len(lines))

    a = (alpha - 2 * beta + gamma) / 2
    b = (4*beta - 3* alpha - gamma) / 2
    c = alpha

    f = lambda x: a*x**2 + b*x + c

    num_steps = 26_501_365

    print(f(num_steps//len(lines)))

