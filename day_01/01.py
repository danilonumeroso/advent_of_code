import re
import math

def find_first(iterable, condition):
    for i, j in enumerate(iterable):
        if condition(j):
            return j
    return -1

with open("input.txt", "r") as f:
    lines = f.readlines()

numbers = []
for line in lines:
    first = find_first(line, lambda x: x.isdigit())
    last = find_first(reversed(line), lambda x: x.isdigit())
    numbers.append(int(first + last))

print(sum(numbers))
