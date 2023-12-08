import random

CARD_STRENGTH = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}

def is_five_of_a_kind(hand):
    return len(set(hand)) == 1

def is_four_of_a_kind(hand):
    return len(set(hand)) == 2 and any(map(lambda x: hand.count(x) == 4, hand))

def is_full_house(hand):
    return len(set(hand)) == 2 and any(map(lambda x: hand.count(x) == 3, hand))

def is_three_of_a_kind(hand):
    return len(set(hand)) == 3 and any(map(lambda x: hand.count(x) == 3, hand))

def is_two_pairs(hand):
    return len(set(hand)) == 3 and any(map(lambda x: hand.count(x) == 2, hand))

def is_one_pair(hand):
    return len(set(hand)) == 4 and any(map(lambda x: hand.count(x) == 2, hand))

def is_high_card(hand):
    return len(set(hand)) == 5

def geq_element_wise(hand1, hand2):
    for card1, card2 in zip(hand1, hand2):
        if CARD_STRENGTH[card1] < CARD_STRENGTH[card2]:
            return False
        elif CARD_STRENGTH[card1] > CARD_STRENGTH[card2]:
            return True
        
    return True

def geq(hand1, hand2):
    if is_five_of_a_kind(hand1):
        return not is_five_of_a_kind(hand2) or geq_element_wise(hand1, hand2)
    
    if is_five_of_a_kind(hand2):
        return False
    
    if is_four_of_a_kind(hand1):
        return not is_four_of_a_kind(hand2) or geq_element_wise(hand1, hand2)

    if is_four_of_a_kind(hand2):
        return False
    
    if is_full_house(hand1):
        return not is_full_house(hand2) or geq_element_wise(hand1, hand2)
    
    if is_full_house(hand2):
        return False
    
    if is_three_of_a_kind(hand1):
        return not is_three_of_a_kind(hand2) or geq_element_wise(hand1, hand2)
    
    if is_three_of_a_kind(hand2):
        return False
    
    if is_two_pairs(hand1):
        return not is_two_pairs(hand2) or geq_element_wise(hand1, hand2)
    
    if is_two_pairs(hand2):
        return False
    
    if is_one_pair(hand1):
        return not is_one_pair(hand2) or geq_element_wise(hand1, hand2)
    
    if is_one_pair(hand2):
        return False
    
    return geq_element_wise(hand1, hand2)


# Implement a quick sort algorithm to sort the hands using the above geq function
def quick_sort(hands_and_bids):
    if len(hands_and_bids) <= 1:
        return hands_and_bids
    
    pivot = random.choice(hands_and_bids)
    less = []
    equal = []
    greater = []

    for hand_and_bid in hands_and_bids:
        if geq(pivot[0], hand_and_bid[0]):
            greater.append(hand_and_bid)
        elif geq(hand_and_bid[0], pivot[0]):
            less.append(hand_and_bid)
        else:
            equal.append(hand_and_bid)

    return quick_sort(less) + equal + quick_sort(greater)



with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

hands = [line.split(' ')[0] for line in lines]
bids = [int(line.split(' ')[1]) for line in lines]

sorted_hands_and_bids = quick_sort(list(zip(hands, bids)))

rank = len(sorted_hands_and_bids)
winning = 0

for hand, bid in sorted_hands_and_bids:
    winning += rank * bid
    rank -= 1

print(winning)