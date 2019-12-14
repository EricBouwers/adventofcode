#!/usr/bin/env python
import math
import sys
from collections import defaultdict

test_1 = """10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL"""
test_2 = """9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL"""
test_3 = """157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"""
test_4 = """2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF"""


def parse_formula(data):
    formulas = {}
    for line in data:
        fr, to = line.split(" => ")

        q, w = to.split(" ")

        needs = []
        for r in fr.split(", "):
            r = r.split(" ")
            r[0] = int(r[0])
            needs.append(r)

        formulas[w] = [int(q), needs]

    return formulas


def part1(data, needed=1):
    formulas = parse_formula(data)

    ores = 0
    still_left = defaultdict(lambda:0)

    needs = [[needed, "FUEL"]]
    while needs:
        how_much, sub_need = needs.pop(0)

        if how_much <= still_left[sub_need]:
            still_left[sub_need] = still_left[sub_need] - how_much
        else:
            if sub_need == "ORE":
                ores += how_much
            else:
                needs = produce_needs(formulas, how_much, needs, still_left, sub_need)

    return ores


def state(state_dict):
    return str(state_dict.items())


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


def part2_failed(data):
    formulas = parse_formula(data)

    ores = 1000000000000
    fuel_produced = 0
    still_left = defaultdict(lambda:0)
    needs = [] + formulas["FUEL"][1]
    seens = defaultdict(dict)
    loops = {}
    looped = False
    while ores > 0:
        if len(needs) == 0:
            fuel_produced += 1
            needs = [] + formulas["FUEL"][1]

            for k, v in still_left.items():
                if k not in loops:
                    sub_states = seens[k]
                    if v in sub_states:
                        old_fuel, old_ores = sub_states[v]

                        iteration_produced = fuel_produced - old_fuel
                        iteration_ores = old_ores - ores

                        loops[k] = [v, iteration_produced, iteration_ores]

            if len(still_left.keys() - loops.keys()) == 0 and not looped:
                total_iterations = None
                state_produced, state_ores, max_produced, max_used = 0, 0, 0, 0
                for k, v in loops.items():
                    k_left, state_produced, state_ores = v

                    diff_produced = state_produced
                    diff_used = state_ores

                    total_iterations = lcm(total_iterations, diff_produced) if total_iterations is not None else diff_produced
                    still_left[k] = k_left

                    max_produced = max(max_produced, diff_produced)
                    max_used = max(max_used, diff_used)

                iteration_produced = total_iterations
                iteration_ores = total_iterations * max_used

                fuel_produced += total_iterations - max_produced
                ores += max_used
                ores -= iteration_ores

                while ores-iteration_ores > 0:
                    fuel_produced += iteration_produced
                    ores -= iteration_ores
                    # print("loop!", ores)
                    looped = True
            else:
                for k, v in still_left.items():
                    if fuel_produced == 1:
                        seens[k][v] = [fuel_produced, ores]

        how_much, sub_need = needs.pop(0)

        if how_much <= still_left[sub_need]:
            still_left[sub_need] = still_left[sub_need] - how_much
        else:
            if sub_need == "ORE":
                ores -= how_much
            else:
                needs = produce_needs(formulas, how_much, needs, still_left, sub_need)

    return fuel_produced


def produce_needs(formulas, how_much, needs, still_left, sub_need):
    how_much = how_much - still_left[sub_need]
    still_left[sub_need] = 0
    can_get, my_needs = formulas[sub_need]

    i = math.ceil(how_much/can_get)

    left_over = i * can_get - how_much
    still_left[sub_need] += left_over
    needs = needs + [[i * n[0], n[1]] for n in my_needs]

    return needs


def part2_slow(data):
    formulas = parse_formula(data)

    ores = 1000000000000
    fuel_produced = 0
    still_left = defaultdict(lambda:0)
    needs = [] + formulas["FUEL"][1]
    seens = {}
    while ores > 0:
        if len(needs) == 0:
            fuel_produced += 1
            needs = [] + formulas["FUEL"][1]

            state_key = state(still_left)
            if state_key in seens:
                old_fuel, old_ores = seens[state_key]

                iteration_produced = fuel_produced - old_fuel
                iteration_ores = old_ores - ores

                while ores-iteration_ores > 0:
                    fuel_produced += iteration_produced
                    ores -= iteration_ores
                    # print("loop!", ores)
            else:
                seens[state_key] = [fuel_produced, ores]

        how_much, sub_need = needs.pop(0)

        if how_much <= still_left[sub_need]:
            still_left[sub_need] = still_left[sub_need] - how_much
        else:
            if sub_need == "ORE":
                ores -= how_much
            else:
                needs = produce_needs(formulas, how_much, needs, still_left, sub_need)

    return fuel_produced


def part2_others(data):
    have_ore = 1000000000000
    min_f = have_ore//part1(data, 1)
    max_f = 2*min_f
    while max_f > min_f+1:
        prod_fuel = (min_f + max_f) // 2
        if part1(data, prod_fuel) > have_ore:
            max_f = prod_fuel
        else:
            min_f = prod_fuel

    return min_f


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 31
    assert part1(test_2.splitlines()) == 165
    assert part1(test_3.splitlines()) == 13312
    assert part1(test_4.splitlines()) == 180697
    assert part2_slow(test_3.splitlines()) == 82892753
    assert part2_others(test_3.splitlines()) == 82892753
    assert part2_slow(test_3.splitlines()) == 82892753
    assert part2_slow(test_4.splitlines()) == 5586022

    print("done testing")

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    # print(part2_slow(data.splitlines()))
    print(part2_others(data.splitlines()))

