#!/usr/bin/env python

import sys

test_1 = """#########
#b.A.@.a#
#########"""
test_2 = """########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################"""
test_3 = """#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################"""
test_4 = """#######
#a.#Cd#
##...##
##.@.##
##...##
#cB#Ab#
#######"""
test_5 = """###############
#d.ABC.#.....a#
######...######
######.@.######
######...######
#b.....#.....c#
###############"""
test_6 = """#############
#g#f.D#..h#l#
#F###e#E###.#
#dCba...BcIJ#
#####.@.#####
#nK.L...G...#
#M###N#H###.#
#o#m..#i#jk.#
#############"""


def parse_world(data):
    world = {}
    y = 0

    me = None
    keys = dict()

    for line in data.splitlines():
        x = 0
        for c in line:
            cur_pos = (x, y)
            world[cur_pos] = c
            if c == "@":
                me = cur_pos
            elif c.islower():
                keys[c] = cur_pos

            x += 1
        y += 1

    return world, keys, me


STEPS = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def take_step(cur_pos, step, world, keys):
    new_pos = cur_pos[0] + step[0], cur_pos[1] + step[1]
    if world[new_pos] in [".", "@"] or world[new_pos].islower() or world[new_pos].lower() in keys:
        return new_pos
    else:
        return None


def print_state(pos, keys):
    return str(pos) + "keys = [" + ",".join(sorted(keys)) + "]"


def part1(data):
    world, keys, me = parse_world(data)

    moves = [(0, me, set())]
    seen_states = set(print_state(me, set()))

    while len(moves) > 0:
        steps, cur_pos, my_keys = moves.pop(0)

        if len(keys.keys() - my_keys) == 0:
            return steps, my_keys
        else:
            for s in STEPS:
                new_pos = take_step(cur_pos, s, world, my_keys)
                new_keys = my_keys
                if new_pos is not None:
                    if world[new_pos].islower():
                        new_keys = set([k for k in my_keys])
                        new_keys.add(world[new_pos])

                    state_key = print_state(new_pos, new_keys)
                    if state_key not in seen_states:
                        moves.append((steps+1, new_pos, new_keys))

                    seen_states.add(state_key)

    return -1, my_keys


def part2(data):
    world, keys, me = parse_world(data)

    world[me] = "#"
    world[(me[0]-1, me[1])] = "#"
    world[(me[0]+1, me[1])] = "#"
    world[(me[0], me[1]-1)] = "#"
    world[(me[0], me[1]+1)] = "#"

    world[(me[0]-1, me[1]-1)] = "@"
    world[(me[0]+1, me[1]+1)] = "@"
    world[(me[0]-1, me[1]+1)] = "@"
    world[(me[0]+1, me[1]-1)] = "@"

    all_mes = [(me[0]-1, me[1]-1), (me[0]+1, me[1]+1), (me[0]+1, me[1]-1), (me[0]-1, me[1]+1)]

    moves = [(0, all_mes, set())]
    seen_states = set(print_state(all_mes, set()))

    while len(moves) > 0:
        steps, cur_positions, my_keys = moves.pop(0)

        if len(keys.keys() - my_keys) == 0:
            return steps
        else:
            for i, cur_pos in enumerate(cur_positions):
                for s in STEPS:
                    new_pos = take_step(cur_pos, s, world, my_keys)
                    new_keys = my_keys
                    if new_pos is not None:
                        if world[new_pos].islower():
                            new_keys = set([k for k in my_keys])
                            new_keys.add(world[new_pos])

                        new_positions = [n for n in cur_positions]
                        new_positions[i] = new_pos
                        state_key = print_state(new_pos, new_keys)
                        if state_key not in seen_states:
                            moves.append((steps+1, new_positions, new_keys))

                        seen_states.add(state_key)


if __name__ == '__main__':

    assert part1(test_1)[0] == 8
    assert part1(test_2)[0] == 86
    assert part1(test_3)[0] == 136
    assert part2(test_4) == 8
    assert part2(test_5) == 24
    # assert part2(test_6) == 72

    print('done testing')

    with open('input') as f:
        data = f.read()

    print(part1(data))
    print(part2(data))

