import re

def check_constraints(assignment, groups):
    if '?' in assignment:
        return True
    
    contiguous_springs = re.findall(r'#+', assignment)

    if len(contiguous_springs) != len(groups):
        return False
    
    for s_1, l_1 in zip(contiguous_springs, groups):
        if len(s_1) != l_1:
            return False
        
    return True

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

    for a in ['.', '#']:
        if check_constraints(assignment[:i] + a + assignment[i + 1:], groups):
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
