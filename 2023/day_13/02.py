def compute_hamming_distance(s1, s2):
    return sum([c1 != c2 for c1, c2 in zip(s1, s2)])

def find_possible_reflections(puzzle):
    possible_lines = []
    for i, (l1, l2) in enumerate(zip(puzzle, puzzle[1:])):
        if compute_hamming_distance(l1, l2) in [0, 1]:
            possible_lines.append((i, i+1, compute_hamming_distance(l1, l2) == 1))

    return possible_lines

def check_reflection(puzzle, start, end, exact):
    """
        Check if the reflection is valid. If exact is True, 
        it means that the smudge was found right in the line of reflection, hence 
        the remaining reflection must be perfect. Otherwise (exact is False), 
        we have to find a smudge in the reflection.
    """
    found_smudge = False
    for i, j in zip(range(start-1, -1, -1), range(end+1, len(puzzle))):
        found_smudge = found_smudge or compute_hamming_distance(puzzle[i], puzzle[j]) == 1
        if compute_hamming_distance(puzzle[i], puzzle[j]) > (0 if exact else 1):
            return False

    return found_smudge or exact


def find_horizontal_line(puzzle):
    possible_lines = find_possible_reflections(puzzle)
    for start, end, smudge in possible_lines:
        if check_reflection(puzzle, start, end, smudge):
            return start+1

    return -1
        
def find_vertical_line(puzzle):
    # Transpose a list of string
    puzzle = list(map("".join, map(list, zip(*puzzle))))
    return find_horizontal_line(puzzle)


def find_reflection(puzzle):
    n_rows = find_horizontal_line(puzzle)
    n_cols = find_vertical_line(puzzle)

    assert n_rows > 0 or n_cols > 0
    return n_rows * 100 if n_rows > 0 else n_cols

with open('input.txt', 'r') as f:
    lines = f.readlines()

puzzles = [p.split('\n') for p in "".join(lines).split("\n\n")]
print(sum([find_reflection(p) for p in puzzles]))