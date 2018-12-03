#!/usr/bin/env python

import sys, re

def create_fabric(claims, size):
    fabric = [[None]*size for _ in range(0,size)]
    
    for claim in claims.split("\n"):
        claim = map(int, re.findall('[0-9]+', claim))
        for x in range(claim[1], claim[1]+ claim[3]):
            for y in range(claim[2], claim[2] + claim[4]):
                if fabric[y][x] is None:
                    fabric[y][x] = [claim[0]]
                else:
                    fabric[y][x].append(claim[0])

    return fabric


def overlaps(claims, size):
    fabric = create_fabric(claims, size)
    overlaps = 0

    for r in fabric:
        for c in r:
            overlaps += 1 if c is not None and len(c) > 1 else 0

    return overlaps        

def intact(claims, size):
    fabric = create_fabric(claims, size)
    intact = [True] * len(claims.split("\n"))

    for r in fabric:
        for c in r:
            if c is not None and len(c) > 1:
                for cl in c:
                    intact[cl-1] = False

    return intact.index(True) + 1



if __name__ == '__main__':

    assert overlaps("#1 @ 1,3: 4x4\n#2 @ 3,1: 4x4\n#3 @ 5,5: 2x2", 8) == 4
    assert intact("#1 @ 1,3: 4x4\n#2 @ 3,1: 4x4\n#3 @ 5,5: 2x2", 8) == 3

    print overlaps(sys.argv[1], 1000)
    print intact(sys.argv[1], 1000)

