#!/usr/bin/env python
from collections import defaultdict
from functools import reduce
from os import times

test_1 = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""
test_2 = """"""


def parse_data(data):
    ingredients = {}
    for line in data:
        parts = line.split(" ")
        ingredients[parts[0][0:-1]] = {
            'cap': int(parts[2][0:-1]),
            'dur': int(parts[4][0:-1]),
            'fla': int(parts[6][0:-1]),
            'tex': int(parts[8][0:-1]),
            'cal': int(parts[10]),
        }
    return ingredients

def get_spoons(nr_of_ingredients, req_amount):
    if nr_of_ingredients == 1:
        return [[req_amount]]
    else:
        pos_spoons = []
        for i in range(1, req_amount):
            for pos in get_spoons(nr_of_ingredients - 1, req_amount - i):
                pos_spoons.append([i] + pos)
        return pos_spoons


def check_spoons(ingredients, cal=None):
    max_score = 0
    spoon_possibilities = get_spoons(len(ingredients.keys()), 100)

    for s in spoon_possibilities:
        cookie_properties = defaultdict(lambda: 0)
        for prop in ['cap', 'dur', 'fla', 'tex', 'cal']:
            for spoons, ingredient in zip(s, ingredients.values()):
                cookie_properties[prop] += spoons * ingredient[prop]

        calories = cookie_properties.pop('cal')
        score = reduce(lambda acc, v: acc * (v if v > 0 else 0), cookie_properties.values(), 1)

        if cal is None or calories == cal:
            max_score = max([score, max_score])

    return max_score

def part1(data):
    ingredients = parse_data(data)
    return check_spoons(ingredients)

def part2(data):
    ingredients = parse_data(data)
    return check_spoons(ingredients, cal=500)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 62842880
    assert part2(test_1.splitlines()) == 57600000

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

