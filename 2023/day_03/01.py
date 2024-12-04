import re 

def is_engine_part(lines, current_line, span):
    # Check if previous line contains any symbol except a dot '.' or a digit in the span
    if current_line - 1 >= 0:
        if re.search(r'[^\.0-9]', lines[current_line-1][max(span[0]-1, 0):span[1]+1]):
            return True
        
    # Check if next line contains any symbol except a dot '.' or a digit in the span
    if current_line + 1 <= len(lines) - 1:
        if re.search(r'[^\.0-9]', lines[current_line+1][max(span[0]-1, 0):span[1]+1]):
            return True
    # Check if current line contains any symbol except a dot '.' or a digit in the span
    if re.search(r'[^\.0-9]', lines[current_line][max(span[0]-1, 0):span[1]+1]):
        return True
    
    return False

with open('engine.txt') as f:
    lines = [line[:-1] for line in f.readlines()]

engine_parts = []
# For each line, extract the positions of the numbers
for i in range(len(lines)):
    start = len(engine_parts)
    # Extract the numbers
    numbers = re.finditer(r'\d+', lines[i])
    for number in numbers:
        if is_engine_part(lines, i, span=number.span()):
            engine_parts.append(number.group())

# Convert all numbers to int and sum them all
print(sum([int(number) for number in engine_parts]))