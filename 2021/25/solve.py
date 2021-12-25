#!/usr/bin/env python
from collections import defaultdict

test_1 = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def parse_data(data):
    cucumbers = defaultdict(list)
    max_x = 0
    max_y = 0
    for line in data:
        max_x = 0
        for c in line:
            if c != '.':
                 cucumbers[c].append((max_x, max_y))
            max_x += 1
        max_y += 1

    return cucumbers, max_x, max_y


def step_right(c, max_x):
    return (c[0] + 1) % max_x, c[1]


def step_down(c, max_y):
    return c[0], (c[1] + 1) % max_y


def take_step(cucumbers, max_x, max_y):
    new_cucumbers = defaultdict(list)
    all_coors = set(cucumbers['>'] + cucumbers['v'])

    new_r = [step_right(cucumber, max_x) if step_right(cucumber, max_x) not in all_coors else cucumber for cucumber in cucumbers['>']]
    new_cucumbers['>'] = new_r

    all_coors = set(new_cucumbers['>'] + cucumbers['v'])
    new_d = [step_down(cucumber, max_y) if step_down(cucumber, max_y) not in all_coors else cucumber for cucumber in
             cucumbers['v']]
    new_cucumbers['v'] = new_d

    return new_cucumbers


def are_different(c1, c2):
    return set(c1['>']) - set(c2['>']) or set(c1['v']) - set(c2['v'])


def part1(data):
    cucumbers, max_x, max_y = parse_data(data)
    steps = 1
    new_cucumbers = take_step(cucumbers, max_x, max_y)
    while are_different(cucumbers, new_cucumbers):
        cucumbers = new_cucumbers
        new_cucumbers = take_step(cucumbers, max_x, max_y)
        steps += 1
        print(steps)
    return steps


def part2(data):
    return None


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 58
    assert part2(test_3.splitlines()) == None
    assert part2(test_4.splitlines()) == None

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

