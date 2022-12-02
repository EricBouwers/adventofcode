#!/usr/bin/env python

test_1 = """A Y
B X
C Z
"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def translate_to_hand(i):
    if i in ['A', 'X']:
        return 'R'
    if i in ['B', 'Y']:
        return 'P'
    if i in ['C', 'Z']:
        return 'S'


def parse_hand_data(data):
    plays = []
    for d in data:
        plays.append([x for x in map(translate_to_hand, d.split(" "))])
    return plays


def translate_to_play(play):
    if play[1] == 'Y':
        return [play[0], play[0]]
    elif play[1] == 'X':
        return [play[0], 'C' if play[0] == 'A' else 'A' if play[0] == 'B' else 'B']
    else:
        return [play[0], 'B' if play[0] == 'A' else 'C' if play[0] == 'B' else 'A']


def parse_play_data(data):
    plays = []
    for d in data:
        plays.append([translate_to_hand(x) for x in translate_to_play(d.split(" "))])
    return plays


MATCH_SCORES = {
    ('R', 'R'): 3,
    ('R', 'P'): 6,
    ('R', 'S'): 0,
    ('P', 'R'): 0,
    ('P', 'P'): 3,
    ('P', 'S'): 6,
    ('S', 'R'): 6,
    ('S', 'P'): 0,
    ('S', 'S'): 3,
}

HAND_SCORES = {'R': 1, 'P': 2, 'S': 3}


def part1(data):
    return sum(map(lambda x: MATCH_SCORES[(x[0], x[1])] + HAND_SCORES[x[1]], parse_hand_data(data)))


def part2(data):
    return sum(map(lambda x: MATCH_SCORES[(x[0], x[1])] + HAND_SCORES[x[1]], parse_play_data(data)))


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 15
    assert part2(test_1.splitlines()) == 12

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

