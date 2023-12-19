#!/usr/bin/env python
import json
from operator import gt, lt

test_1 = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""
test_2 = """"""


def parse_data(data):
    ins = {}
    parts = []

    for line in data:
        if line and line[0] == '{':
            parts.append(json.loads(line.replace('=', ':').replace('{', '{"').replace(',', ',"').replace(':', '":')))
        elif line:
            name, body = line.split('{')
            body_ins = []
            for i in body[:-1].split(','):
                if ':' in i:
                    cond, goto = i[2:].split(':')
                    body_ins.append((i[0], lt if i[1] == '<' else gt, int(cond), goto))
                else:
                    body_ins.append((None, None, None, i))
            ins[name] = body_ins

    return ins, parts


def test_part(part, instructions):
    label, idx = 'in', 0

    while label not in 'AR':
        prop, check, cond, goto = instructions[label][idx]
        if prop is not None:
            if check(part[prop], cond):
                label, idx = goto, 0
            else:
                label, idx = label, idx+1
        else:
            label, idx = goto, 0

    return label


def part1(data):
    ins, parts = parse_data(data)
    accepted = [p for p in parts if test_part(p, ins) == 'A']
    return sum([sum(p.values()) for p in accepted])


def combine_ranges(range_map1, range_map2):
    return [range_map1, range_map2]


def split_ranges(range_list, check, cond):
    new_ranges = []
    for lower, upper in range_list:
        if check == lt:
            if upper < cond:
                new_ranges.append((lower, upper))
            elif lower < cond < upper:
                new_ranges.append((lower, cond-1))
        elif check == gt:
            if lower > cond:
                new_ranges.append((lower, upper))
            elif lower < cond < upper:
                new_ranges.append((cond+1, upper))

    return new_ranges


def find_paths(label, idx, instructions):
    if label == 'A':
        return [{'x': [(1, 4000)], 'm': [(1, 4000)], 'a': [(1, 4000)], 's': [(1, 4000)]}]
    elif label == 'R':
        return [{'x': [], 'm': [], 'a': [], 's': []}]
    else:
        prop, check, cond, goto = instructions[label][idx]
        if prop is not None:
            true_paths = find_paths(goto, 0, instructions)
            false_paths = find_paths(label, idx+1, instructions)

            for true_path in true_paths:
                true_path[prop] = split_ranges(true_path[prop], check, cond)

            for false_path in false_paths:
                false_path[prop] = split_ranges(false_path[prop], lt if check == gt else gt, cond + (1 if check == gt else -1))

            return true_paths + false_paths
        else:
            return find_paths(goto, 0, instructions)


def part2(data):
    ins, _ = parse_data(data)

    paths = find_paths('in', 0, ins)

    options = 0
    for p in paths:
        path_options = 1
        for k, v in p.items():
            char_options = 0
            for lower, upper in v:
                char_options += (upper - lower + 1)
            path_options *= char_options
        options += path_options

    return options


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 19114
    assert part2(test_1.splitlines()) == 167409079868000

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

