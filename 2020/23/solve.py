#!/usr/bin/env python
import cProfile
from collections import deque

test_1 = """389125467"""
test_3 = """"""
test_4 = """"""


def shuffle_cups_deque(cups, moves, max_cup):
    for m in range(moves):
        current_cup = cups.popleft()
        other_cups = [cups.popleft(), cups.popleft(), cups.popleft()]
        other_cups.reverse()

        append_cup = current_cup
        while append_cup == current_cup or append_cup in other_cups:
            append_cup -= 1
            if append_cup == 0:
                append_cup = max_cup

        to_append_index = cups.index(append_cup)
        cups.insert(to_append_index + 1, other_cups[0])
        cups.insert(to_append_index + 1, other_cups[1])
        cups.insert(to_append_index + 1, other_cups[2])

        cups.append(current_cup)

        if m % 1000 == 0:
            print(m)

    return cups


def print_cups_dict(cups_dict):
    lst = []
    cur = list(cups_dict.keys())[0]
    lst.append(cur)
    while cups_dict[cur] not in lst:
        lst.append(cups_dict[cur])
        cur = cups_dict[cur]

    print(''.join([str(c) for c in lst]))


def shuffle_cups_dict(cups, moves, max_cup):
    cups_dict = {}
    first = cups.popleft()
    prev = first
    while cups:
        nxt = cups.popleft()
        cups_dict[prev] = nxt
        prev = nxt

    cups_dict[prev] = first

    current_cup = first
    for m in range(moves):
        next_cups = [cups_dict[current_cup]]
        next_cups.append(cups_dict[next_cups[0]])
        next_cups.append(cups_dict[next_cups[1]])

        cups_dict[current_cup] = cups_dict[next_cups[2]]

        append_cup = current_cup
        while append_cup == current_cup or append_cup in next_cups:
            append_cup -= 1
            if append_cup == 0:
                append_cup = max_cup

        append_cup_nxt = cups_dict[append_cup]

        cups_dict[append_cup] = next_cups[0]
        cups_dict[next_cups[2]] = append_cup_nxt

        current_cup = cups_dict[current_cup]

        if m % 1000000 == 0:
            print(m)

    return cups_dict


def part1(data, moves=100):
    cups = deque([int(c) for c in data[0]])
    max_cup = max(cups)

    cups_dict = shuffle_cups_dict(cups, moves, max_cup)
    lst = []
    cur = 1
    lst.append(cur)
    while cups_dict[cur] not in lst:
        lst.append(cups_dict[cur])
        cur = cups_dict[cur]

    return "".join([str(c) for c in lst[1:]])


def part2(data):
    cups = [int(c) for c in data[0]]
    max_cup = max(cups)

    cups = deque(cups + [x for x in range(max_cup+1, 1000001)])
    cups = shuffle_cups_dict(cups, 10000000, 1000000)

    fst = cups[1]
    snd = cups[fst]
    return str(fst * snd)


if __name__ == '__main__':

    assert part1(test_1.splitlines(), 10) == "92658374"
    assert part1(test_1.splitlines(), 100) == "67384529"
    assert part2(test_1.splitlines()) == "149245887792"

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
