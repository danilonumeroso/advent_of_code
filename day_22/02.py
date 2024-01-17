from collections import defaultdict
from copy import deepcopy

# def find_first(bricks, cond_fn):
#     for brick in bricks:
#         if cond_fn(brick):
#             return brick
#     return None

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

# def count_non_supports(bricks):
#     ans = 0
#     for i, current_brick in enumerate(bricks):
#         above = list(filter(lambda b: b[0][-1] == current_brick[1][-1]+1 and intersects(b, current_brick), bricks[:i]))
#         # print(current_brick, above)
#         if len(above) == 0:
#             # print("Has nothing above, can be safely removed")
#             # input()
#             ans += 1
#             continue

#         same_z_axis = list(filter(lambda b: b[0][-1] == current_brick[0][-1] and b is not current_brick, bricks))
#         is_not_support = True
#         # print("Other candidates", same_z_axis)
#         for a in above:
#             if not any(intersects(a, b) for b in same_z_axis):
#                 # print(a, "has no support. Can't be safely removed")
#                 is_not_support = False
#                 break
            
#         if is_not_support:
#             ans += 1

#         # input()
#     return ans


# def fall(bricks):
#     for i, brick in enumerate(bricks):
#         start, _ = brick

#         if start[-1] == 1:
#             continue

#         support = find_first(reversed(bricks[:i]), lambda s: intersects(s, brick))
#         support = support if support else [[0,0,1], [0,0,1]]

#         _, support_end = support

#         fall_length = start[-1] - (support_end[-1] + 1)

#         brick[1][-1] -= fall_length
#         brick[0][-1] -= fall_length

#     return bricks

# def fall_2(bricks):

#     is_support = {}
#     for brick in bricks:
#         is_support[brick[0]] = False

#     for i, brick in enumerate(bricks):
#         idx, (start, _) = brick

#         if start[-1] == 1:
#             continue

#         support = find_first(reversed(bricks[:i]), lambda s: intersects(s[1], brick[1]))
#         if support:
#             support_2 = find_first(reversed(bricks[:i]), lambda s: intersects(s[1], brick[1]) and s[0] != support[0])
#             if not support_2 or support_2[1][1][-1] == support[1][1][-1]:
#                 is_support[support[0]] = True

#         support = support if support else [-1, [[0,0,1], [0,0,1]]]

#         _, support_end = support[1]

#         fall_length = start[-1] - (support_end[-1] + 1)

#         brick[1][1][-1] -= fall_length
#         brick[1][0][-1] -= fall_length

#     return bricks, is_support


def find_supports(bricks):
    supported_by = defaultdict(set)
    for i, (idx_b, current_brick) in enumerate(bricks):
        start, _ = current_brick
        supports = list(filter(lambda s: intersects(s[1], current_brick), reversed(bricks[:i])))
        
        z_end = supports[0][1][1][-1] if len(supports) > 0 else 0
        
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


