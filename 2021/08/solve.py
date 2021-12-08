#!/usr/bin/env python

test_1 = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def part1(data):
    total = 0
    for l in data:
        outputs = l.split(" | ")[1]
        total += len([d for d in outputs.split(" ") if len(d) in [2, 3, 4, 7]])

    return total


DIGITS_TO_SEGMENT = {
    0: [0, 1, 2, 4, 5, 6],
    1: [2, 5],
    2: [0, 2, 3, 4, 6],
    3: [0, 2, 3, 5, 6],
    4: [1, 2, 3, 5],
    5: [0, 1, 3, 5, 6],
    6: [0, 1, 3, 4, 5, 6],
    7: [0, 2, 5],
    8: [0, 1, 2, 3, 4, 5, 6],
    9: [0, 1, 2, 3, 5, 6]
}

SEGMENT_TO_DIGITS = {
    tuple(sorted(v)): k for k, v in DIGITS_TO_SEGMENT.items()
}


def filter_mapping(d, s, mapping):
    d = [x for x in d]
    for m in mapping.keys():
        if m in DIGITS_TO_SEGMENT[s]:
            mapping[m] = [m for m in mapping[m] if m in d]
        else:
            mapping[m] = [m for m in mapping[m] if m not in d]


def deduce_mapping(line):
    mapping = {x: ['a', 'b', 'c', 'd', 'e', 'f', 'g'] for x in range(0, 7)}
    digits = sorted(line.split(" "), key=len)

    for d, s in [[0, 1], [1, 7], [2, 4]]:
        filter_mapping(digits[d], s, mapping)

    # find the five
    possible_letters = set().union(*[mapping[0], mapping[5]])
    for d in digits:
        if len(d) == 5 and set(possible_letters) <= set(d):
            d = [d for d in d]
            mapping[6] = [m for m in mapping[6] if m in d]
            for x in range(0, 6):
                mapping[x] = [m for m in mapping[x] if m != mapping[6][0]]

    # find the three
    possible_letters = set().union(*[mapping[0], mapping[5], mapping[6]])
    for d in digits:
        if len(d) == 5 and set(possible_letters) <= set(d):
            d = [d for d in d]
            mapping[3] = [m for m in mapping[3] if m in d]
            for x in [0, 1, 2, 4, 5, 6]:
                mapping[x] = [m for m in mapping[x] if m != mapping[3][0]]

    # find the two
    possible_letters = set().union(*[mapping[0], mapping[3], mapping[4], mapping[6]])
    for d in digits:
        if len(d) == 5 and set(possible_letters) <= set(d):
            d = [d for d in d]
            mapping[2] = [m for m in mapping[2] if m in d]
            for x in [0, 1, 3, 4, 5, 6]:
                mapping[x] = [m for m in mapping[x] if m != mapping[2][0]]

    return {mapping[k][0]: k  for k in mapping.keys()}


def map_number(mapping, digit):
    segments = [mapping[d] for d in digit]
    return str(SEGMENT_TO_DIGITS[tuple(sorted(segments))])


def part2(data):
    total = 0
    for l in data:
        mapping = deduce_mapping(l.split(" | ")[0])
        total += int(''.join([map_number(mapping, d) for d in l.split(" | ")[1].split(" ")]))

    return total


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 26
    assert part2(test_1.splitlines()) == 61229

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

