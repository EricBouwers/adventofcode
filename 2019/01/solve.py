#!/usr/bin/env python

import sys


def fuel(mass):
    return int((int(mass) / 3)) - 2


def rec_fuel(mass):
    total = 0
    new_fuel = fuel(mass)
    while new_fuel > 0:
        total += new_fuel
        new_fuel = fuel(new_fuel)

    return total


def total_fuel(mass_list):
    return sum(map(fuel, mass_list))


def total_rec_fuel(mass_list):
    return sum(map(rec_fuel, mass_list))


if __name__ == '__main__':
    
    assert fuel("12") == 2
    assert fuel("14") == 2
    assert fuel("1969") == 654
    assert fuel("100756") == 33583

    assert rec_fuel("12") == 2
    assert rec_fuel("1969") == 966
    assert rec_fuel("100756") == 50346

    with open(sys.argv[1]) as f:
        input_lines = f.readlines()

    print(total_fuel(input_lines))
    print(total_rec_fuel(input_lines))

