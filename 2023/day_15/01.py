def compute_hash(string):
    curr_value = 0 
    for char in string:
        curr_value = (curr_value + ord(char)) * 17 % 256
    return curr_value


with open('input.txt', 'r') as f:
    line = f.readlines()[0].rstrip()

print(sum([compute_hash(s) for s in line.split(',')]))

