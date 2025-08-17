#!/usr/bin/env python
import re
from collections import defaultdict

test_1 = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""
test_2 = """"""


def parse_data(data):
    deers = []
    for line in data:
        nums = re.findall(r'\d+', line)
        deers.append(tuple([int(x) for x in nums]))
    
    return deers

def run_reindeers(deers, seconds):
    max_dist = 0
    max_i = 0
    distances = {}
    for i, (km_s, fly, rest) in enumerate(deers):
        times, left = divmod(seconds, fly + rest)
        dist = (times * fly * km_s) + min(fly, left) * km_s
        distances[i] = dist

    return distances


def part1(data, seconds=2503):
    deers = parse_data(data)
    return max(run_reindeers(deers, seconds).values())

def part2(data, seconds=2503):
    deers = parse_data(data)
    points = defaultdict(lambda: 0)

    for s in range(1, seconds+1):
        distances = run_reindeers(deers, s)
        max_dist = max(distances.values())
        for who, dist in distances.items():
            if dist == max_dist:
                points[who] += 1

    return max(points.values())


if __name__ == '__main__':

    assert part1(test_1.splitlines(), 1000) == 1120
    assert part2(test_1.splitlines(), 1000) == 689

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

