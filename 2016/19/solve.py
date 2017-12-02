#!/usr/bin/python

import sys

elfs = int(sys.argv[1])

# from https://www.youtube.com/watch?v=uCsD3ZGzMgE
binary = "{0:b}".format(elfs) 
binary += binary[0]

print int(binary[1:], 2)

circel = [i for i in range(1, elfs+1)]

# takes waaaay to long
while len(circel) > 1:
    unlucky_pos = len(circel) / 2
    del circel[unlucky_pos]
    circel.append(circel.pop(0))

print circel

