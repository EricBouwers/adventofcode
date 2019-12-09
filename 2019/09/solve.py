#!/usr/bin/env python

import sys
import int_code_comp

test_1 = """109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"""
test_2 = """1102,34915192,34915192,7,4,7,99,0"""
test_3 = """104,1125899906842624,99"""
test_4 = """"""


def part1(data):
    int_code_comp.intcode_comp([int(x) for x in data.split(",")], [1])


def part2(data):
    int_code_comp.intcode_comp([int(x) for x in data.split(",")], [2])


if __name__ == '__main__':

    # int_code_comp.intcode_comp([int(x) for x in test_1.split(",")], [])
    # int_code_comp.intcode_comp([int(x) for x in test_2.split(",")], [])
    # int_code_comp.intcode_comp([int(x) for x in test_3.split(",")], [])

    with open('input') as f:
        data = f.readlines()

    part1(data[0])
    part2(data[0])

