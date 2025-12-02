#!/usr/bin/env python
import re

test_1 = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
test_2 = """"""


def parse_data(data):
    return [list(map(int, x.split("-"))) for x in data[0].split(",")]


def is_invalid1(id):
    length = len(id)
    return length % 2 == 0 and id[0:length//2] == id[length//2:]


def is_invalid2(id):
    half = len(id) // 2

    for i in range(1, half+1):
        regex = "^(%s)+$" % id[0:i]
        if re.match(regex, id) is not None:
            return True



def part1(data, f=is_invalid1):
    ranges = parse_data(data)

    total_invalid = 0
    for r in ranges:
        for i in range(r[0], r[1]+1):
            total_invalid += i if f(str(i)) else 0

    return total_invalid


def part2(data):
    return part1(data, is_invalid2)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 1227775554
    assert part2(test_1.splitlines()) == 4174379265

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

