#!/usr/bin/env python

import sys, re, collections

test_rules = """...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #"""

def part1(state, rules, allow_missing=False):
    rules = {l[0:5]:l[9] for l in rules.split("\n")}
    if not allow_missing:
        rules["...."] = "."

    for _ in range(0, 20):
        state = "...." + state + "...." 
        new_state = []
        len_pots = len(state) 
        
        for i in range(0,len_pots-3):
            if allow_missing:
                new_state.append("#" if state[i:i+5] in rules.keys() else ".")
            else:
                new_state.append(rules[state[i:i+5]])
        state = "".join(new_state)    

    sum_plants = 0
    for i in range(0, len(state)):
        sum_plants += (-40+i) if state[i] == "#" else 0
    
    return sum_plants

def part2(data):
    return None

if __name__ == '__main__':

    assert part1("#..#.#..##......###...###", test_rules, True) == 325

    assert part2("") == None

    data = sys.argv[1]
    initial = "..#..####.##.####...#....#######..#.#..#..#.#.#####.######..#.#.#.#..##.###.#....####.#.#....#.#####"
    print part1(initial, data)
    print part2(data)

