#!/usr/bin/env python

import sys
from collections import defaultdict

test_1 = """123456789012"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def part1(data, wide=25, tall=6):
    data = list(data)
    layers = []

    while data:
        layer = {}
        for h in range(tall):
            for w in range(wide):
                next_val = int(data.pop(0))
                layer[next_val] = layer[next_val] + 1 if next_val in layer else 1
        layers.append(layer)

    min_layer = layers[0]
    for layer in layers:
        min_layer = min_layer if min_layer[0] < layer[0] else layer

    return min_layer[1] * min_layer[2]


def get_pixel(w, h, layers):
    for l in layers:
        if l[(w, h)] != 2:
            return l[(w, h)]


def part2(data, wide=25, tall=6):
    data = list(data)
    layers = []

    while data:
        layer = {}
        for h in range(tall):
            for w in range(wide):
                layer[(w, h)] = int(data.pop(0))
        layers.append(layer)

    for h in range(tall):
        line = ""
        for w in range(wide):
            color = get_pixel(w, h, layers)
            line += " " if color == 0 else "*"
        print(line)


if __name__ == '__main__':

    with open('input') as f:
        data = f.readlines()

    print(part1(data[0]))
    part2("0222112222120000", 2, 2)
    part2(data[0])

