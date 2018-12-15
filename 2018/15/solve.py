#!/usr/bin/env python

example_input_1 = """#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######"""

example_input_2 = """#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######"""

example_input_3 = """#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######"""

example_input_4 = """#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######"""

example_input_5 = """#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.#
#########"""

import sys, re

def parse_input(data):
    area = [[c for c in l] for l in data.split("\n")]
    w = len(area[0])
    h = len(area)

    elves = []
    goblins = []

    for y in range(0, h):
        for x in range(0, w):
            if area[y][x] in "GE":
                d = elves if area[y][x] == "E" else goblins
                d.append([x,y,200,area[y][x]])

    return area, w, h, elves, goblins                

def adjacent(x,y,w,h):
    result = [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]
    
    result = filter(lambda c: 0 <= c[0] and 0 <= c[1], result)
    result = filter(lambda c: c[0] < w and c[1] < h, result)

    return result 

def find_adj_enemies(unit, enemies, area, w, h):
    neigh = adjacent(unit[0], unit[1], w, h)
    enemy = "E" if unit[3] == "G" else "G"

    result = []
    for n in neigh:
        if area[n[1]][n[0]] == enemy:
            result.append([e for e in enemies if e[1] == n[1] and e[0] == n[0]][0]) 

    return result 

def open_spaces(coords, area):
    result = []
    for c in coords:
        if area[c[1]][c[0]] == ".":
            result.append(c)
    return result        

def find_targets(unit, enemies, area, w, h):
    all_enemy_neigh = []
    for e in enemies:
        all_enemy_neigh += adjacent(e[0], e[1], w, h)
    
    return open_spaces(all_enemy_neigh, area)

def find_step(unit, targets, area, w, h):
    paths = []
    for t in targets:
        shortest_path = find_shortest_path(unit, t, area, w, h)
        if shortest_path is not None:
            paths.append([shortest_path, t[1], t[0]])
   
    if len(paths) > 0:
        paths.sort()

        selected = [paths[0][2], paths[0][1]]
        dist = paths[0][0]
        neighs = open_spaces(adjacent(unit[0], unit[1], w, h), area)
        for n in sorted(neighs, key = lambda x: (x[1], x[0])):
            new_dist = find_shortest_path(n, selected, area, w, h)
            if new_dist is not None and (new_dist == dist - 1):
                return n
    else:
        return None

def hash_pos(pos):
    return str(pos[0]) + "_" + str(pos[1])

def get_possible_steps(steps, current_pos, first, area, w, h):
    neighs = open_spaces(adjacent(current_pos[0], current_pos[1], w, h), area)
    return [(steps + 1, n, n if first is None else first) for n in neighs]

def find_shortest_path(unit, target, area, w, h):
    states = [(0, unit[0:2], None)]
    seen_states = set()
    paths = []

    seen_all = False
    while len(states) > 0 and not seen_all:
        steps, cur_pos, first = states.pop(0)

        while hash_pos(cur_pos) in seen_states and states:
            steps, cur_pos, first = states.pop(0)
       
        seen_all = hash_pos(cur_pos) in seen_states
        
        if cur_pos[0] == target[0] and cur_pos[1] == target[1]: 
            return steps
        else:
            seen_states.add(hash_pos(cur_pos))
            states += get_possible_steps(steps, cur_pos, first, area, w, h)

    return None

def take_step(step, unit, area):
    area[unit[1]][unit[0]] = "."
    unit[0] = step[0]
    unit[1] = step[1]
    area[unit[1]][unit[0]] = unit[3]

def print_area(area):
    for y in area:
        print "".join(y)

    print "========="    

def part1(data, elf_power=3, debug_area=True):
    area, w, h, elves, goblins = parse_input(data)
    start_elves = len(elves)
    rounds = 0
  
    while len(elves) > 0 and len(goblins) > 0:
        finished = False
        units = sorted(elves+goblins, key=lambda x: (x[1], x[0]))
        for unit in units:

            if unit[2] <= 0:
                continue 

            enemies = elves if unit[3] == "G" else goblins
            team = elves if unit[3] == "E" else goblins

            if len(enemies) == 0 or len(team) == 0:
                finished = True
                continue

            adj_enemies = find_adj_enemies(unit, enemies, area, w, h) 
            if len(adj_enemies) == 0:
                targets = find_targets(unit, enemies, area, w, h)
                if len(targets) > 0:
                    step = find_step(unit, targets, area, w, h)
                    if step is not None:
                        take_step(step, unit, area)
                        adj_enemies = find_adj_enemies(unit, enemies, area, w, h) 
                else:
                    adj_enemies = [] 

            if len(adj_enemies) > 0:
                adj_enemies.sort(key=lambda x: (x[2], x[1], x[0]))
                adj_enemies[0][2] -= 3 if unit[3] == "G" else elf_power

                killed = filter(lambda u: u[2] <= 0, elves + goblins)
                for k in killed:
                    area[k[1]][k[0]] = "."

                elves = filter(lambda e: e[2] > 0, elves)
                goblins = filter(lambda e: e[2] > 0, goblins)

                if elf_power > 3 and len(elves) != start_elves:
                    return None, False

        rounds += 1 if not finished else 0

        if debug_area:
            print_area(area)

    result = rounds * sum(map(lambda x: x[2], elves + goblins))
    return result, len(elves) == start_elves

def part2(data):
    elves_win_no_loss = False
    attack_power = 3
    result = None

    while not elves_win_no_loss:
        attack_power += 1 
        result, elves_win_no_loss = part1(data, elf_power=attack_power)     
        print attack_power, elves_win_no_loss

    return result

if __name__ == '__main__':

    assert part1(example_input_1) == (27730, False)
    assert part1(example_input_2) == (36334, False)
    assert part1(example_input_3) == (39514, False)
    assert part1(example_input_4) == (28944, False)
    assert part1(example_input_5) == (18740, False)
    assert part2(example_input_1) == 4988 
    assert part2(example_input_3) == 31284

    data = sys.argv[1]

    print part1(data)
    print part2(data)
