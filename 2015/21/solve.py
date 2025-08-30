#!/usr/bin/env python
from itertools import permutations, combinations

test_1 = """"""
test_2 = """"""

WEAPONS = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0),
]

ARMOR = [
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
]

RINGS = [
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
]

def parse_data(data):
    # hitpoints, damage, armor
    return int(data[0].split(" ")[-1]), int(data[1].split(" ")[-1]), int(data[2].split(" ")[-1])

def get_item_combinations():
    ring_combos = [r for r in combinations([x for x in range(0, 6)], 2)] + [(x,) for x in range(0, 6)]

    item_combinations = []
    for w in WEAPONS:
        weapon_combinations = [(w[0], w[1], w[2])]
        for a in ARMOR:
            weapon_combinations.append(((w[0]+a[0], w[1]+a[1], w[2]+a[2])))

        for wc in weapon_combinations:
            item_combinations.append(wc)
            for rc in ring_combos:
                ring_costs = sum([RINGS[i][0] for i in rc])
                ring_damage = sum([RINGS[i][1] for i in rc])
                ring_armor = sum([RINGS[i][2] for i in rc])
                item_combinations.append((wc[0] + ring_costs, wc[1] + ring_damage, wc[2] + ring_armor))

    return item_combinations

def do_i_win(player, boss):
    player_hitpoints = player[0]
    boss_hitpoints = boss[0]
    player_step = max([1, player[1]-boss[2]])
    boss_step = max([1, boss[1]-player[2]])

    my_turn = True
    while player_hitpoints > 0 and boss_hitpoints > 0:
        if my_turn:
            boss_hitpoints -= player_step
        else:
            player_hitpoints -= boss_step
        my_turn = not my_turn

    return player_hitpoints > 0

def part1(data):
    boss = parse_data(data)

    lowest_win = 10000000
    for cost, damage, armor in get_item_combinations():
        if cost < lowest_win and do_i_win((100, damage, armor), boss):
            lowest_win = cost

    return lowest_win


def part2(data):
    boss = parse_data(data)

    largest_loss = 0
    for cost, damage, armor in get_item_combinations():
        if cost > largest_loss and not do_i_win((100, damage, armor), boss):
            largest_loss = cost

    return largest_loss


if __name__ == '__main__':

    assert do_i_win((8, 5, 5), (12, 7, 2)) == True
    assert do_i_win((8, 5, 5), (13, 7, 2)) == False

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

# too high 256
# too high 131
# too low 111