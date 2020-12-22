#!/usr/bin/env python

test_1 = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def parse_data(data):
    allergens = {}
    foods = []

    for line in data:
        parts = line.split(' (contains ')
        cur_allergens = set(parts[1].replace(')', '').replace(',', '').split(' '))
        ingredients = set(parts[0].split(' '))
        for allergen in cur_allergens:
            if allergen in allergens:
                allergens[allergen] = allergens[allergen].intersection(ingredients)
            else:
                allergens[allergen] = ingredients

        foods.append(parts[0].split(' '))

    return allergens, foods


def flatten(t):
    return [item for sublist in t for item in sublist]


def part1(data):
    allergens, foods = parse_data(data)
    allergen_ingredients = flatten(allergens.values())
    all_ingredients = set(flatten(foods))
    non_allergens = [i for i in all_ingredients if i not in allergen_ingredients]

    occurrences = 0
    for i in non_allergens:
        occurrences += len([f for f in foods if i in f])

    return occurrences


def part2(data):
    allergens, foods = parse_data(data)

    ingredient_allergens = {}
    while allergens:
        ingredient_allergens.update({i.pop(): a for a, i in allergens.items() if len(i) == 1})
        allergens = {a: (i - set(ingredient_allergens.keys())) for a, i in allergens.items() if len(i) > 0}

    inverse = {v: k for k, v in ingredient_allergens.items()}
    allergens = sorted(inverse.keys())

    return ",".join(inverse[a] for a in allergens)


if __name__ == '__main__':
    assert part1(test_1.splitlines()) == 5
    assert part2(test_1.splitlines()) == 'mxmxvkd,sqjhc,fvjkl'

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
