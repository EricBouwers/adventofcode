#!/usr/bin/env python

test_1 = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
test_2 = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""


def part1(data):
    for i in range(4, len(data)):
        if len(set(data[i-4:i])) == 4:
            return i
    return None


def part2(data):
    for i in range(14, len(data)):
        if len(set(data[i-14:i])) == 14:
            return i
    return None


if __name__ == '__main__':

    assert part1(test_1.splitlines()[0]) == 7
    assert part1(test_2.splitlines()[0]) == 11
    assert part2(test_1.splitlines()[0]) == 19
    assert part2(test_2.splitlines()[0]) == 26

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()[0]))
    print(part2(data.splitlines()[0]))

