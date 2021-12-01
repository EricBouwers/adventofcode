#!/usr/bin/env python

test_1 = """199
200
208
210
200
207
240
269
260
263"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def part1(data):
    inc = 0
    prev = data[0]
    for d in data:
        d = int(d)
        inc += 1 if d > prev else 0
        prev = d
    return inc


def part2(data):
    data = [int(d) for d in data]
    slices = [sum(data[x:x+3]) for x in range(0, len(data)-2)]
    return part1(slices)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 7
    assert part2(test_1.splitlines()) == 5

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

