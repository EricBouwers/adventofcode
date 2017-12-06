#!/usr/bin/env python

import sys

def distribute_highest(bank):
    max_val = max(bank)
    index = bank.index(max_val)
    bank[index] = 0

    for i in xrange(1,max_val+1):
        bank[(index + i) % len(bank)] += 1

    return bank

def calc_steps(bank):
    result = 0
    seen_states = []

    while bank not in seen_states:
        seen_states.append(list(bank))
        bank = distribute_highest(bank)
        result += 1

    return result, bank


if __name__ == '__main__':
    
    assert calc_steps([0,2,7,0])[0] == 5

    steps, bank = calc_steps([2,8,8,5,4,2,3,1,5,5,1,2,15,13,5,14])
    print steps
    print calc_steps(bank)

