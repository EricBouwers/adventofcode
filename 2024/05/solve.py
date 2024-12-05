#!/usr/bin/env python
from collections import defaultdict
from functools import cmp_to_key

test_1 = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
test_2 = """"""


def parse_data(data):
    rules = defaultdict(lambda:set())
    updates = []

    for line in data:
        if '|' in line:
            ordering = [int(x) for x in line.split('|')]
            rules[ordering[0]].add(ordering[1])
        elif ',' in line:
            update = [int(x) for x in line.split(',')]
            updates.append(update)

    return rules, updates


def is_valid(update, rules):
    for i, u in enumerate(update):
        if len(set(update[:i]).intersection(rules[u])) > 0:
            return False
    return True


def part1(data):
    rules, updates = parse_data(data)

    count = 0
    for update in updates:
        if is_valid(update, rules):
            count += update[int(len(update) / 2)]
    return count


def part2(data):
    rules, updates = parse_data(data)
    count = 0
    for update in updates:
        if not is_valid(update, rules):
            update.sort(key=cmp_to_key(lambda x, y: 1 if y in rules[x] else -1))
            count += update[int(len(update) / 2)]
    return count


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 143
    assert part2(test_1.splitlines()) == 123

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

