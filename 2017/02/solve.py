#!/usr/bin/env python

import sys
import itertools as it

def do_checksum(sheet):
    return sum(map(lambda x: max(x) - min(x), sheet))

def do_even(sheet):
    
    def calc_evens(row):
        result = 0
        for r in it.combinations(row,2):
            if max(r) % min(r) == 0:
                result += max(r)/min(r)
        return result
    
    print map(calc_evens, sheet)

    return sum(map(calc_evens,sheet))

def parse_sheet(raw_sheet):
    parsed = []
    for line in raw_sheet.split("\n"):
        if line:
            parsed.append(map(int, line.split()))
    return parsed

if __name__ == '__main__':
   
    parsed = parse_sheet("5  1  9  5 \n7  5  \t3\n2  4    6    8\n")
    assert [[5,1,9,5],[7,5,3],[2,4,6,8]] == parsed
    assert do_checksum(parsed) == 18
    assert do_even([[5,9,2,8],[9,4,7,3],[3,8,6,5]]) == 9

    parsed = parse_sheet(sys.argv[1])
    print do_checksum(parsed)
    print do_even(parsed)

