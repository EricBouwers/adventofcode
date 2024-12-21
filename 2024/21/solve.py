#!/usr/bin/env python

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
    '1': {'A': '>>vA', '0': '>vA', '1': 'A', '2': '>A', '3': '>>A', '4': '^A', '5': '>^A', '6': '>>^A', '7': '^^A', '8': '>^^A', '9': '>>^^A'},
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
    'v': {'A': '>^A', '<': '<A', '>': '>A', 'v': 'A', '^': '^A'},
    '<': {'A': '>>^A', '<': 'A', '>': '>>A', 'v': '>A', '^': '>^A'},
    '>': {'A': '^A', '<': '<<A', '>': 'A', 'v': '<A', '^': '<^A'},
    '^': {'A': '>A', '<': 'v<A', '>': 'v>A', 'v': 'vA', '^': 'A'}
}

for k, v in KEYPAD_MAP.items():
    for k2, v2 in v.items():
        if not v2.endswith('A'):
            print(k, k2)

for k, v in DIRPAD_MAP.items():
    for k2, v2 in v.items():
        if not v2.endswith('A'):
            print(k, k2)


def get_num_keypad_sequence(code, current):
    if code:
        return KEYPAD_MAP[current][code[0]] + get_num_keypad_sequence(code[1:], code[0])
    else:
        return ''


def get_dir_keypad_sequence(sequence, current):
    if sequence:
        return DIRPAD_MAP[current][sequence[0]] + get_dir_keypad_sequence(sequence[1:], sequence[0])
    else:
        return ''


def get_sequence(code, recursion=2):
    keypad_sequence = get_num_keypad_sequence(code, 'A')
    dir_sequence = get_dir_keypad_sequence(keypad_sequence, 'A')
    for x in range(recursion-1):
        dir_sequence = get_dir_keypad_sequence(dir_sequence, 'A')
        print(dir_sequence)

    return dir_sequence


def part1(data):
    codes = parse_data(data)

    complexity = 0
    for code in codes:
        sequence = get_sequence(code)
        complexity += int("".join([c for c in code if c.isdigit()])) * len(sequence)

    return complexity


def part2(data):
    codes = parse_data(data)

    complexity = 0
    for code in codes:
        sequence = get_sequence(code, 25)
        complexity += int("".join([c for c in code if c.isdigit()])) * len(sequence)

    return complexity


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 126384
    assert part2(test_1.splitlines()) == None

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))


