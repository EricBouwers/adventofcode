#!/usr/bin/env python
from collections import defaultdict
from functools import reduce

test_1 = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""
test_2 = """"""


def parse_data(data):
    return data[0].split(',')


def ascii_hash(s):
    return reduce(lambda cv, c: (cv + ord(c)) * 17 % 256, s, 0)


def part1(data):
    parsed = parse_data(data)
    return sum(map(ascii_hash, parsed))


def part2(data):
    lenses = parse_data(data)
    boxes = defaultdict(lambda: [])

    for lens in lenses:
        label = lens[0:-1] if lens[-1] == '-' else lens.split("=")[0]
        label_hash = ascii_hash(label)
        box_lenses = boxes[label_hash]

        if '-' in lens:
            boxes[label_hash] = [l for l in box_lenses if l[0] != label]
        else:
            fl = int(lens.split("=")[1])
            if label in [l[0] for l in box_lenses]:
                boxes[label_hash] = [(l[0], l[1] if l[0] != label else fl) for l in box_lenses]
            else:
                box_lenses.append((label, fl))

    return sum([sum([(box+1) * (i+1) * l[1] for i, l in enumerate(lenses)]) for box, lenses in boxes.items()])


if __name__ == '__main__':

    assert ascii_hash("HASH") == 52
    assert part1(test_1.splitlines()) == 1320
    assert part2(test_1.splitlines()) == 145

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

