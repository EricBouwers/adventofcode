#!/usr/bin/python

import sys, re
import md5

def calc_checksum(s):
    c = []
    for i in xrange(0, len(s), 2):
        c.append(1 if  s[i] == s[i+1] else 0)
    return c        

e_data = "10000"
e_dsize = 20

data = "11110010111001001"
dsize_1 = 272
dsize = 35651584

while len(data) < dsize:
    b = data[::-1].replace("1","a").replace("0","1").replace("a", "0")
    data = data + "0" + b 

checksum = calc_checksum(data[:dsize])

while len(checksum) % 2 == 0:
    print len(checksum)
    checksum = calc_checksum(checksum)

print data[:dsize], "".join(map(str,checksum))   
