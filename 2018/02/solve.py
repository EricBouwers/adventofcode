#!/usr/bin/env python

import sys
import collections 
import itertools

def count_id(boxid):
    c = collections.Counter(boxid)
    two = 0
    three = 0

    for _, c in c.most_common():
        if c == 2:
            two = 1
        if c == 3:
            three = 1

    return (two, three)

def checksum(boxids):
    counts = map(count_id, boxids.split("\n"))
    return sum(map(lambda x: x[0], counts)) * sum(map(lambda x: x[1], counts))

def count_diffs(tup):
    diffs = [ord(x) - ord(y) for x,y in zip(tup[0],tup[1])]
    if len(filter(lambda x: x != 0 , diffs)) == 1:
        return (diffs, tup[0])
    else:
        return None

def common_letters(boxids):
    combos = itertools.combinations(boxids.split("\n"), 2)
    match = filter(None, map(count_diffs, combos)) 
    
    return "".join([y if x == 0 else "" for x,y in zip(match[0][0], match[0][1])])


if __name__ == '__main__':
    
    assert count_id("abcdef") == (0,0)
    assert count_id("bababc") == (1,1)
    assert count_id("abbcde") == (1,0)
    assert count_id("aabcdd") == (1,0)

    assert checksum("aabcdd\naaabcd") == 1

    assert common_letters("abcde\nfghij\nklmno\npqrst\nfguij\naxcye\nwvxyz") == "fgij"

    print checksum(sys.argv[1])
    print common_letters(sys.argv[1])

