import re
from functools import reduce

def get_race_distance(time_spent_holding_the_button, time_limit):
    """
        Get the distance covered by the boat given the time spent holding the button.
    """
    return (time_limit - time_spent_holding_the_button) * time_spent_holding_the_button


with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

times = list(map(int, re.findall(r'\d+', lines[0])))
distances = list(map(int, re.findall(r'\d+', lines[1])))

number_of_possible_ways = []
# For each time limit, get the number of possible ways in which the boat can covered a distance greater than the record
for time_limit, record in zip(times, distances):
    number_of_possible_ways.append(len(list(filter(lambda x: x > record, 
                                         [get_race_distance(time_spent_holding_the_button, time_limit) 
                                          for time_spent_holding_the_button in range(1, time_limit)]))))

print(reduce(lambda a,b: a*b, number_of_possible_ways, 1))
