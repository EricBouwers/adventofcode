#!/usr/bin/env python

import sys, re

example_input_1 = """x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504"""

def parse_area(data):
    sand = []
    for l in data.split("\n"):
        ints = [int(x) for x in re.findall("\d+", l)]

        if l[0] == "x":
            x = ints[0]
            y = range(ints[1], ints[2]+1)
            sand += zip([x]*len(y), y)
        else:    
            x = range(ints[1], ints[2]+1)
            y = ints[0]
            sand += zip(x, [y]*len(x))
    sand = set(sand) 
    min_y = min([c[1] for c in sand])
    max_y = max([c[1] for c in sand]) + 1
    min_x = min([c[0] for c in sand])
    max_x = max([c[0] for c in sand])
  
    area = []
    for y in range(0, max_y):
        layer = []
        area.append(layer)
        for x in range(min_x-2, max_x+2):
            if x == 500 and y == 0:
                c = "+"
            else:
                c = "#" if (x,y) in sand else "."
            layer.append(c)
    
    return area, min_y, max_y

def part1(data):
    area, min_y, max_y = parse_area(data)  

    cur_i = 1
    while cur_i != max_y:
        prev_layer = area[cur_i - 1]
        layer = area[cur_i]
        next_layer = area[cur_i + 1] if cur_i + 1 < max_y else None 

        changed = False
        x = 0
        while x != len(layer):
            if layer[x] in "#~":
                x += 1
            elif prev_layer[x] in "+|":
                if next_layer is None or next_layer[x] not in "~#":
                    layer[x] = "|" if layer[x] == "." else layer[x]
                    x += 1
                else:
                    left_x, right_x = (x,x)
                    left_w, right_w = (False, False)
                    left_s, right_s = (True, True)
                    
                    while left_s and (left_x >= 0 or not left_w):
                        if layer[left_x] in ".|" and next_layer[left_x] in "~#":
                            left_x -= 1
                        elif layer[left_x] == "#":
                            left_w = True
                            left_s = False
                        elif next_layer[left_x] not in "~#":
                            left_s = False
                    
                    while right_s and (right_x <= len(layer) or not right_w):
                        if layer[right_x] in ".|" and next_layer[right_x] in "~#":
                            right_x += 1
                        elif layer[right_x] == "#":
                            right_w = True
                            right_s = False
                        elif next_layer[right_x] not in "~#":
                            right_s = False
                    
                    new_char = "~" if right_w and left_w else "|"
                    for new_x in range(left_x, right_x+1):
                        if layer[new_x] in ".|":
                            changed = layer[new_x] != new_char 
                            layer[new_x] = new_char
                    
                    x = right_x 
            else:    
                x += 1
        
        cur_i += 1 if not changed else -1

    total, remain = (0,0)
    for y in range(min_y, max_y):
        total += sum([1 for x in area[y] if x in "|~"])
        remain += sum([1 for x in area[y] if x in "~"])

    return total, remain

def print_area(area):
    for layer in area:
        print "".join(layer)

if __name__ == '__main__':

    assert part1(example_input_1) == (57, 29)

    data = sys.argv[1]

    print part1(data)

