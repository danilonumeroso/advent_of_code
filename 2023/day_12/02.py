import re
import functools

@functools.cache
def compute_num_valid_arrangements(springs, group):  
    if not group:
        return 1 if '#' not in springs else 0

    if len(springs) < sum(group):
        return 0

    if springs[0] == '.': 
        return compute_num_valid_arrangements(springs[1:], group)

    n_1 = (
        compute_num_valid_arrangements(springs[(group[0] + 1):], group[1:])
        if '.' not in springs[:group[0]] and (
            len(springs) > group[0] and 
            springs[group[0]] != '#' or 
            len(springs) <= group[0]
        )
        else 0
    )
    n_2 = compute_num_valid_arrangements(springs[1:], group) if springs[0] == '?' else 0
    
    return n_1 + n_2

with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()][:1000]

groups = [tuple(map(int, line.split(' ')[1].split(','))) for line in lines]
springs = [line.split(' ')[0] for line in lines]

groups = list(map(lambda x: x*5, groups))
springs = list(map(lambda x: x[:-1], map(lambda x: (x+'?')*5, springs)))

num_assignment = 0
for g, s in zip(groups, springs):
    num_assignment += compute_num_valid_arrangements(s, g)

print(num_assignment)
