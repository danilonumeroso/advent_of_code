from collections import defaultdict
from copy import deepcopy
import tqdm

def find_first(rocks, key_fn):
    for s in rocks:
        if key_fn(s):
            return s

def is_rock(char):
    return char in ['O', '#']

def can_move(rock):
    assert is_rock(rock)
    return rock == 'O'

def invert(rock_positions):
    """Inverts the rock_positions dictionary, so that the keys are the rows and the values are the columns"""
    new_rock_positions = defaultdict(list)
    for col, pos in rock_positions.items():
        for rock, row in pos:
            new_rock_positions[row].append([rock, col])

    for row in new_rock_positions.keys():
       new_rock_positions[row].sort(key=lambda x: x[1])
    return new_rock_positions

def move_north(rock_positions):
    for col in rock_positions.keys():
        for i in range(len(rock_positions[col])):
            rock, _ = rock_positions[col][i]
            if can_move(rock):
                rock_positions[col][i][1] = 0 if i == 0 else rock_positions[col][i-1][1] + 1

    return rock_positions

def move_west(rock_positions):
    return invert(move_north(invert(rock_positions)))

def move_south(rock_positions, max_rows):
    for col in rock_positions.keys():
        for i in range(len(rock_positions[col])-1, -1, -1):
            rock, _ = rock_positions[col][i]
            if can_move(rock):
                rock_positions[col][i][1] = max_rows-1 if i == len(rock_positions[col]) - 1 else rock_positions[col][i+1][1] - 1
    return rock_positions

def move_east(rock_positions, max_cols):
    return invert(move_south(invert(rock_positions), max_cols))

def roll(rock_positions, max_rows, max_cols):
    """Simulates one iteration of the "rock rolling" (https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUJcmljayByb2xs)"""
    rock_positions = move_north(rock_positions)
    rock_positions = move_west(rock_positions)
    rock_positions = move_south(rock_positions, max_rows)
    rock_positions = move_east(rock_positions, max_cols)
    return rock_positions


def compute_score(rock_positions, max_rows):
    score = 0
    for col in rock_positions.keys():
        score += sum([max_rows-row for rock, row in rock_positions[col] if rock == 'O'])
    return score


with open('input.txt', 'r') as f:
    lines = [line.rstrip() for line in f.readlines()]

rock_positions = defaultdict(list)
"""
    Save the rock positions in a dictionary, where the keys are the columns and 
    the values are the rocks in that column
"""
for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if is_rock(char):
            rock_positions[col].append([char, row])


old_rock_positions = []
max_iter = 1000000000 
for i in range(max_iter):
    old_rock_positions.append(deepcopy(rock_positions))
    rock_positions = roll(rock_positions, max_rows=len(lines), max_cols=len(lines[0]))

    # Check if rock_positions is in old_rock_positions to detect cycles
    if rock_positions in old_rock_positions:
        break

# We found a cycle, so we can run the simulation only for the last few iterations
for _ in range((max_iter - i) % (i+1)):
    rock_positions = roll(rock_positions, max_rows=len(lines), max_cols=len(lines[0]))

print(compute_score(rock_positions, len(lines)))