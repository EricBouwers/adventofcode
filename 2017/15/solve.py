#!/usr/bin/env python

import sys
import itertools


def genX(x, max_i, step, modulo=None):
    i = 0
    while i < max_i:
        x = (x * step) % 2147483647

        if modulo:
            while x % modulo != 0:
                x = (x * step) % 2147483647
        
        yield x
        i += 1

        if i % 1000000 == 0:
            print i


def final_count(starta, startb):
    count_one = 0
    count_two = 0
    mask = (1 << 16) - 1

    for a, b in itertools.izip(genX(starta, 40000000, 16807), genX(startb, 40000000, 48271)):
        if (a & mask) == (b & mask):
            count_one += 1
    
    for a, b in itertools.izip(genX(starta, 5000000, 16807, 4), genX(startb, 5000000, 48271, 8)):
        if (a & mask) == (b & mask):
            count_two += 1

    return count_one, count_two


if __name__ == '__main__':
    
    assert final_count(65l, 8921l) == (588, 309)

    print final_count(289l, 629l)

