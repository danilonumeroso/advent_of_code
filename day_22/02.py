from collections import defaultdict
from copy import deepcopy

def intersects(brick1, brick2):
    start_1, end_1 = brick1
    start_2, end_2 = brick2

    b1_x1, b1_y1, _ = start_1
    b1_x2, b1_y2, _ = end_1

    b2_x1, b2_y1, _ = start_2
    b2_x2, b2_y2, _ = end_2

    x1 = max(b1_x1, b2_x1)
    y1 = max(b1_y1, b2_y1)
    x2 = min(b1_x2, b2_x2)
    y2 = min(b1_y2, b2_y2)

    return x1 <= x2 and y1 <= y2


def find_supports(bricks):
    supported_by = defaultdict(set)
    for i, (idx_b, current_brick) in enumerate(bricks):
        start, _ = current_brick
        supports = list(filter(lambda s: intersects(s[1], current_brick), reversed(bricks[:i])))
        
        z_end = max(map(lambda x: x[1][1][-1], supports)) if len(supports) > 0 else 0
        
        fall_length = start[-1] - (z_end + 1)

        current_brick[1][-1] -= fall_length
        current_brick[0][-1] -= fall_length

        assert current_brick[0][-1] == z_end + 1

        if len(supports) == 0:
            supported_by[idx_b].add(-1)
            continue

        for idx_s, _ in filter(lambda s: s[1][1][-1] == z_end, supports):
            supported_by[idx_b].add(idx_s)
    return supported_by

def invert_dict(d):
    inv = defaultdict(set)
    for k, v in d.items():
        for value in v:
            inv[value].add(k)
    return inv

def count_falling_bricks(supports_dict, supported_by_dict, number_of_bricks):
    res = 0 
    for i in range(number_of_bricks):
        number_of_falling_bricks = 0
        brick_list = supports_dict[i]
        cond = True
        for v in brick_list:
            if len(supported_by_dict[v]) == 1:
                number_of_bricks += 1
        if cond:
            res += 1

    return res

def count_falling(supports_dict, supported_by_dict, brick):
    if len(supports_dict) == 0:
        return 0
    
    res = 0

    for v in supports_dict[brick]:
        supported_by_dict[v].remove(brick)
        if len(supported_by_dict[v]) == 0:
            res += 1 + count_falling(supports_dict, supported_by_dict, v)

    return res

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        bricks = [[line.rstrip().split('~')[0], 
                        line.rstrip().split('~')[1]] for line in f.readlines()]
        
    bricks = [(i, [list(map(int, start.split(','))), 
               list(map(int, end.split(',')))]) for i, (start, end) in enumerate(bricks)]

    bricks = sorted(bricks, key=lambda x: (x[1][0][-1], x[1][1][-1]))
    supported_by = find_supports(bricks)
    supports = invert_dict(supported_by)

    print(sum(count_falling(deepcopy(supports), deepcopy(supported_by), i) for i in range(len(bricks))))


