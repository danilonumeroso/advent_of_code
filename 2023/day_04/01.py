with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]


def compute_card_values(card_numbers, my_numbers):
    number_of_matches = 0 

    for x in my_numbers:
        if x in card_numbers:
            number_of_matches += 1

    if number_of_matches == 0:
        return 0 

    return 2**(number_of_matches-1)

card_values = []
for line in lines:
    card_info, my_numbers = line.split('|')
    _, card_numbers = card_info.split(':')

    card_numbers = list(map(int, filter(lambda x: len(x) > 0, card_numbers.strip().split(' '))))
    my_numbers = list(map(int, filter(lambda x: len(x) > 0, my_numbers.strip().split(' '))))
    card_values.append(
        compute_card_values(card_numbers, my_numbers)
    )

print(sum(card_values))