def find_header(headers, line):
    for header in headers:
        if header in line:
            return header
    return None

def get_location_from_seed(seed, headers, maps):
    """
        Starting from an initial seed, find the corresponing location in which the seed was planted.
    """
    location = seed
    for header in headers:
        for from_ in maps[header]:
            to_, length = maps[header][from_]
            # Check if the input falls in the mapping range
            if location >= from_ and location < from_ + length:
                # Compute the right index for subsequent mappings
                location = to_ + (location - from_)
                break

    return location

with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

headers = ["seed-to-soil", 
           "soil-to-fertilizer", 
           "fertilizer-to-water", 
           "water-to-light", 
           "light-to-temperature", 
           "temperature-to-humidity", 
           "humidity-to-location"]

maps = {header: {} for header in headers}
seeds = list(map(int, lines[0].split(':')[-1].strip().split(' ')))
current_header = None


for line in lines[1:]:
    if line == "":
        continue
    
    if find_header(headers, line) is not None:
        current_header = find_header(headers, line)
        continue

    dest_start, source_start, length = tuple(map(int, line.strip().split(' ')))
    
    """
        For performance reasons, we won't enumerate every possible mapping in the dictionary, but
        only save the range of values, since the dictionary would end up being too big given
        the input size otherwise. Given x, we can easily get the corresponding output by checking
        if x falls in the range of any of the mappings (dest_start, dest_start + length), 
        and then applying the corresponding function:
        y = f(x) = dest_start + (x - source_start)
    """
    maps[current_header][source_start] = (dest_start, length)


print(min([get_location_from_seed(starting_seed, headers, maps) for starting_seed in seeds]))
