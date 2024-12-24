#!/usr/bin/env python
import operator
from copy import deepcopy

test_1 = """x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02
"""
test_2 = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
"""
test_3 = """x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z05
x01 AND y01 -> z02
x02 AND y02 -> z01
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z00
"""


def parse_data(data):
    values = {}
    gates = {}
    for line in data:
        if ' -> ' in line:
            parts = line.split(' -> ')
            variables = [parts[0][0:3], parts[0][-3:]]
            op = operator.ne if "XOR" in line else operator.or_ if 'OR' in line else operator.and_
            gates[parts[1]] = (op, variables)
        elif line:
            parts = line.split(': ')
            values[parts[0]] = True if parts[1] == '1' else False

    return values, gates


def calculate_value(v, values, grid):
    if v in values:
        return values[v]
    else:
        op, to_calc = grid[v]
        return op(calculate_value(to_calc[0], values, grid), calculate_value(to_calc[1], values, grid))


def calculate_values(values, grid):
    for v in grid.keys():
        if v not in values:
            values[v] = calculate_value(v, values, grid)

    return values


def find_number(values, size=1000000):
    keys = sorted([v for v in values if v.startswith('z')], reverse=True)
    return int(''.join(['1' if values[k] else '0' for k in keys])[-size:], 2)


def part1(data):
    values, gates = parse_data(data)
    values = calculate_values(values, gates)

    return find_number(values)


def print_gate(name, gates):
    if name[0] in 'xy':
        return name
    else:
        op, sides = gates[name]
        sides.sort()
        return ('(' + print_gate(sides[0], gates) + ') ' +
                ('XOR' if op == operator.ne else 'OR' if op == operator.or_ else 'AND') +
                ' (' + print_gate(sides[1], gates) + ')')


def collect_gates(name, gates):
    if name[0] in 'xy':
        return {name}
    else:
        op, sides = gates[name]
        return collect_gates(sides[0], gates).union(collect_gates(sides[1], gates)).union({name})


def part2(data):
    values, gates = parse_data(data)

    old = gates['z11']
    gates['z11'] = gates['rpv']
    gates['rpv'] = old

    old = gates['rpb']
    gates['rpb'] = gates['ctg']
    gates['ctg'] = old

    old = gates['dmh']
    gates['dmh'] = gates['z31']
    gates['z31'] = old

    old = gates['dvq']
    gates['dvq'] = gates['z38']
    gates['z38'] = old

    for n in range(1, 46):
        n_x = f'{2 ** (n-1):045b}'
        n_y = f'{2 ** (n-1):045b}'
        new_values = {}
        for i, x in enumerate(n_x):
            new_values[f'x{44 - i:02}'] = x == '1'
        for i, y in enumerate(n_y):
            new_values[f'y{44 - i:02}'] = y == '1'

        new_values = calculate_values(new_values, gates)
        new_number = find_number(new_values, n+1)
        if new_number != 2 ** n:
            print(n, new_number, 2 ** n)

    new_gates = deepcopy(gates)
    to_check = collect_gates('z12', gates).difference(collect_gates('z11', gates))
    for f in [x for x in to_check if x[0] not in 'xy']:
        for t in gates.keys():

            gates = deepcopy(new_gates)
            old = gates[f]
            gates[f] = gates[t]
            gates[t] = old

            n_x = f'{2**10:045b}'
            n_y = f'{2**10:045b}'
            new_values = {}
            for i, x in enumerate(n_x):
                new_values[f'x{44 - i:02}'] = x == '1'
            for i, y in enumerate(n_y):
                new_values[f'y{44 - i:02}'] = y == '1'

            try:
                new_values = calculate_values(new_values, gates)
                number = find_number(new_values, 12)
                if number == 2**11 and t != f:
                    print(f, t)

            except:
                pass

    return ','.join(sorted(['rpv', 'z11', 'ctg', 'rpb', 'z31', 'dmh', 'z38', 'dvq']))

if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 4
    assert part1(test_2.splitlines()) == 2024

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

