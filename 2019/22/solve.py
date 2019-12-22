#!/usr/bin/env python
import datetime
import sys
from collections import deque

test_1 = """deal with increment 7
deal into new stack
deal into new stack"""
test_2 = """cut 6
deal with increment 7
deal into new stack"""
test_3 = """deal with increment 7
deal with increment 9
cut -2"""
test_4 = """"""


def part1(data, size):
    deck = [x for x in range(size)]
    return shuffle_cards(data, deck, size)


def shuffle_cards(data, deck, size):
    for d in data.splitlines():

        if d.startswith("deal into new stack"):
            deck.reverse()

        elif d.startswith("cut"):
            cut_point = int(d.split(" ")[1])
            first_part = deck[0:cut_point]
            deck = deck[cut_point:] + first_part

        elif d.startswith("deal with increment"):
            incr = int(d.split(" ")[3])
            new_deck = [0] * size
            pos = 0
            for x in deck:
                new_deck[pos] = x
                pos += incr
                pos = pos % size
            deck = new_deck

    return deck


def part2(data, size, iterations, position):
    steps = data.splitlines()
    steps.reverse()

    operations = []
    for step in steps:
        if step.startswith("deal into new stack"):
            operations.append((0, None))
        elif step.startswith("cut"):
            operations.append((1, int(step.split(" ")[1])))
        elif step.startswith("deal with increment"):
            increment = int(step.split(" ")[3])

            steps = _calculate_mod_inverse(increment, size)

            operations.append((2, steps))

    for i in range(iterations):
        for what, info in operations:
            if what == 0:
                position = size - position - 1
            elif what == 1:

                needed_position = (position + info)
                if needed_position < 0:
                    needed_position = size + needed_position
                if needed_position > size:
                    needed_position = needed_position % size
                position = needed_position

            elif what == 2:

                position = (position + (position * info)) % size

    return position


def _calculate_mod_inverse(increment, size):
    pos = 0
    steps = 0
    while pos != 1:
        safe_steps = size - pos

        if safe_steps > increment:
            to_take = safe_steps // increment
            pos += to_take * increment
            steps += to_take
        else:
            pos += increment
            pos = pos % size
            steps += 1
    steps -= 1
    return steps


def apply_operation(operations, addi, multi, size):
    operation = operations.popleft()

    if len(operations):
        addi, multi = apply_operation(operations, addi, multi, size)

    if operation[-2] == "cut":
        addi += int(operation[-1]) * multi
    elif operation[-1] == "stack":
        multi *= -1
        addi += multi
    else:
        multi *= modinv(int(operation[-1]), size)

    return addi, multi


def solve_by_others(data):
    operations = deque(reversed([line.split(" ") for line in data]))

    position = 2020
    size = 119315717514047
    iterations = 101741582076661

    addi, multi = apply_operation(operations, 0, 1, size)

    all_multi = pow(multi, iterations, size)
    all_addi = addi * (1 - pow(multi, iterations, size)) * modinv(1 - multi, size)

    return (position * all_multi + all_addi) % size


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


if __name__ == '__main__':

    print(part1("deal with increment 1", 10))  # 0 voor 1
    print(part1("deal with increment 11", 10))  # 0 voor 11
    print(part1("deal with increment 11", 10))  # 0 voor 21

    print(part1("deal with increment 49", 10))  # 8 voor 49
    print(part1("deal with increment 9", 10))  # 8 voor 9
    print(part1("deal with increment 19", 10))  # 8 voor 19

    print(part1("deal with increment 17", 10))  # 2 voor 17
    print(part1("deal with increment 7", 10))  # 2 voor 7

    print(part1("deal with increment 13", 10))  # 6 voor 13
    print(part1("deal with increment 3", 10))  # 6 voor 3

    assert part1("deal with increment 3", 10) == [0, 7, 4, 1, 8, 5, 2, 9, 6, 3]
    assert part1("cut -4", 10) == [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
    assert part1(test_1, 10) == [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]
    assert part1(test_2, 10) == [3, 0, 7, 4, 1, 8, 5, 2, 9, 6]
    assert part1(test_3, 10) == [6, 3, 0, 7, 4, 1, 8, 5, 2, 9]

    assert part2("cut -4", 10, 1, 5) == 1
    assert part2("cut -4", 10, 1, 4) == 0
    assert part2("cut -4", 10, 1, 3) == 9

    assert part2("deal into new stack", 10, 1, 9) == 0
    assert part2("deal into new stack", 10, 1, 6) == 3
    assert part2("deal into new stack", 10, 1, 5) == 4
    assert part2("deal into new stack", 10, 1, 4) == 5
    assert part2("deal into new stack", 10, 1, 3) == 6
    assert part2("deal into new stack", 10, 1, 0) == 9

    assert part2("deal with increment 3", 10, 1, 0) == 0  # 6 voor 3
    assert part2("deal with increment 3", 10, 1, 3) == 1
    assert part2("deal with increment 3", 10, 1, 6) == 2
    assert part2("deal with increment 3", 10, 1, 9) == 3
    assert part2("deal with increment 3", 10, 1, 1) == 7
    assert part2("deal with increment 3", 10, 1, 2) == 4
    assert part2("deal with increment 3", 10, 1, 4) == 8
    assert part2("deal with increment 3", 10, 1, 5) == 5
    assert part2("deal with increment 3", 10, 1, 7) == 9

    assert part2(test_1, 10, 1, 0) == 0
    assert part2(test_1, 10, 1, 1) == 3
    assert part2(test_1, 10, 1, 2) == 6
    assert part2(test_1, 10, 1, 3) == 9

    assert part2(test_3, 10, 1, 0) == 6
    assert part2(test_3, 10, 1, 1) == 3
    assert part2(test_3, 10, 1, 2) == 0
    assert part2(test_3, 10, 1, 3) == 7

    with open('input') as f:
        data = f.read()

    print(part1(data, 10007).index(2019))
    # print(part2(data, 119315717514047, 101741582076661, 2020))

    print(solve_by_others(data.splitlines()))
