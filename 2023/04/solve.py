#!/usr/bin/env python
from collections import defaultdict

test_1 = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
test_2 = """"""


def parse_data(data):
    cards = {}
    for idx, line in enumerate(data):
        numbers = line.split(":")[1].split(" | ")
        cards[idx+1] = (
            set([int(x) for x in numbers[0].split(" ") if x]),
            set([int(x) for x in numbers[1].split(" ") if x])
        )

    return cards


def part1(data):
    cards = parse_data(data)
    return sum([
        int(2**(len(card[0].intersection(card[1])) - 1)) for card in cards.values()
    ])


def part2(data):
    cards = parse_data(data)
    copies_of_cards = defaultdict(lambda: 1)
    for idx, card in cards.items():
        wins = len(card[0].intersection(card[1]))
        for card_idx in range(idx+1, idx+wins+1):
            copies_of_cards[card_idx] += copies_of_cards[idx]

    return sum([copies_of_cards[idx] for idx in cards.keys()])


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 13
    assert part2(test_1.splitlines()) == 30

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

