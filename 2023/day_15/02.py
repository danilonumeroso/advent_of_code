hash_map = [[] for _ in range(256)]

def find(sequence, cond_fn):
    for i, s in enumerate(sequence):
        if cond_fn(s):
            return i
    return -1

def add_or_replace(hash_map, label, focal_length):
    idx = compute_hash(label)

    elem_idx = find(hash_map[idx], lambda x: x[0] == label)
    
    if elem_idx == -1:
        hash_map[idx].append([label, focal_length])
        return
    
    hash_map[idx][elem_idx] = [label, focal_length]
    return

def remove(hash_map, label):
    idx = compute_hash(label)
    elem_idx = find(hash_map[idx], lambda x: x[0] == label)
    if elem_idx == -1:
        return
    hash_map[idx].pop(elem_idx)
    return


def compute_hash(string):
    curr_value = 0 
    for char in string:
        curr_value = (curr_value + ord(char)) * 17 % 256
    return curr_value

def split_lens(lens):
    if '-' in lens:
        label, op = lens[:-1], lens[-1]
        return label, op, None
    
    if '=' in lens:
        label, focal_length = lens.split('=')
        return label, '=', int(focal_length)


def compute_focusing_power(hash_map):
    power = 0
    for i, l in enumerate(hash_map):
        for j, (_, focal_length) in enumerate(l):
            power += (i+1) * (j+1) * focal_length

    return power

with open('input.txt', 'r') as f:
    line = f.readlines()[0].rstrip()

lenses = line.split(',')

for lens in lenses:
    label, op, focal_length = split_lens(lens)
    if op == '=':
        add_or_replace(hash_map, label, focal_length)
    elif op == '-':
        remove(hash_map, label)

print(compute_focusing_power(hash_map))
