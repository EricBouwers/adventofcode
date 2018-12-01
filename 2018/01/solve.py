#!/usr/bin/env python

import sys

def recalibrate(freqs):
    return eval("0" + freqs.replace(", "," "))

def recalibrate_twice(freqs):
    freqs = [int(x) for x in freqs.split(", ")]
    len_freqs = len(freqs)
    current, index = (0,0)
    seen_freqs = set() 

    while current not in seen_freqs:
        seen_freqs.add(current)
        current += freqs[index]
        index = (index + 1) % len_freqs

    return current


if __name__ == '__main__':
    
    assert recalibrate("+1, +1, +1") == 3
    assert recalibrate("-1, -2, -3") == -6
    
    assert recalibrate_twice("+1, -1") == 0
    assert recalibrate_twice("+3, +3, +4, -2, -4") == 10
    assert recalibrate_twice("-6, +3, +8, +5, -6") == 5
    assert recalibrate_twice("+7, +7, -2, -7, -4") == 14

    print recalibrate(sys.argv[1])
    print recalibrate_twice(sys.argv[1])

