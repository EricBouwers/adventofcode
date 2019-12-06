#!/usr/bin/env python

import sys
from collections import defaultdict

test_1 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""

test_2 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""


def graph(data):
    orbits = defaultdict(list)
    orbitted = defaultdict(list)
    planets = set()

    for d in data:
        p = d.split(")")
        orbits[p[1]].append(p[0])
        orbitted[p[0]].append(p[1])
        planets.update(p)

    return orbits, planets, orbitted


def count_planet(planet, orbits, cache):
    total = 0
    for p in orbits[planet]:
        if p not in cache:
            p_count = count_planet(p, orbits, cache)
            cache[p] = p_count

        total += cache[p]
        total += 1

    return total


def count_deps(orbits, planets):
    counts = {}
    for p in planets:
        counts[p] = count_planet(p, orbits, counts)

    return counts


def part1(data):
    orbits, planets, _ = graph(data)
    counts = count_deps(orbits, planets)
    return sum(counts.values())


def part2(data):
    orbits, planets, orbitted = graph(data)
    my_orbit = orbits["YOU"][0]
    santas_orbit = orbits["SAN"][0]

    steps = [(1, o) for o in orbits[my_orbit]]
    seen = set(my_orbit)

    while len(steps) > 0:
        o_step, cur_pos = steps.pop()
        seen.add(cur_pos)

        if cur_pos == santas_orbit:
            return o_step
        else:
            steps = steps + \
                    [(o_step+1, o) for o in orbits[cur_pos] if o not in seen] + \
                    [(o_step+1, o) for o in orbitted[cur_pos] if o not in seen]


if __name__ == '__main__':

    assert part1(test_1.split("\n")) == 42
    assert part2(test_2.split("\n")) == 4

    with open(sys.argv[1]) as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

