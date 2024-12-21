#!/usr/bin/env python
from collections import defaultdict

test_1 = """029A
980A
179A
456A
379A
"""
test_2 = """"""


def parse_data(data):
    return data


KEYPAD_MAP = {
    'A': {'A': 'A', '0': '<A', '1': '^<<A', '2': '<^A', '3': '^A', '4': '^^<<A', '5': '<^^A', '6': '^^A', '7': '^^^<<A', '8': '<^^^A', '9': '^^^A'},
    '0': {'A': '>A', '0': 'A', '1': '^<A', '2': '^A', '3': '>^A', '4': '<^^A', '5': '^^A', '6': '>^^A', '7': '<^^^A', '8': '^^^A', '9': '>^^^A'},
    '1': {'A': '>>vA', '0': '>vA', '1': 'A', '2': '>A', '3': '>>A', '4': '^A', '5': '>^A', '6': '^>>A', '7': '^^A', '8': '>^^A', '9': '>>^^A'},
    '2': {'A': 'v>A', '0': 'vA', '1': '<A', '2': 'A', '3': '>A', '4': '<^A', '5': '^A', '6': '>^A', '7': '<^^A', '8': '^^A', '9': '>^^A'},
    '3': {'A': 'vA', '0': '<vA', '1': '<<A', '2': '<A', '3': 'A', '4': '<<^A', '5': '<^A', '6': '^A', '7': '<<^^A', '8': '<^^A', '9': '^^A'},
    '4': {'A': '>>vvA', '0': '>vvA', '1': 'vA', '2': 'v>A', '3': 'v>>A', '4': 'A', '5': '>A', '6': '>>A', '7': '>^A', '8': '>>^A', '9': '>>>^A'},
    '5': {'A': 'vv>A', '0': 'vvA', '1': '<vA', '2': 'vA', '3': 'v>A', '4': '<A', '5': 'A', '6': '>A', '7': '<^A', '8': '^A', '9': '>^A'},
    '6': {'A': 'vvA', '0': '<vvA', '1': '<<vA', '2': '<vA', '3': 'vA', '4': '<<A', '5': '<A', '6': 'A', '7': '<<^A', '8': '<^A', '9': '^A'},
    '7': {'A': '>>vvvA', '0': '>vvvA', '1': 'vvA', '2': 'vv>A', '3': 'vv>>A', '4': 'vA', '5': 'v>A', '6': 'v>>A', '7': 'A', '8': '>A', '9': '>>A'},
    '8': {'A': 'vvv>A', '0': 'vvvA', '1': '<vvA', '2': 'vvA', '3': 'v>A', '4': '<vA', '5': 'vA', '6': 'v>A', '7': '<A', '8': 'A', '9': '>A'},
    '9': {'A': 'vvvA', '0': '<vvvA', '1': '<<vvA', '2': '<vvA', '3': 'vvA', '4': '<<vA', '5': '<vA', '6': 'vA', '7': '<<A', '8': '<A', '9': 'A'},
}


DIRPAD_MAP = {
    'A': {'A': 'A', '<': 'v<<A', '>': 'vA', 'v': '<vA', '^': '<A'},
    'v': {'A': '^>A', '<': '<A', '>': '>A', 'v': 'A', '^': '^A'},
    '<': {'A': '>>^A', '<': 'A', '>': '>>A', 'v': '>A', '^': '>^A'},
    '>': {'A': '^A', '<': '<<A', '>': 'A', 'v': '<A', '^': '<^A'},
    '^': {'A': '>A', '<': 'v<A', '>': 'v>A', 'v': 'vA', '^': 'A'}
}


def get_num_keypad_sequence(code, current='A'):
    if code:
        return KEYPAD_MAP[current][code[0]] + get_num_keypad_sequence(code[1:], code[0])
    else:
        return ''


def get_simple_dir_keypad_sequence(sequence, current='A'):
    if sequence:
        return DIRPAD_MAP[current][sequence[0]] + get_simple_dir_keypad_sequence(sequence[1:], sequence[0])
    else:
        return ''


def split_in_discrete_blocks(sequence):
    blocks = defaultdict(lambda: 0)
    for s in sequence.split('A'):
        blocks[s + 'A'] += 1
    blocks['A'] -= 1
    return blocks


def get_dir_keypad_sequence(sequences):
    result = defaultdict(lambda: 0)
    for sequence, count in sequences.items():
        dir_sequence = get_simple_dir_keypad_sequence(sequence)
        for b, c in split_in_discrete_blocks(dir_sequence).items():
            result[b] += count * c

    return result


def get_sequence(code, recursion=2):
    keypad_sequence = get_num_keypad_sequence(code)
    dir_sequence = get_simple_dir_keypad_sequence(keypad_sequence)
    dir_sequences = split_in_discrete_blocks(dir_sequence)

    for x in range(recursion - 1):
        dir_sequences = get_dir_keypad_sequence(dir_sequences)

    return dir_sequences


def part1(data, recursion=2):
    codes = parse_data(data)

    complexity = 0
    for code in codes:
        sequences = get_sequence(code, recursion)
        complexity += int("".join([c for c in code if c.isdigit()])) * sum([len(k) * v for k, v in sequences.items()])

    return complexity


def part2(data):
    return part1(data, recursion=25)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 126384
    assert part2(test_1.splitlines()) > 0

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))


# too high 132929214388818, 117045327454816
# too low 53103927712042