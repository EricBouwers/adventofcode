#!/usr/bin/env python

test_1 = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
test_2 = """"""


def parse_data(data):
    equations = []
    for line in data:
        o, l = line.split(": ")
        equations.append((int(o), [int(x) for x in l.split(" ")]))

    return equations


def can_be_true(out, ins, concat=False):
    tries = [ins[0]]
    for x in ins[1:]:
        new_tries = []
        for t in tries:
            new_tries.append(t+x)
            new_tries.append(t * x)
            new_tries.append(int(f"{t}{x}") if concat else 0)
        tries = [t for t in new_tries if t <= out]

    return out in tries


def part1(data):
    equations = parse_data(data)
    return sum([eq[0] for eq in equations if can_be_true(*eq)])


def part2(data):
    equations = parse_data(data)
    return sum([eq[0] for eq in equations if can_be_true(*eq, concat=True)])


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 3749
    assert part2(test_1.splitlines()) == 11387

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

