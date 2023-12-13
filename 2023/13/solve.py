#!/usr/bin/env python

test_1 = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""
test_2 = """"""


def parse_data(data):
    patterns = []
    cur_pattern = []

    for line in data:
        if line == '':
            patterns.append(cur_pattern)
            cur_pattern = []
        else:
            cur_pattern.append([c for c in line])

    patterns.append(cur_pattern)
    return patterns


def get_mirror_info(p, original=None):
    for i in range(len(p) -1):
        if p[i] == p[i+1] and all([t[0] == t[1] for t in zip(reversed(p[:i+1]), p[i+1:])]) and ('H', i+1) != original:
            return 'H', i+1

    # rotated_p = [[line[i] for line in p] for i in range(len(p[0]))]
    p = [*zip(*p)]

    for i in range(len(p) -1):
        if p[i] == p[i+1] and all([t[0] == t[1] for t in zip(reversed(p[:i+1]), p[i+1:])]) and ('V', i+1) != original:
            return 'V', i+1


def get_smudged_mirror_info(p, original):
    for y in range(len(p)):
        for x in range(len(p[0])):
            p[y][x] = '.' if p[y][x] == '#' else '#'
            info = get_mirror_info(p, original)
            if info is not None:
                return info
            else:
                p[y][x] = '.' if p[y][x] == '#' else '#'


def part1(data):
    patterns = parse_data(data)

    total = 0
    for p in patterns:
        t, i = get_mirror_info(p)
        total += i if t == 'V' else 100*i

    return total


def part2(data):
    patterns = parse_data(data)

    total = 0
    for p in patterns:
        original = get_mirror_info(p)
        t, i = get_smudged_mirror_info(p, original)

        total += i if t == 'V' else 100*i

    return total


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 405
    assert part2(test_1.splitlines()) == 400

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
