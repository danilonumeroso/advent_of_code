import re
import math
from tail_recursion import tail_recursive, recurse

"""
    Python is bad and doesn't optimise tail recursion, so we have to do it ourselves.
    Kudos @christpenner https://chrispenner.ca/posts/python-tail-recursion

    For performance reasons, in part two we just count the number of steps.
"""
@tail_recursive
def find_path_length(nodes, sequence, source, step=0):
    if source.endswith("Z"):
        return step

    left, right = nodes[source]
    use_left = sequence[step % len(sequence)] == "L"

    return recurse(nodes, sequence, left if use_left else right, step + 1)


with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

sequence = lines[0]
nodes = {}

for line in lines[1:]:
    if len(line) == 0:
        continue
    
    node, instructions = line.split('=')
    nodes[node.strip()] = tuple(re.findall(r'([A-Z]+)', instructions.strip()))

sources = list(filter(lambda x: x.endswith("A"), nodes.keys()))

print(math.lcm(*[find_path_length(nodes, sequence, s) for s in sources]))