UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

MOVES = {
    "U": UP,
    "D": DOWN,
    "R": RIGHT,
    "L": LEFT
}

def compute_number_of_interior_points(boundary):
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
    
    return int(compute_shoelace_area(boundary) - len(boundary[:-1]) / 2 + 1)

def sum_t(t1, t2):
    return tuple(map(lambda x, y: x + y, t1, t2))

def dig(instructions):
    start = (0, 0)
    boundary = [start]
    
    for move, length in instructions:
        for _ in range(length):
            boundary.append(sum_t(boundary[-1], MOVES[move]))

    breakpoint()
    return compute_number_of_interior_points(boundary) + len(boundary) - 1


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
    
    instructions = [(line.split(' ')[0], int(line.split(' ')[1])) for line in lines]
    colors = [line.split(' ')[-1] for line in lines]
    print(dig(instructions))