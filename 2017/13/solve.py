#!/usr/bin/env python

import sys

example = """0: 3
1: 2
4: 4
6: 4"""

def parse_ports(ports):
    port_ranges = {} 
    for p in ports.split("\n"):
        parts = p.split(":")
        port_ranges[int(parts[0])] = int(parts[1].replace(" ",""))
    
    return port_ranges


def calc_caughts(port_ranges, delay):
    caughts = 0
    ps = 0 + delay
    caught = False
    for step in xrange(0, max(port_ranges.keys())+1):
        if step in port_ranges:
            port_range = port_ranges[step]
            range_steps = port_range * 2 - 2
            
            if ps == 0 or ps % range_steps == 0:
                caughts += step * port_ranges[step]
                caught = True
        ps += 1    

    return caughts, caught


def calc_safe(ports):
    delay = 0

    while True: 
        if not calc_caughts(ports, delay)[1]:
            return delay
        else:
            delay += 1


if __name__ == '__main__':
    
    assert calc_caughts(parse_ports(example), 0) == (24, True)
    assert calc_safe(parse_ports(example)) == 10

    print calc_caughts(parse_ports(sys.argv[1]), 0)
    print calc_safe(parse_ports(sys.argv[1]))

