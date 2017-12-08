#!/usr/bin/env python

import sys
import operator as o
from collections import defaultdict

test = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""

ops = {">":o.gt, "<":o.lt, "==":o.eq, "<=":o.le, ">=":o.ge, "!=":o.ne, "inc":o.add, "dec":o.sub}

def execute(x):
    reg = defaultdict(lambda:0)
    max_val = 0

    for line in x.split("\n"):
        parts = line.split()

        if ops[parts[5]](reg[parts[4]], int(parts[6])):
            reg[parts[0]] = ops[parts[1]](reg[parts[0]], int(parts[2])) 

        max_val = max(max_val, max(reg.values()))

    return max(reg.values()), max_val


if __name__ == '__main__':
    
    assert execute(test) == (1, 10)

    print execute(sys.argv[1])

