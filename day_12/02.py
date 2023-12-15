import re
from tqdm import tqdm
from functools import cache

def check_constraints(assignment, groups, i):
    contiguous_springs = [(i, m) for i, m in enumerate(re.finditer(r'#+', assignment))]
    relevant_springs = list(filter(lambda x: i in range(x[1].start() - 1, x[1].end() + 1), contiguous_springs))

    if len(relevant_springs) == 0:

        possible_future_groups = [m.group(0) for m in re.finditer(r'(\?+|#+)+', assignment[i:])]
        number_of_definitive_groups = len(list(filter(lambda x: x.end() < i, map(lambda x: x[1], contiguous_springs))))
        breakpoint()

        if len(possible_future_groups) + number_of_definitive_groups < len(groups):
            return False
        
        iterator_pfg = reversed(map(len, possible_future_groups)) 
        for l_1, l_2 in zip(reversed(groups[1:]), iterator_pfg):
            if l_1 > l_2:
                return False
            
        return True
        

    for idx, springs in relevant_springs:
        if '?' in assignment[max(springs.start() - 1, 0): springs.end() + 1]:
            return True

        if idx >= len(groups) or groups[idx] != len(springs.group(0)):
            return False
    
    return True
    # breakpoint()
    

def backtrack(groups, assignment):
    """
        Backtrack to find the number of consistent assignments.
        Highly inefficient, but it works.
    """

    if '?' not in assignment:
        # print(groups, assignment)
        
        # # input()
        return 1

    num_consistent_assignments = 0
    i = assignment.index('?')

    for a in ['.', '#']:
        if check_constraints(assignment[:i] + a + assignment[i + 1:], groups, i):
            num_consistent_assignments += backtrack(groups, assignment[:i] + a + assignment[i + 1:])

    return num_consistent_assignments

with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()][:1000]

groups = [tuple(map(int, line.split(' ')[1].split(','))) for line in lines]
springs = [line.split(' ')[0] for line in lines]

# groups = list(map(lambda x: x*5, groups))
# springs = list(map(lambda x: x[:-1], map(lambda x: (x+'?')*5, springs)))

num_assignment = 0
for g, s in tqdm(zip(groups, springs)):
    num_assignment += backtrack(g, s)

print(num_assignment)
