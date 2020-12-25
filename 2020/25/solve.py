#!/usr/bin/env python

test_1 = """5764801
17807724"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def part1(data):
    card = int(data[0])
    door = int(data[1])

    card_loop = calc_loop_size(card)

    print(card_loop)

    secret = 1
    for i in range(card_loop):
        secret = secret * door
        secret = secret % 20201227

    return secret


def calc_loop_size(card):
    value = 1
    loop = 0
    while value != card:
        value = value * 7
        value = value % 20201227
        loop += 1
    return loop


def part2(data):
    return None


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 14897079
    assert part2(test_3.splitlines()) == None
    assert part2(test_4.splitlines()) == None

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

