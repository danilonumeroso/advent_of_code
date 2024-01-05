from collections import defaultdict

def is_rock(char):
    return char in ['O', '#']

def can_move_up(rock):
    assert is_rock(rock)
    return rock == 'O'


def roll(rock_positions):
    for col in rock_positions.keys():
        for i in range(len(rock_positions[col])):
            rock, _ = rock_positions[col][i]
            if can_move_up(rock):
                rock_positions[col][i][1] = 0 if i == 0 else rock_positions[col][i-1][1] + 1

    return rock_positions


def compute_score(rock_positions, max_rows):
    score = 0
    for col in rock_positions.keys():
        score += sum([max_rows-row for rock, row in rock_positions[col] if rock == 'O'])
    return score

with open('input.txt', 'r') as f:
    lines = [line.rstrip() for line in f.readlines()]

rock_positions = defaultdict(list)

for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if is_rock(char):
            rock_positions[col].append([char, row])

rock_positions = roll(rock_positions)
print(compute_score(rock_positions, len(lines)))