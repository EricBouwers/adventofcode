#!/usr/bin/env python
import itertools
from collections import defaultdict
from copy import deepcopy

test_1 = """"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def predictable(n):
    c = 0
    while True:
        c += 1
        yield c
        c = 0 if c == n else c


def part1(p1_pos, p2_pos):
    scores = [0, 0]
    positions = [p1_pos - 1, p2_pos - 1]
    throws = 0
    dice = predictable(100)
    turn = 0
    while max(scores) < 1000:
        p_throws = sum([next(dice), next(dice), next(dice)])
        throws += 3
        positions[turn] = (positions[turn] + p_throws) % 10
        scores[turn] += positions[turn] + 1
        turn = 0 if turn == 1 else 1

    return throws * min(scores)


def part2(p1_pos, p2_pos):
    games = defaultdict(lambda: 0)
    games[(0, 0, p1_pos - 1, p2_pos - 1, 0)] = 1
    wins = [0, 0]

    has_games = True
    while has_games:
        new_games = defaultdict(lambda: 0)
        for game, universes in games.items():
            for t1 in range(1, 4):
                for t2 in range(1, 4):
                    for t3 in range(1, 4):
                        p1_score, p2_score, p1_pos, p2_pos, turn = deepcopy(game)
                        scores = [p1_score, p2_score]
                        positions = [p1_pos, p2_pos]
                        p_throws = sum([t1, t2, t3])
                        positions[turn] = (positions[turn] + p_throws) % 10
                        scores[turn] += positions[turn] + 1
                        if max(scores) >= 21:
                            wins[turn] += universes
                        else:
                            turn = 0 if turn == 1 else 1
                            new_games[(scores[0], scores[1], positions[0], positions[1], turn)] += universes
        games = new_games
        has_games = len(games) > 0

    return max(wins)


if __name__ == '__main__':

    assert part1(4, 8) == 739785
    assert part2(4, 8) == 444356092776315

    with open('input') as f:
        data = f.read()

    print(part1(7, 8))
    print(part2(7, 8))

