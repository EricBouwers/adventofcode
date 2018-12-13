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

def part1(state, rules, gens, allow_missing=False):
    rules = {l[0:5]:l[9] for l in rules.split("\n")}
    if not allow_missing:
        rules["...."] = "."

    first_pos = 0
    seen = set()

    for x in xrange(0, gens):
        state = "...." + state + "..." 
        new_state = []
        len_pots = len(state) 
        first_pos -= 2
        
        for i in range(0,len_pots-4):
            if allow_missing:
                new_state.append("#" if state[i:i+5] in rules.keys() else ".")
            else:
                new_state.append(rules[state[i:i+5]])
        state = "".join(new_state)    

        first_flower = state.find("#")
        state = state[first_flower:]
        first_pos += first_flower 
        
        len_state = len(state)    
        if state[len_state-1:] == '..':
            state = state[0:len_state-1]

        if state in seen:
            first_pos += (gens - x) - 1
            break
        else:
            seen.add(state)    

    sum_plants = 0
    for i in range(0, len(state)):
        sum_plants += (first_pos + i) if state[i] == "#" else 0
   
    return sum_plants 

if __name__ == '__main__':

    assert part1("#..#.#..##......###...###", test_rules, 20, True) == 325

    data = sys.argv[1]
    initial = "..#..####.##.####...#....#######..#.#..#..#.#.#####.######..#.#.#.#..##.###.#....####.#.#....#.#####"
    print part1(initial, data, 20)
    print part1(initial, data, 50000000000)

