def compute_number_of_matches(card_numbers, my_numbers):
    """
    This function calculates the number of matches between two lists of numbers.

    Parameters:
    card_numbers (list): A list of numbers, representing the card's numbers.
    my_numbers (list): A list of numbers, representing user's numbers.

    Returns:
    number_of_matches (int): The count of numbers that are present in both lists.
    """
    number_of_matches = 0

    for x in my_numbers:
        if x in card_numbers:
            number_of_matches += 1

    return number_of_matches

def compute_won_cards(base_id, card_numbers, my_numbers, won_cards={}):
    """
    This function computes the values of cards based on the number of matches between card numbers and user's numbers.

    Parameters:
    base_id (int): The base identifier for a card.
    card_numbers (list): A list of numbers, representing the card's numbers.
    my_numbers (list): A list of numbers, representing a user's numbers.
    won_cards (dict): A dictionary representing the cards won so far.

    Returns:
    won_cards (dict): The updated dictionary of won cards after considering the current card.
    """
    number_of_matches = compute_number_of_matches(card_numbers, my_numbers) 

    for offset_id in range(1, number_of_matches+1):
        # You win as many copies of subsequent cards (`offset_id + base_id`) 
        # as the number of scratchcards `base_id` you currently have.
        if (base_id + offset_id) not in won_cards:
            won_cards[base_id + offset_id] = 1 * won_cards[base_id]
        else:
            won_cards[base_id + offset_id] += 1 * won_cards[base_id]

    return won_cards

with open('input.txt') as f:
    lines = [line[:-1] for line in f.readlines()]

card_values = []
won_cards = {card_id: 1 for card_id in range(1, len(lines)+1)}

for i, line in enumerate(lines):

    if (i+1) not in won_cards:
        break

    card_info, my_numbers = line.split('|')
    _, card_numbers = card_info.split(':')

    card_numbers = list(map(int, filter(lambda x: len(x) > 0, card_numbers.strip().split(' '))))
    my_numbers = list(map(int, filter(lambda x: len(x) > 0, my_numbers.strip().split(' '))))
    won_cards = (
        compute_won_cards(i+1, card_numbers, my_numbers, won_cards)
    )

print(sum(won_cards.values()))