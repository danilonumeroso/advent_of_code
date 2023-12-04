import re

def check_game(game):
    for trial in game:
        if 'blue' in trial and trial['blue'] > 14:
            return False

        if 'red' in trial and trial['red'] > 12:
            return False

        if 'green' in trial and trial['green'] > 13:
            return False

    return True


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

X = map(lambda x: x[0], filter(lambda x: check_game(x[1]), zip(game_ids, game_info)))

print(sum(X))


