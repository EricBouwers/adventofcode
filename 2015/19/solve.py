#!/usr/bin/env python
from collections import defaultdict

test_1 = """H => HO
H => OH
O => HH

HOH
"""
test_2 = """H => HO
H => OH
O => HH

HOHOHO
"""
test_3 = """HO => s

HOH
"""
test_4 = """e => H
e => O
H => HO
H => OH
O => HH

HOH
"""
test_5 = """e => H
e => O
H => HO
H => OH
O => HH

HOHOHO
"""

def parse_data(data):
    replacements = defaultdict(list)
    start = None
    for line in data:
        if line:
            parts = line.split(' => ')
            if len(parts) == 1:
                start = parts[0]
            else:
                replacements[parts[0]].append(parts[1])

    return replacements, start

def get_new_molecules(replacements, start):
    molecules = set()

    for i, c in enumerate(start):
        seen = start[0:i]
        to_check = start[i:]
        for k, rs in replacements.items():
            if to_check.startswith(k):
                for r in rs:
                    molecules.add(seen + r + to_check[len(k):])

    return molecules

def get_new_molecules_backwards(replacements, start):
    molecules = set()

    for i, c in enumerate(start):
        seen = start[0:i]
        to_check = start[i:]
        for k, rs in replacements.items():
            for r in rs:
                if to_check.startswith(r):
                    molecules.add(seen + k + to_check[len(r):])

    return molecules

def part1(data):
    replacements, start = parse_data(data)
    molecules = get_new_molecules(replacements, start)
    return len(molecules)

def part2(data):
    replacements, start = parse_data(data)

    states = [(start, 0)]
    target = 'e'
    seen_molecules = set()
    while states:
        cur_mol, steps = states.pop(0)

        if cur_mol == target:
            return steps
        else:
            for m in get_new_molecules_backwards(replacements, cur_mol):
                if len(m) > 0 and m not in seen_molecules:
                    seen_molecules.add(m)
                    states.append((m, steps+1))

            states.sort(key=lambda x: len(x[0]))


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 4
    assert part1(test_2.splitlines()) == 7
    assert part1(test_3.splitlines()) == 1
    assert part2(test_4.splitlines()) == 3
    assert part2(test_5.splitlines()) == 6

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
