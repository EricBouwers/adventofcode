#!/usr/bin/env python

import sys, re


def is_valid(password):
    password = str(password)
    prev = None
    double = False
    higher = True
    for p in [int(x) for x in password]:
        double = double or p == prev
        higher = higher and (prev is None or p >= prev)
        prev = p

    return double and higher


def is_valid2(password):
    password = str(password)
    prev = None
    higher = True
    double_digits = []
    for p in [int(x) for x in password]:
        if p == prev:
            double_digits.append(p)
        higher = higher and (prev is None or p >= prev)
        prev = p

    valid_double_digits = [x for x in double_digits if not re.findall(r'[' + str(x) + ']{3,}', password)]

    return higher and len(valid_double_digits) > 0


def part1(data):
    r = [int(x) for x in data.split("-")]

    all_passed = set()
    for r in range(r[0], r[1]):
        if is_valid(r):
            all_passed.add(r)

    return len(all_passed)


def part2(data):
    r = [int(x) for x in data.split("-")]

    all_passed = set()
    for r in range(r[0], r[1]):
        if is_valid2(r):
            all_passed.add(r)

    return len(all_passed)


if __name__ == '__main__':

    assert is_valid(111111)
    assert not is_valid(223450)
    assert not is_valid(123789)

    assert is_valid2(112233)
    assert not is_valid2(123444)
    assert is_valid2(111122)

    with open(sys.argv[1]) as f:
        data = f.readlines()

    print(part1(data[0]))
    print(part2(data[0]))

