#!/usr/bin/env python
from functools import reduce
from operator import mul

test_1 = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""
test_2 = """"""


def parse_data(data):
    monkeys = []
    monkey = {}

    for d in data:
        if d.startswith('  Starting items: '):
            monkey['items'] = [int(x) for x in d[len('  Starting items: '):].split(", ")]
        elif d.startswith('  Test: divisible by '):
            monkey['divby'] = int(d[len('  Test: divisible by '):])
        elif d.startswith('    If true: throw to monkey '):
            monkey['t'] = int(d[len('    If true: throw to monkey '):])
        elif d.startswith('    If false: throw to monkey '):
            monkey['f'] = int(d[len('    If false: throw to monkey '):])
        elif d.startswith('  Operation: new ='):
            operation = d[len('  Operation: new = '):]
            if operation == 'old * old':
                monkey['update'] = lambda x: x*x
            else:
                i = int(operation[len('old * '):])
                if operation.startswith('old *'):
                    monkey['update'] = lambda x, y=i: x * y
                else:
                    monkey['update'] = lambda x, y=i: x + y
        elif d.startswith('Monkey '):
            if monkey:
                monkeys.append(monkey)
            monkey = {}
    monkeys.append(monkey)

    return monkeys


def do_round(data, worry_func, rounds):
    monkeys = parse_data(data)
    inspects = [0] * len(monkeys)

    overall_mod_by = reduce(mul, [m['divby'] for m in monkeys])

    for i in range(0, rounds):
        for m, monkey in enumerate(monkeys):
            while len(monkey['items']) > 0:
                item = monkey['items'].pop(0)
                item = monkey['update'](item)

                item = item % overall_mod_by
                item = worry_func(item)

                if item % monkey['divby'] == 0:
                    monkeys[monkey['t']]['items'].append(item)
                else:
                    monkeys[monkey['f']]['items'].append(item)
                inspects[m] += 1

    inspects = sorted(inspects, reverse=True)
    return inspects[0]*inspects[1]


def part1(data):
    return do_round(data, lambda x: x // 3, 20)


def part2(data):
    return do_round(data, lambda x: x, 10000)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 10605
    assert part2(test_1.splitlines()) == 2713310158

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

