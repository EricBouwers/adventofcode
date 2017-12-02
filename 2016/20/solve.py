#!/usr/bin/python

import sys

rows = sys.argv[1].split("\n")
blocked = []

for row in rows:
    start_end = row.split("-")
    blocked.append((int(start_end[0]), int(start_end[1])))

blocked = sorted(blocked)
allowed = []

cur_max = 0
for x in range(0, len(blocked)):
    print cur_max + 1,  blocked[x][0]
    for a in range(cur_max + 1, blocked[x][0]):
        print a
        allowed.append(a)
    cur_max = max(cur_max, blocked[x][1])

print allowed
print allowed[0], len(set(allowed)) + (4294967295 - cur_max)
