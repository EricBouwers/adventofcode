#!/usr/bin/python

import sys, re

d = sys.argv[1]

def decompress(d):
    outputsize = 0
    while d:
        m = re.search(r"\(\d+x\d+\)", d)

        if m:
            outputsize += len(d[0:m.start()])
            pattern = d[m.start():m.end()]
            d = d[m.end():]

            data = pattern.split("x")
            chars = int(data[0].replace("(",""))
            times = int(data[1].replace(")",""))

            repeatchars = d[0:chars]
            d = d[chars:]
            outputsize += decompress(repeatchars)*times

        else:
            outputsize += len(d)
            d = ""
    return outputsize

outputsize = decompress(d)

print outputsize
