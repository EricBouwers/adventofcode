#!/usr/bin/env python

test_1 = """"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def part1(data):
    return None


def part2(data):
    return None


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == None
    assert part1(test_2.splitlines()) == None
    assert part2(test_3.splitlines()) == None
    assert part2(test_4.splitlines()) == None

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

