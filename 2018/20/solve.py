#!/usr/bin/env python

import sys, re

rsteps = { "N":(0,-2), "E":(2,0), "S":(0,2), "W":(-2,0) }
dsteps = { "N":(0,-1), "E":(1,0), "S":(0,1), "W":(-1,0) }

def add_coords(x,y):
    return (x[0] + y[0], x[1] + y[1])

# using https://stackoverflow.com/questions/4284991/parsing-nested-parentheses-in-python-grab-content-by-level
def push(obj, l, depth):
    while depth:
        l = l[-1]
        depth -= 1

    l.append(obj)

def parse_parens(s):
    groups = []
    depth = 0

    for char in s:
        if char == '(':
            push([], groups, depth)
            depth += 1
        elif char == ')':
            depth -= 1
        else:
            push(char, groups, depth)
    
    return groups

def part1(data):
    rooms = {}
    doors = set()
    cur_pos = (0,0)
    seen_doors = 0

    stack = []
    
    for s in data[1:len(data)-1]:
        if s == "(":
            stack.append((cur_pos, seen_doors))
        elif s == ")":
            cur_pos, seen_doors = stack.pop()
        elif s == "|":
            cur_pos, seen_doors = stack[-1]
        else:
            doors.add(add_coords(cur_pos, dsteps[s]))
            cur_pos = add_coords(cur_pos, rsteps[s])
            seen_doors += 1
            if cur_pos not in rooms.keys() or rooms[cur_pos] > seen_doors:
                rooms[cur_pos] = seen_doors
    
    return max(rooms.values()), sum([1 for x in rooms.values() if x >= 1000])

if __name__ == '__main__':

    assert part1("^WNE$")[0] == 3
    assert part1("^ENWWW(NEEE|SSE(EE|N))$")[0] == 10
    assert part1("^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$")[0] == 18
    assert part1("^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$")[0] == 23
    assert part1("^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$")[0] == 31

    data = sys.argv[1]

    print part1(data)
