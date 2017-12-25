#!/usr/bin/env python

import sys


example = [[(1, 1, 1),(0,-1,1)], [(1,-1,0),(1,1,0)]]

my_ins = [[(1,1,1),(0,-1,1)],
          [(0,1,2),(1,-1,1)],
          [(1,1,3),(0,-1,0)],
          [(1,-1,4),(1,-1,5)],
          [(1,-1,0),(0,-1,3)],
          [(1,1,0),(1,-1,4)]]

def process_one(ins, i):
    tape = [0]*i
    state = 0
    index = i/2
    
    for x in xrange(0, i):
        cur_ins = ins[state]
        tape[index], idx, state = cur_ins[tape[index]]
        index += idx

    return sum(tape)


if __name__ == '__main__':
    assert process_one(example, 6) == 3

    print process_one(my_ins, 12629077)
