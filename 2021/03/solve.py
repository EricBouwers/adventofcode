#!/usr/bin/env python

test_1 = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


def parse_data(data):
    r = []
    for d in data:
        r.append([int(x) for x in d])    

    return r


def part1(data):
    data = parse_data(data)
    g, e = "", ""
    for x in range(0, len(data[0])):
        if sum([d[x] for d in data]) > (len(data) / 2):
            g += '1'
            e += '0'
        else:
            g += '0'
            e += '1'

    return int(g, 2) * int(e, 2)


def part2(input_data):
    o, c = "", ""

    data = parse_data(input_data)
    for x in range(0, len(data[0])):
        if sum([d[x] for d in data]) >= (len(data) / 2.0):
            data = [d for d in data if d[x] == 1]
        else:
            data = [d for d in data if d[x] == 0]
        if len(data) == 1:
            o = "".join([str(x) for x in data[0]])

    data = parse_data(input_data)   
    for x in range(0, len(data[0])):
        if sum([d[x] for d in data]) >= (len(data) / 2.0):
            data = [d for d in data if d[x] == 0]
        else:
            data = [d for d in data if d[x] == 1]
        if len(data) == 1:          
            c = "".join([str(x) for x in data[0]])       
    
    return int(o, 2) * int(c, 2)    


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 198
    assert part2(test_1.splitlines()) == 230

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

