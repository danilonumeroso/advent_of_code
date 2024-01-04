def find_possible_reflections(puzzle):
    """All reflections must start with adjacent equal lines"""
    possible_lines = []
    for i, (l1, l2) in enumerate(zip(puzzle, puzzle[1:])):
        if l1 == l2:
            possible_lines.append((i, i+1))

    return possible_lines

def check_reflection(puzzle, start, end):
    for i, j in zip(range(start, -1, -1), range(end, len(puzzle))):
        if puzzle[i] != puzzle[j]:
            return False
    return True


def find_horizontal_line(puzzle):
    possible_lines = find_possible_reflections(puzzle)
    for start, end in possible_lines:
        if check_reflection(puzzle, start, end):
            return start+1

    return -1
        
def find_vertical_line(puzzle):
    # Transpose a list of string
    puzzle = list(map("".join, map(list, zip(*puzzle))))
    return find_horizontal_line(puzzle)

def find_reflection(puzzle):
    n_rows = find_horizontal_line(puzzle)
    n_cols = find_vertical_line(puzzle)

    assert n_rows > 0 or n_cols > 0, "No reflection found"

    return n_rows * 100 if n_rows > 0 else n_cols

with open('input.txt', 'r') as f:
    lines = f.readlines()

puzzles = [p.split('\n') for p in "".join(lines).split("\n\n")]

print(sum([find_reflection(p) for p in puzzles]))