#!/usr/bin/env python
from functools import reduce
from operator import mul

test_1 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
test_2 = """"""


start_config = {
    'red': 12, 'green': 13, 'blue': 14
}


def parse_game(game):
    return {g.split(" ")[1]: int(g.split(" ")[0]) for g in game.split(", ")}


def parse_data_line(line):
    parts = line.split(': ')[1].split('; ')
    return [parse_game(p) for p in parts]


def game_is_possible(game, start):
    possible = True
    for color, total in game.items():
        possible = possible and total <= start[color]
    return possible


def part1(data):
    parsed = {idx+1: parse_data_line(l) for idx,l in enumerate(data)}
    total = 0
    for index, games in parsed.items():
        if all([game_is_possible(game, start_config) for game in games]):
            total += index
    return total


def part2(data):
    parsed = {idx + 1: parse_data_line(l) for idx, l in enumerate(data)}

    total = 0
    for index, games in parsed.items():
        minimal_config = {'red': 0, 'blue': 0, 'green': 0}
        for game in games:
            minimal_config['red'] = max(minimal_config['red'], game.get('red') or 0)
            minimal_config['blue'] = max(minimal_config['blue'], game.get('blue') or 0)
            minimal_config['green'] = max(minimal_config['green'], game.get('green') or 0)
        total += reduce(mul, minimal_config.values(), 1)
    return total


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 8
    assert part2(test_1.splitlines()) == 2286

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

