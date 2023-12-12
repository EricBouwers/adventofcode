#!/usr/bin/env python
import re
from functools import cache
from itertools import product

test_1 = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""
test_2 = """"""


def make_regex(sequence):
    return '^\.*' + '\.+'.join(['#{' + i + '}' for i in sequence]) + '\.*$'


def parse_data(data, times=1):
    return [("?".join([line.split()[0]]*times), make_regex(line.split()[1].split(',') * times)) for line in data]


def get_options(line):
    options = [(c,) if c != '?' else ('.', '#') for c in line]
    return (''.join(o) for o in product(*options))


def part1(data):
    parsed = parse_data(data)

    total_matches = 0
    for line, regex in parsed:
        for option in get_options(line):
            if re.fullmatch(regex, option):
                total_matches += 1

    return total_matches


@cache
def reduce_options(options, sequence):
    if len(options) == 0:
        return 1 if len(sequence) == 0 else 0

    if len(sequence) == 0:
        return 1 if '#' not in options else 0

    cur_option = options[0]
    if cur_option == '.':
        return reduce_options(options[1:], sequence)
    elif cur_option == '#':
        if len(sequence) >= 1:
            to_eat = int(sequence[0])
            could_eat = "." not in options[0:to_eat]
            could_eat &= (len(options) == to_eat and len(sequence) == 1) or (len(options) > to_eat and options[to_eat] in '.?')

            return reduce_options(options[to_eat+1:], sequence[1:]) if could_eat else 0
        else:
            return 0
    elif len(sequence) >= 1:
        to_eat = int(sequence[0])
        could_eat = "." not in options[0:to_eat]
        could_eat &= (len(options) == to_eat and len(sequence) == 1) or (len(options) > to_eat and options[to_eat] in '.?')

        if could_eat:
            return reduce_options(options[to_eat+1:], sequence[1:]) + reduce_options(options[1:], sequence)
        else:
            return reduce_options(options[1:], sequence)


def part2(data):
    total_options = 0
    for line in data:
        expanded = "?".join([line.split()[0]] * 5)
        sequence = line.split()[1].split(',') * 5

        options = ''.join([s for s in reversed(expanded)])
        sequence = [s for s in reversed(sequence)]

        reduced_options = reduce_options(options, tuple(sequence))

        total_options += reduced_options

    return total_options


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 21
    assert part2(test_1.splitlines()) == 525152

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

