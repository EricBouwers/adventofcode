#!/usr/bin/env python
from collections import Counter
from functools import cmp_to_key

test_1 = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
test_2 = """"""

FIVE_OF_KIND = 7
FOUR_OF_KIND = 6
FULL_HOUSE = 5
THREE_OF_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1


def determine_score(card, allow_jokers=False):
    counts = Counter(card)

    if allow_jokers and counts['J'] != 5:
        common = [c for c, n in counts.most_common() if c != 'J'][0]
        counts[common] += counts['J']
        del counts['J']

    diff_cards = len(counts.keys())
    if diff_cards == 1:
        return FIVE_OF_KIND
    if diff_cards == 5:
        return HIGH_CARD
    if diff_cards == 4:
        return ONE_PAIR
    if diff_cards == 3:
        return THREE_OF_KIND if 3 in counts.values() else TWO_PAIR
    if diff_cards == 2:
        return FOUR_OF_KIND if 4 in counts.values() else FULL_HOUSE


def parse_data(data, allow_jokers=False):
    return [(l.split(' ')[0], determine_score(l.split(' ')[0], allow_jokers=allow_jokers), int(l.split(' ')[1])) for l in data]


def sort_cards(card1, card2, deck):
    if card1[1] != card2[1]:
        return card1[1] - card2[1]
    else:
        for c1, c2 in zip(card1[0], card2[0]):
            i1, i2 = deck.index(c1), deck.index(c2)
            if i1 != i2:
                return i2 - i1


def sort_card_without_j(card1, card2):
    return sort_cards(card1, card2, ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'])


def sort_card_with_j(card1, card2):
    return sort_cards(card1, card2, ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'])


def part1(data):
    hands = parse_data(data, allow_jokers=False)
    hands.sort(key=cmp_to_key(sort_card_without_j))
    return sum([(i+1) * hand[2] for i, hand in enumerate(hands)])


def part2(data):
    hands = parse_data(data, allow_jokers=True)
    hands.sort(key=cmp_to_key(sort_card_with_j))
    return sum([(i+1) * hand[2] for i, hand in enumerate(hands)])


if __name__ == '__main__':

    assert determine_score('AAAAA') == FIVE_OF_KIND
    assert determine_score('AA8AA') == FOUR_OF_KIND
    assert determine_score('23332') == FULL_HOUSE
    assert determine_score('TTT98') == THREE_OF_KIND
    assert determine_score('23432') == TWO_PAIR
    assert determine_score('A23A4') == ONE_PAIR
    assert determine_score('23456') == HIGH_CARD
    assert determine_score('KTJJT') == TWO_PAIR
    assert determine_score('KTJJT', allow_jokers=True) == FOUR_OF_KIND
    assert determine_score('T55J5', allow_jokers=True) == FOUR_OF_KIND
    assert determine_score('J55J5', allow_jokers=True) == FIVE_OF_KIND
    assert determine_score('J35J3', allow_jokers=True) == FOUR_OF_KIND
    assert part1(test_1.splitlines()) == 6440
    assert part2(test_1.splitlines()) == 5905

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
