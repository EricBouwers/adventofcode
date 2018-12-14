#!/usr/bin/env python

import sys, re

def part1(data):
    scores = [3,7]
    len_scores = 2
    elf1 = 0
    elf2 = 1

    while len_scores < (data + 10):
        new_recep = str(scores[elf1] + scores[elf2])
        for s in new_recep:
            scores.append(int(s))
        len_scores += len(new_recep)

        elf1 += (1 + scores[elf1])
        elf2 += (1 + scores[elf2])
        elf1 = elf1 % len_scores
        elf2 = elf2 % len_scores

    return "".join([str(s) for s in scores[data:data+10]])

def part2(data):
    scores = [3,7]
    len_scores = 2
    elf1 = 0
    elf2 = 1

    data = [int(x) for x in data]
    last_n = len(data)

    found = False
    while not found: 
        new_recep = str(scores[elf1] + scores[elf2])

        for s in new_recep:
            scores.append(int(s))
            len_scores += 1
            if scores[len_scores-last_n:] == data:
                found = True
                break

        elf1 += (1 + scores[elf1])
        elf2 += (1 + scores[elf2])
        elf1 = elf1 % len_scores
        elf2 = elf2 % len_scores

    return len_scores - last_n

if __name__ == '__main__':

    assert part1(9) == "5158916779"
    assert part1(5) == "0124515891" 
    assert part1(18) == "9251071085"
    assert part1(2018) == "5941429882"
    
    assert part2("51589") == 9
    assert part2("01245") == 5
    assert part2("92510") == 18
    assert part2("59414") == 2018

    print part1(505961)
    print part2("505961")

