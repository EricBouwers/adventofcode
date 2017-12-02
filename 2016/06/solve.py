#!/usr/bin/python

import sys
from collections import Counter

messages = sys.argv[1].split("\n")
verticals = [""]*8

for message in messages:
    for i in range(0,len(message)):
        verticals[i] += message[i]

message = ""
alt_message = ""
for v in verticals:
    if v:
        common = Counter(v).most_common()
        message += common[0][0]
        alt_message += common[-1][0]

print message
print alt_message
