#!/usr/bin/env python
import operator

test_1 = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""
test_2 = """"""


def parse_data(data):
    return {
        d.split(": ")[0] : d.split(": ")[1] for d in data
    }


OPS_TO_OP = {
    "+": operator.add, "-": operator.sub, "/": operator.floordiv, "*": operator.mul
}


def replace_data(parsed, cur_node):
    if " " not in cur_node:
        if parsed[cur_node].isdigit():
            return int(parsed[cur_node])
        else:
            return replace_data(parsed, parsed[cur_node])
    else:
        left, op, right = cur_node.split(" ")
        return OPS_TO_OP[op](replace_data(parsed, left), replace_data(parsed, right))


def part1(data):
    parsed = parse_data(data)

    root = parsed['root']
    return replace_data(parsed, root)


def part2(data, op=operator.gt):
    parsed = parse_data(data)

    root = parsed['root']
    left, _, right = root.split(" ")

    right_num = int(replace_data(parsed, right))
    max_i = i = right_num * 10000
    left_num = right_num * 2

    while left_num != right_num:
        if op(left_num,right_num):
            i = i + int((max_i - i) / 2)
        else:
            max_i = i
            i = int(i / 2)
        parsed['humn'] = str(i)
        left_num = int(replace_data(parsed, left))

        print(max_i, i, left_num, right_num, int(replace_data(parsed, right)))

    while left_num == right_num:
        i -= 1
        parsed['humn'] = str(i)
        left_num = int(replace_data(parsed, left))

    return i+1


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 152
    assert part2(test_1.splitlines(), op=operator.lt) == 301

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

