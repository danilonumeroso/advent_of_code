def find_header(headers, line):
    for header in headers:
        if header in line:
            return header
    return None

def is_initial_seed_location(location, headers, maps, initial_seeds):
    seed = location
    for header in headers:
        for starting_point in maps[header]:
            dest_start, length = maps[header][starting_point]
            if seed >= starting_point and seed < starting_point + length:
                seed = dest_start + (seed - starting_point)
                break

    for starting_seed, length in initial_seeds:
        if seed >= starting_seed and seed < starting_seed + length:
            return True

    return False

with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

headers = ["seed-to-soil", 
           "soil-to-fertilizer", 
           "fertilizer-to-water", 
           "water-to-light", 
           "light-to-temperature", 
           "temperature-to-humidity", 
           "humidity-to-location"]

reversed_maps = {header: {} for header in headers}
# Saving seed ranges as (start, length) tuples
initial_seeds = list(map(int, lines[0].split(':')[-1].strip().split(' ')))
initial_seeds = [(initial_seeds[i], initial_seeds[i+1]) for i in range(0, len(initial_seeds), 2)]
current_header = None

for line in lines[1:]:
    if line == "":
        continue
    
    if find_header(headers, line) is not None:
        current_header = find_header(headers, line)
        continue

    dest_start, source_start, length = tuple(map(int, line.strip().split(' ')))
    
    """
        Same reasoning as part 1, but we reverse the mapping as we will be starting the lookup
        from the location and not the seed this time.
    """
    reversed_maps[current_header][dest_start] = (source_start, length)

"""
    Loop through all possible locations and check if any of them is a location where
    an initial seed was planted. Not the smartest solution.
"""
for location in range(max(reversed_maps['humidity-to-location'].keys())):
    if is_initial_seed_location(location, reversed(headers), reversed_maps, initial_seeds):
        print(location)
        break
