#!/usr/bin/env python
from collections import defaultdict

test_1 = """1
10
100
2024
"""
test_2 = """1
2
3
2024
"""


def parse_data(data):
    return [int(d) for d in data]


def hash_number(prev):
    result = prev ^ (prev * 64)
    result = result % 16777216
    result = result ^ (result // 32)
    result = result % 16777216
    result = result ^ (result * 2048)
    result = result % 16777216
    return result


def part1(data):
    secrets = parse_data(data)

    result = 0
    for s in secrets:
        for _ in range(2000):
            s = hash_number(s)
        result += s

    return result


def part2(data):
    secrets = parse_data(data)
    result = 0
    main_sequences = defaultdict(list)
    for m in secrets:
        monkey_sequences = set()
        cur_sequence = []
        s = m
        s_price = s % 10
        for i in range(2000):
            new_s = hash_number(s)
            new_s_price = new_s % 10
            price_diff = new_s_price - s_price
            cur_sequence.append(price_diff)
            if len(cur_sequence) > 4:
                cur_sequence = cur_sequence[1:5]

            cur_sequence_key = ",".join(map(str, cur_sequence))
            if cur_sequence_key not in monkey_sequences:
                main_sequences[cur_sequence_key].append(new_s_price)
                monkey_sequences.add(cur_sequence_key)
            s = new_s
            s_price = new_s_price

    return max([sum(v) for v in main_sequences.values()])


if __name__ == '__main__':
    assert hash_number(123) == 15887950
    assert hash_number(15887950) == 16495136
    assert part1(test_1.splitlines()) == 37327623
    assert part2(test_2.splitlines()) == 23

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

