#!/usr/bin/env python

test_1 = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def part1(data):
    x, y = 0,0
    for d in data:
        parts = d.split()
        if parts[0] == 'up':
            y -= int(parts[1])
        if parts[0] == 'down':
            y += int(parts[1])
    	if parts[0] == 'forward':
            x += int(parts[1])    		
    return x*y

def part2(data):
    x, y, aim = 0,0,0
    for d in data:
        parts = d.split()
        if parts[0] == 'up':
            aim -= int(parts[1])
        if parts[0] == 'down':
            aim += int(parts[1])
        if parts[0] == 'forward':
            x += int(parts[1])
            y += aim * int(parts[1])
 		
    return x*y


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 150
    assert part2(test_1.splitlines()) == 900

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

