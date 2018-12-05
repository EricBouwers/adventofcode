#!/usr/bin/env python

import sys, re, string

def part1(data):

    regex = [ l + u + "|" + u + l for l, u in zip(string.ascii_lowercase, string.ascii_uppercase)]
    regex = "|".join(regex)

    prevLen = len(data) + 1
    while prevLen != len(data):
        prevLen = len(data)
        data = re.sub(regex, "", data)

    return len(data) 

def part2(data):

    best_len = len(data)

    for l, u in zip(string.ascii_lowercase, string.ascii_uppercase):
        new_data = re.sub(l + "|" + u, "", data)
        new_len = part1(new_data)
        if new_len < best_len:
            best_len = new_len

    return best_len

if __name__ == '__main__':

    assert part1("dabAcCaCBAcCcaDA") == 10
    assert part2("dabAcCaCBAcCcaDA") == 4

    data = sys.argv[1]

    print part1(data)
    print part2(data)

