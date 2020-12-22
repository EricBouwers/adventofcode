#!/usr/bin/env python
from operator import mul

test_1 = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def parse_decks(data):
    data.pop(0)
    player_1 = []
    player_2 = []
    cur_player = player_1
    while data:
        line = data.pop(0)
        if line != "":
            cur_player.append(int(line))
        else:
            data.pop(0)
            cur_player = player_2

    return player_1, player_2


def play_deck(player_1, player_2, recurse=False):
    decks_player_1 = set()
    decks_player_2 = set()
    while len(player_1) > 0 and len(player_2) > 0:
        p1_deck = " ".join([str(c) for c in player_1])
        p2_deck = " ".join([str(c) for c in player_2])
        if p1_deck in decks_player_1 or p2_deck in decks_player_2:
            return True, player_1, player_2
        else:
            decks_player_1.add(p1_deck)
            decks_player_2.add(p2_deck)

        card_1 = player_1.pop(0)
        card_2 = player_2.pop(0)

        if recurse and card_1 <= len(player_1) and card_2 <= len(player_2):
            player_1_wins, _, _ = play_deck(
                [x for x in player_1[0:card_1]],
                [y for y in player_2[0:card_2]],
                True)
        else:
            player_1_wins = card_1 > card_2

        if player_1_wins:
            player_1.append(card_1)
            player_1.append(card_2)
        else:
            player_2.append(card_2)
            player_2.append(card_1)

    return len(player_1) > 0, player_1, player_2


def part1(data, recurse=False):
    player_1, player_2 = parse_decks(data)
    player_1_wins, player_1, player_2 = play_deck(player_1, player_2, recurse)

    winner_deck = player_1 if player_1_wins else player_2
    winner_deck.reverse()

    return sum([mul(*t) for t in zip(winner_deck, range(1, len(winner_deck) + 1))])


def part2(data):
    return part1(data, True)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 306
    assert part2(test_1.splitlines()) == 291

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

