#!/usr/bin/env python

from collections import defaultdict

test_1 = """         A           
         A           
  #######.#########  
  #######.........#  
  #######.#######.#  
  #######.#######.#  
  #######.#######.#  
  #####  B    ###.#  
BC...##  C    ###.#  
  ##.##       ###.#  
  ##...DE  F  ###.#  
  #####    G  ###.#  
  #########.#####.#  
DE..#######...###.#  
  #.#########.###.#  
FG..#########.....#  
  ###########.#####  
             Z       
             Z      """
test_2 = """                   A               
                   A               
  #################.#############  
  #.#...#...................#.#.#  
  #.#.#.###.###.###.#########.#.#  
  #.#.#.......#...#.....#.#.#...#  
  #.#########.###.#####.#.#.###.#  
  #.............#.#.....#.......#  
  ###.###########.###.#####.#.#.#  
  #.....#        A   C    #.#.#.#  
  #######        S   P    #####.#  
  #.#...#                 #......VT
  #.#.#.#                 #.#####  
  #...#.#               YN....#.#  
  #.###.#                 #####.#  
DI....#.#                 #.....#  
  #####.#                 #.###.#  
ZZ......#               QG....#..AS
  ###.###                 #######  
JO..#.#.#                 #.....#  
  #.#.#.#                 ###.#.#  
  #...#..DI             BU....#..LF
  #####.#                 #.#####  
YN......#               VT..#....QG
  #.###.#                 #.###.#  
  #.#...#                 #.....#  
  ###.###    J L     J    #.#.###  
  #.....#    O F     P    #.#...#  
  #.###.#####.#.#####.#####.###.#  
  #...#.#.#...#.....#.....#.#...#  
  #.#####.###.###.#.#.#########.#  
  #...#.#.....#...#.#.#.#.....#.#  
  #.###.#####.###.###.#.#.#######  
  #.#.........#...#.............#  
  #########.###.###.#############  
           B   J   C               
           U   P   P               """
test_3 = """             Z L X W       C                 
             Z P Q B       K                 
  ###########.#.#.#.#######.###############  
  #...#.......#.#.......#.#.......#.#.#...#  
  ###.#.#.#.#.#.#.#.###.#.#.#######.#.#.###  
  #.#...#.#.#...#.#.#...#...#...#.#.......#  
  #.###.#######.###.###.#.###.###.#.#######  
  #...#.......#.#...#...#.............#...#  
  #.#########.#######.#.#######.#######.###  
  #...#.#    F       R I       Z    #.#.#.#  
  #.###.#    D       E C       H    #.#.#.#  
  #.#...#                           #...#.#  
  #.###.#                           #.###.#  
  #.#....OA                       WB..#.#..ZH
  #.###.#                           #.#.#.#  
CJ......#                           #.....#  
  #######                           #######  
  #.#....CK                         #......IC
  #.###.#                           #.###.#  
  #.....#                           #...#.#  
  ###.###                           #.#.#.#  
XF....#.#                         RF..#.#.#  
  #####.#                           #######  
  #......CJ                       NM..#...#  
  ###.#.#                           #.###.#  
RE....#.#                           #......RF
  ###.###        X   X       L      #.#.#.#  
  #.....#        F   Q       P      #.#.#.#  
  ###.###########.###.#######.#########.###  
  #.....#...#.....#.......#...#.....#.#...#  
  #####.#.###.#######.#######.###.###.#.#.#  
  #.......#.......#.#.#.#.#...#...#...#.#.#  
  #####.###.#####.#.#.#.#.###.###.#.###.###  
  #.......#.....#.#...#...............#...#  
  #############.#.#.###.###################  
               A O F   N                     
               A A D   M                     """
test_4 = """"""


def parse_world(data):
    world = {}
    y = 0
    max_x = 0

    for line in data.splitlines():
        x = 0
        for c in line:
            cur_pos = (x, y)
            world[cur_pos] = c

            x += 1
        y += 1
        max_x = max(max_x, x)

    return world, max_x, y


def fold_world(world, max_x, max_y):

    portal_index = 97
    portal_mapping = {}
    portal_positions = defaultdict(list)

    for y in range(max_y):
        for x in range(max_x):
            pos = (x, y)
            what = world.get((x, y), "")
            if what.isupper():
                created, portal_index = try_create_portal([1, 0], portal_index, portal_positions, portal_mapping, pos, world)
                if not created:
                    created, portal_index = try_create_portal([0, 1], portal_index, portal_positions, portal_mapping, pos, world)

                if not created:
                    created, portal_index = try_create_portal([-1, 0], portal_index, portal_positions, portal_mapping, pos, world)

                if not created:
                    created, portal_index = try_create_portal([0, -1], portal_index, portal_positions, portal_mapping, pos, world)

    return world, portal_positions, portal_mapping


