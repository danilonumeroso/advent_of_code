import re

def find_first(all_springs, key_fn):
    for i, s in enumerate(all_springs):
        if key_fn(s):
            return i, s

def check_dot(assignment, groups, i):
    # Regex matching all non dots characters
    past_groups = list(filter(lambda x: x.end() < i+1, re.finditer(r'#+', assignment)))
    possible_future_groups = list(filter(lambda x: x.start() > i, re.finditer(r'[^\.]+', assignment)))

    if len(possible_future_groups) + len(past_groups) < len(groups):
        return False
    
    for group_idx, s in enumerate(past_groups):
        if s.end() - s.start() != groups[group_idx]:
            return False
        
    return True


def check_hash(assignment, groups, i):
    contiguous_springs = list(re.finditer(r'[^\.]+', assignment))

    group_idx, current_springs = find_first(contiguous_springs, lambda s: s.start() <= i <= s.end())

    return group_idx < len(groups) and \
        ('?' in current_springs.group(0) and current_springs.end() - current_springs.start() >= groups[group_idx] or \
        '?' not in current_springs.group(0) and current_springs.end() - current_springs.start() == groups[group_idx])

def check_constraints(assignment, groups, i):

    constraints_fn = check_hash if assignment[i] == '#' else check_dot

    return constraints_fn(assignment, groups, i)

def backtrack(groups, assignment):
    """
        Backtrack to find the number of consistent assignments.
        Highly inefficient, but it works.
    """
    if '?' not in assignment:
        print(assignment)
        return 1

    num_consistent_assignments = 0
    i = assignment.index('?')

    for a in ['#', '.']:
        if check_constraints(assignment[:i] + a + assignment[i + 1:], groups, i):
            num_consistent_assignments += backtrack(groups, assignment[:i] + a + assignment[i + 1:])

    return num_consistent_assignments

with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()][1:2]

groups = [list(map(int, line.split(' ')[1].split(','))) for line in lines]
springs = [line.split(' ')[0] for line in lines]

num_assignment = 0
for g, s in zip(groups, springs):
    num_assignment += backtrack(g, s)

print(num_assignment)
