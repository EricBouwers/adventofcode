#!/usr/bin/env python

import sys, re


def is_valid(password):
    prev = None
    double = False
    while password:
        password, p = divmod(password, 10)
        double = double or p == prev
        if prev is None or p <= prev:
            prev = p
        else:
            return False

    return double


def is_valid2(password):
    prev = None
    double_digits = set()
    tmp = password
    while tmp:
        tmp, p = divmod(tmp, 10)
        if p == prev:
            double_digits.add(str(p))
        if prev is None or p <= prev:
            prev = p
        else:
            return False

    str_password = str(password)
    valid_double_digits = [x for x in double_digits if not re.findall("".join(3*[x]), str_password)]

    return len(valid_double_digits) > 0


def part1(data):
    r = [int(x) for x in data.split("-")]

    all_passed = 0
    for r in range(r[0], r[1]):
        all_passed += 1 if is_valid(r) else 0

    return all_passed


def part2(data):
    r = [int(x) for x in data.split("-")]

    all_passed = 0
    for r in range(r[0], r[1]):
        all_passed += 1 if is_valid2(r) else 0

    return all_passed


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

