import itertools

RANGE = (200000000000000, 400000000000000)

class SameLineError(Exception):
    pass

class NoIntersectionError(Exception):
    pass

def find_line_equation(p1, velocity):
    """Find the equation of the line passing through p1 and p2=p1 + velocity"""
    p2 = (p1[0] + velocity[0], p1[1] + velocity[1])

    x1, y1 = p1
    x2, y2 = p2
    
    m = (y2 - y1) / (x2 - x1)

    return m, y1 - m * x1

def find_intersection_point(eq1, eq2):
    """Find the intersection point of two lines"""

    if eq1 == eq2:
        raise SameLineError
    
    if eq1[0] == eq2[0]:
        raise NoIntersectionError

    m1, q1 = eq1
    m2, q2 = eq2

    x = (q2 - q1) / (m1 - m2)
    y = m1 * x + q1

    return x, y

def is_in_the_future(intersection, p1, v1):
    dx, dy = intersection[0] - p1[0], intersection[1] - p1[1]
    return (dx > 0) == (v1[0] > 0) and (dy > 0) == (v1[1] > 0)

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.rstrip().split('@') for line in f.readlines()]
    
    points = [tuple(map(int, line[0].strip().split(',')))[:2] for line in lines]
    velocity = [tuple(map(int, line[1].strip().split(',')))[:2] for line in lines]

    line_eqs = [[find_line_equation(p, v), p, v] for p, v in zip(points, velocity)]

    num_collisions = 0

    for (eq1, p1, v1), (eq2, p2, v2) in itertools.combinations(line_eqs, 2):
        try: 
            x, y = find_intersection_point(eq1, eq2)
            if RANGE[0] <= x <= RANGE[1] and RANGE[0] <= y <= RANGE[1]:
                # Collision detected, check if it will happen in the future or if it already happened
                if is_in_the_future((x, y), p1, v1) and is_in_the_future((x, y), p2, v2):
                    num_collisions += 1
        except SameLineError:
            print("same line detected")
            pass
        except NoIntersectionError:
            pass

    print(num_collisions)
