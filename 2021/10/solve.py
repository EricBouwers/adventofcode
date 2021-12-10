#!/usr/bin/env python
from functools import reduce
from statistics import median

test_1 = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""
test_2 = """"""
test_3 = """"""
test_4 = """"""

PAIRS = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>'
}

ERROR_SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

COMPLETE_SCORES = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def part1(data):
    parse_errors = []
    for l in data:
        stack = []
        for c in l:
            if c in PAIRS:
                stack.append(c)
            else:
                open_char = stack.pop()
                if c is not PAIRS[open_char]:
                    parse_errors.append(c)
    return sum([ERROR_SCORES[e] for e in parse_errors])


def part2(data):
    additions = []
    for l in data:
        stack = []
        parse_error = False
        score = 0
        for c in l:
            if c in PAIRS:
                stack.append(c)
            else:
                open_char = stack.pop()
                if c is not PAIRS[open_char]:
                    parse_error = True

        if not parse_error:
            adds = [PAIRS[r] for r in reversed(stack)]
            score = reduce(lambda x, y: (x * 5) + COMPLETE_SCORES[y], adds, 0)
            additions.append(score)

    return median(additions)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 26397
    assert part2(test_1.splitlines()) == 288957

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

