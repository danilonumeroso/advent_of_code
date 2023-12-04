import re 

def compute_gear_ratio(lines, current_line, span):
    if current_line - 1 < 0 or current_line + 1 > len(lines) - 1:
        return 0
    
    adj_numbers = []

    # Check all adjacent numbers in previous...
    for number in re.finditer(r'\d+', lines[current_line-1]):
        if span[0] in list(range(number.span()[0] - 1, number.span()[1] + 1)):
            adj_numbers.append(number.group())
            
    #... current...
    for number in re.finditer(r'\d+', lines[current_line]):
        if span[0] in list(range(number.span()[0] - 1, number.span()[1] + 1)):
            adj_numbers.append(number.group())

    #... and next line
    for number in re.finditer(r'\d+', lines[current_line+1]):
        if span[0] in list(range(number.span()[0] - 1, number.span()[1] + 1)):
            adj_numbers.append(number.group())
 
    if len(adj_numbers) != 2:
        return 0

    # Return gear ratios only if * is adjacent to exactly two numbers   
    return int(adj_numbers[0]) * int(adj_numbers[1])

with open('engine.txt') as f:
    lines = [line[:-1] for line in f.readlines()]

gear_ratios = []
# For each line, extract the positions of the numbers
for i in range(len(lines)):
    # Extract the numbers
    gears = re.finditer(r'\*', lines[i])
    for gear in gears:
        gear_ratios.append(compute_gear_ratio(lines, i, span=gear.span()))


print(sum(gear_ratios))
