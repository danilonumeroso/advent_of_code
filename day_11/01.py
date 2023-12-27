from itertools import chain

def get_galaxy_locations(map_):
    """
        Get the locations of all the galaxies in the map.
    """
    dim = len(map_)
    return [(i, j) for i in range(len(map_)) for j in range(len(map_[i])) if map_[i][j] == "#"]

def get_empty_rows(map_):
    """
        Get the rows of the map that are empty.
    """
    return [i for i in range(len(map_)) if all(map(lambda x: x == ".", map_[i]))]

def get_empty_cols(map_):
    """
        Get the columns of the map that are empty.
    """

    # Transpose the map
    map_ = list(map(list, zip(*map_)))
    return get_empty_rows(map_)


def expand_universe(galaxies, empty_rows, empty_cols, expansion=2):
    new_galaxies = []
    for x, y in galaxies:
        empty_cols_before_galaxy = sum([1 for _ in empty_cols if _ < y])
        empty_rows_before_galaxy = sum([1 for _ in empty_rows if _ < x])
        new_galaxies.append((x + empty_rows_before_galaxy * (expansion - 1), y + empty_cols_before_galaxy * (expansion - 1)))

    return new_galaxies

def l1_distance(galaxy_1, galaxy_2):
    return abs(galaxy_1[0] - galaxy_2[0]) + abs(galaxy_1[1] - galaxy_2[1])

with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

galaxies = get_galaxy_locations(lines)
empty_rows, empty_cols = get_empty_rows(lines), get_empty_cols(lines)
galaxies = expand_universe(galaxies, empty_rows, empty_cols, expansion=2)

# Compute the distance between each pair of galaxies
distances = [[l1_distance(galaxy_1, galaxy_2) for galaxy_1 in galaxies] for galaxy_2 in galaxies]

print(sum(map(sum, distances)) // 2)