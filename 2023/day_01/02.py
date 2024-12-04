import re

def find_first(iterable, condition):
    for i, j in enumerate(iterable):
        if condition(j):
            return j
    return -1

with open("input.txt", "r") as f:
    lines = f.readlines()

new_lines = []
for x in lines:
    for string_number in [('one', 'o1e'), 
                          ('two', 't2e'), 
                          ('three', 't3e'), 
                          ('four', 'f4r'), 
                          ('five', 'f5e'), 
                          ('six', 's6x'), 
                          ('seven', 's7n'), 
                          ('eight', 'e8t'), 
                          ('nine', 'n9e')]:
        x = x.replace(string_number[0], string_number[1])

    new_lines.append(x)

numbers = []
for line in new_lines:
    first = find_first(line, lambda x: x.isdigit())
    last = find_first(reversed(line), lambda x: x.isdigit())
    numbers.append(int(first + last))

print(sum(numbers))
