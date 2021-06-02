import random


def get_card(_deck):
    return random.choice(_deck)


def hand_total(_list):
    if sum(_list) > 21 and 11 in _list:
        return sum(_list) - 10
    else:
        return sum(_list)