def try_create_portal(step, portal_index, portal_positions, portals, pos, world):
    neighbor = take_step(pos, step)
    if world.get(neighbor, "").isupper():
        next_next = take_step(neighbor, step)

        if world.get(next_next, "") == ".":

            portal_name = world[pos] + world[neighbor] if 1 in step else world[neighbor] + world[pos]

            if portal_name not in portals:
                portals[portal_name] = str(chr(portal_index))
                portal_index += 1

            my_index = portals[portal_name]
            portal_positions[my_index].append(next_next)
            world[neighbor] = my_index
            world[pos] = " "

            return True, portal_index

    return False, portal_index


def take_step(cur_pos, step):
    return cur_pos[0] + step[0], cur_pos[1] + step[1]


def print_world(world, max_x, max_y):

    for y in range(max_y):
        line = ""
        for x in range(max_x):
            line += world.get((x,y), " ")
        print(line)


STEPS = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def part1(data):
    world, max_x, max_y = parse_world(data)
    world, portal_positions, portal_mapping = fold_world(world, max_x, max_y)
    print_world(world, max_x, max_y)

    cur_pos = portal_positions[portal_mapping["AA"]][0]
    end = portal_positions[portal_mapping["ZZ"]][0]

    moves = [(0, cur_pos)]
    min_seens = {}

    while len(moves) > 0:
        steps, cur_pos = moves.pop(0)
        if cur_pos == end:
            return steps
        else:
            for s in STEPS:
                new_pos = take_valid_step(cur_pos, s, world, portal_positions)
                if new_pos is not None:
                    my_steps = steps + 1
                    if new_pos not in min_seens:
                        moves.append((my_steps, new_pos))
                        min_seens[new_pos] = my_steps

    return None


def take_valid_step(cur_pos, step, world, portal_positions):
    new_pos = cur_pos[0] + step[0], cur_pos[1] + step[1]
    if world[new_pos] == ".":
        return new_pos
    elif world[new_pos] in portal_positions:
        possible = [p for p in portal_positions[world[new_pos]] if p != cur_pos]
        return possible[0] if possible else None
    else:
        return None


def take_valid_level_step(cur_pos, step, level, world, portal_positions, outer_portals):
    new_pos = cur_pos[0] + step[0], cur_pos[1] + step[1]
    if world[new_pos] == ".":
        return new_pos, level
    elif world[new_pos] in portal_positions:
        possible = [p for p in portal_positions[world[new_pos]] if p != cur_pos]
        if possible:
            jump_pos = possible[0]

            if new_pos in outer_portals:
                if level > 0:
                    new_level = level - 1
                    return jump_pos, new_level
                else:
                    return None, level
            else:
                new_level = level + 1
                return jump_pos, new_level

    return None, level


def is_outer_portal_position(portal, max_x, max_y):
    return portal[0] == 1 or portal[0] == (max_x - 2) or portal[1] == 1 or portal[1] == (max_y - 2)


def part2(data):
    world, max_x, max_y = parse_world(data)
    world, portal_positions, portal_mapping = fold_world(world, max_x, max_y)
    print_world(world, max_x, max_y)

    start_pos = portal_positions[portal_mapping["AA"]][0]
    end = portal_positions[portal_mapping["ZZ"]][0]

    outer_portals = []
    for k, v in world.items():
        if v != " " and is_outer_portal_position(k, max_x, max_y):
            outer_portals.append(k)

    moves = [(0, start_pos, 0)]
    min_seens = {}

    while len(moves) > 0:
        steps, cur_pos, level = moves.pop(0)

        world[start_pos] = "#" if level != 0 else "."
        world[end] = "#" if level != 0 else "."

        if cur_pos == end and level == 0:
            return steps
        else:
            for s in STEPS:
                new_pos, new_level = take_valid_level_step(cur_pos, s, level, world, portal_positions, outer_portals)
                if new_pos is not None:
                    my_steps = steps + 1
                    if (new_pos, new_level) not in min_seens:
                        moves.append((my_steps, new_pos, new_level))
                        min_seens[(new_pos, new_level)] = my_steps

    return None


if __name__ == '__main__':

    assert part1(test_1) == 23
    assert part1(test_2) == 58
    assert part2(test_1) == 26
    assert part2(test_3) == 396

    print("Done testing")

    with open('input') as f:
        data = f.read()

    print(part1(data))
    print(part2(data))

