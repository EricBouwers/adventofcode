#!/usr/bin/python

import sys, re
import md5


def disk_falls_through(ticks, rows):
    for idx, row in enumerate(rows):
        position = row[1] + ticks + idx + 1
        if position % row[0] != 0:
            return False

    return True
    
test_machine = [(5,4),(2, 1)]   
machine_01 = [(17,1), (7,0), (19,2),(5,0),(3,0),(13,5)]
machine_02 = machine_01 + [(11,0)]

time = 0

while not disk_falls_through(time, machine_02):
    time += 1

print time
    
