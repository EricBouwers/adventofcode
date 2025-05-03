#!/usr/bin/env python
import re

test_1 = """ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb
"""
test_2 = """qjhvhtzxzqqjkmpb
xxyxx
uurcxstgmygtbstg
ieodomkazucvgmuy
"""


def parse_data(data):
    return data


def is_nice1(line):
    disallowed = r"ab|cd|pq|xy"
    has_vowel = r"[aeiou]"
    has_consecutive = r"([a-z])\1"

    return re.search(disallowed, line) is None \
            and len(re.findall(has_vowel, line)) > 2 \
            and re.search(has_consecutive, line) is not None


def is_nice2(line):
    two_pairs = r"([a-z][a-z])(.)*\1"
    two_letters = r"([a-z])(.)\1"

    return re.search(two_pairs, line) is not None \
            and re.search(two_letters, line) is not None

def part1(data):
    lines = parse_data(data)
    return sum(map(is_nice1, lines))


def part2(data):
    lines = parse_data(data)
    return sum(map(is_nice2, lines))


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 2
    assert part2(test_2.splitlines()) == 2

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
