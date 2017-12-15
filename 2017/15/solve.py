#!/usr/bin/env python

import sys


def final_count(a, b):
    count = 0
    mask = (1 << 16) - 1

    for i in xrange(0, 40000000):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647
       
        if (a & mask) == (b & mask):
            count += 1

    return count


if __name__ == '__main__':
    
    assert final_count(65l, 8921l) == 588

    print final_count(289l, 629l)

