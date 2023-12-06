#!/usr/bin/env python

test_1 = """Time:      7  15   30
Distance:  9  40  200"""
test_2 = """"""


def parse_data(data):
    times = [int(x) for x in data[0].split(":")[1].split()]
    dists = [int(x) for x in data[1].split(":")[1].split()]
    return times, dists


def part1(data):
    times, dists = parse_data(data)

    wins = 1
    for time, dist in zip(times,dists):
        wins *= len([r for r in range(0, time) if (r * (time-r)) > dist])

    return wins


def part2(data):
    time = int(data[0].split(":")[1].replace(' ', ''))
    dist = int(data[1].split(":")[1].replace(' ', ''))

    return len([r for r in range(0, time) if (r * (time-r)) > dist])


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 288
    assert part2(test_1.splitlines()) == 71503

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

