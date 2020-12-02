#!/usr/bin/env python

import sys

test_1 = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def part1(data):
    valid = 0
    for line in data:
        parts = line.split(" ")
        letter = parts[1][0]
        minimal, maximal = parts[0].split("-")
        letter_count = sum([1 if x == letter else 0 for x in parts[2]])

        valid += 1 if int(minimal) <= letter_count <= int(maximal) else 0
    return valid


def part2(data):
    valid = 0
    for line in data:
        parts = line.split(" ")
        letter = parts[1][0]
        pos1, pos2 = [int(x) for x in parts[0].split("-")]
        valid_password = (parts[2][pos1-1] == letter) ^ (parts[2][pos2-1] == letter)

        valid += 1 if valid_password else 0
    return valid


if __name__ == '__main__':

    assert part1(test_1.split('\n')) == 2
    assert part2(test_1.split('\n')) == 1

    with open('input') as f:
        data = f.readlines()

    print(part1(data))
    print(part2(data))

