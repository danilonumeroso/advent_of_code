import re
from functools import reduce

def get_race_distance(time_spent_holding_the_button, time_limit):
    """"
        Get the distance covered by the boat given the time spent holding the button.
    """
    return (time_limit - time_spent_holding_the_button) * time_spent_holding_the_button

def compute_interval_length(a, b):
    assert b >= a
    return b - a + 1

def find_inf(time, record):
    a, b = 0, time-1
    while compute_interval_length(a, b) > 2:
        c = (a + b) // 2
        if get_race_distance(c, time) > record:
            b = c
        else:
            a = c

    return b


def find_sup(time, record):
    a, b = 0, time-1
    while compute_interval_length(a, b) > 2:
        c = (a + b) // 2
        if get_race_distance(c, time) > record:
            a = c
        else:
            b = c 

    return a

def find_interval(time, record):
    return (find_inf(time, record), find_sup(time, record))


with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

time = int(''.join(re.findall(r'\d+', lines[0])))
record = int(''.join(re.findall(r'\d+', lines[1])))

print(compute_interval_length(*find_interval(time, record)))