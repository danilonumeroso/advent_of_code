import re

def return_fewest_conf(game):

    result = {'blue': 0, 'red': 0, 'green': 0}

    for trial in game:
        result['blue'] = max(result['blue'], trial['blue'] if 'blue' in trial else 0)
        result['green'] = max(result['green'], trial['green'] if 'green' in trial else 0)
        result['red'] = max(result['red'], trial['red'] if 'red' in trial else 0)

    return result


with open('games.txt', 'r') as f:
    lines = [line for line in f]

digit = re.compile("\d+")
game_ids = [int(digit.search(line).group(0)) for line in [line.split(':')[0] for line in lines]]
game_info_aux = [line.split(';') for line in [line.split(':')[1] for line in lines]]
game_info = []

for line in game_info_aux:
    game_info.append([])
    for trial in line:
        game_info[-1].append({})
        cubes_info = trial.split(',')
        for cube in cubes_info:
            num, color = cube.strip().split(' ')
            game_info[-1][-1][color] = int(num)

assert len(game_ids) == len(game_info)

X = list(map(return_fewest_conf, game_info))

print(sum(map(lambda x: x['blue'] * x['red'] * x['green'], X)))
