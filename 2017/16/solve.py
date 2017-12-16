#!/usr/bin/env python

import sys
from collections import deque


def dance(p, ins):
    p = list(p)
    for i in ins.split(","):
        if i[0] == "s":
            p = deque(p)
            p.rotate(int(i[1:]))
            p = list(p)
        else:
            parts = i[1:].split("/")
            if i[0] == "x":
                a, b = int(parts[0]), int(parts[1])
            else:
                a, b = p.index(parts[0]), p.index(parts[1])
            p[b], p[a] = p[a], p[b]
    
    return "".join(p)


def many_dance(p, ins):
    seen = []
    while p not in seen:
        seen.append(p)
        p = dance(p, ins)

    moves = len(seen)
    return seen[1000000000 % moves]

if __name__ == '__main__':
    
    assert dance("abcde", "s1,x3/4,pe/b") == "baedc"
    print dance("abcdefghijklmnop", sys.argv[1])
    print many_dance("abcdefghijklmnop", sys.argv[1])


