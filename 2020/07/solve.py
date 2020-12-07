#!/usr/bin/env python
from collections import defaultdict

test_1 = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
test_2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


def parse_data(data):
    contains = defaultdict(list)
    for rule in data:
        words = rule.split()
        current_color = "{} {}".format(words[0], words[1])
        if 'no other bags' in rule:
            contains[current_color] = []
        else:
            idx = 4
            while idx < len(words):
                number = words[idx]
                color = "{} {}".format(words[idx + 1], words[idx + 2])
                contains[current_color].append((color, int(number)))
                idx += 4

    return contains


def is_contained_in(contains, color):
    contained_in_color = set([k for k, v in contains.items() if color in [x[0] for x in v]])
    if len(contained_in_color) == 0:
        return contained_in_color
    else:
        return set.union(*[is_contained_in(contains, c) for c in contained_in_color] + [contained_in_color])


def should_contain(contains, color):
    contained_bags = contains[color]
    if len(contained_bags) == 0:
        return 0
    else:
        return sum([(count * should_contain(contains, color)) + count for color, count in contained_bags])


def part1(data, color_of_interest):
    contains = parse_data(data)
    cs = is_contained_in(contains, color_of_interest)
    return len(cs)


def part2(data, color_of_interest):
    contains = parse_data(data)
    return should_contain(contains, color_of_interest)


if __name__ == '__main__':

    assert part1(test_1.splitlines(), "shiny gold") == 4
    assert part2(test_1.splitlines(), "shiny gold") == 32
    assert part2(test_2.splitlines(), "shiny gold") == 126

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines(), 'shiny gold'))
    print(part2(data.splitlines(), 'shiny gold'))

