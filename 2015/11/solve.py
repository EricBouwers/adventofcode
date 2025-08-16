#!/usr/bin/env python
from collections import Counter

test_1 = """abcdefgh"""
test_2 = """ghijklmn"""


def parse_data(data):
    return data[0]

def num_to_pass(num):
    return "".join([chr(n + 97) for n in num])

def pass_to_num(password):
    return [ord(c) - 97 for c in password]

def has_increasing_nums(numbers):
    for i in range(0, len(numbers)-2):
        if numbers[i] == numbers[i+1]-1 and numbers[i+1] == numbers[i+2]-1:
            return True
    return False

def has_two_pairs(numbers):
    pairs = set()
    for n1, n2 in zip(numbers, numbers[1:]):
        if n1 == n2:
            pairs.add(n1)

    return len(pairs) > 1

def is_valid_password(numbers):
    illegal_chars = len({8,11,14}.intersection(numbers)) != 0
    return not illegal_chars and has_increasing_nums(numbers) and has_two_pairs(numbers)

def calc_next_numbers(numbers):
    cur_i = -1
    numbers[cur_i] += 1
    while numbers[cur_i] > 25:
        numbers[cur_i] = 0
        cur_i -= 1
        numbers[cur_i] += 1
    return numbers

def calc_next_password(password):
    numbers = pass_to_num(password)
    numbers = calc_next_numbers(numbers)

    while not is_valid_password(numbers):
        numbers = calc_next_numbers(numbers)

    return num_to_pass(numbers)

def part1(data):
    password = parse_data(data)
    return calc_next_password(password)


def part2(data):
    password = parse_data(data)
    return calc_next_password(calc_next_password(password))


if __name__ == '__main__':

    assert is_valid_password(pass_to_num('abcdffaa'))
    assert num_to_pass(pass_to_num(test_1.splitlines()[0])) == 'abcdefgh'
    assert part1(test_1.splitlines()) == 'abcdffaa'
    assert part1(test_2.splitlines()) == 'ghjaabcc'

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

