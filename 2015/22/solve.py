#!/usr/bin/env python

test_1 = """Hit Points: 13
Damage: 8"""
test_2 = """"""


def parse_data(data):
    return int(data[0].split(" ")[-1]), int(data[1].split(" ")[-1])


def part1(data, p_hit_points=50, p_mana=500, hard=False):
    b_hit_points, boss_damage = parse_data(data)

    states = [(True, p_hit_points, p_mana, 0, b_hit_points, 0, 0, 0)]
    min_spend = 10000000000

    while states:
        player_turn, p_hit_points, p_mana, p_mana_spend, boss_hit_points, shield, poison, recharge = states.pop()

        if hard and player_turn:
            p_hit_points -= 1

        player_armor = 7 if shield > 0 else 0
        boss_hit_points = boss_hit_points - (3 if poison > 0 else 0)
        p_mana = p_mana + (101 if recharge > 0 else 0)

        shield = max(0, shield - 1)
        poison = max(0, poison - 1)
        recharge = max(0, recharge - 1)

        if boss_hit_points <= 0:
            min_spend = min(min_spend, p_mana_spend)

        if player_turn and p_mana_spend <= min_spend:
            if p_hit_points > 0:
                if p_mana >= 53:
                    states.append((not player_turn, p_hit_points, p_mana - 53, p_mana_spend + 53, boss_hit_points - 4, shield, poison, recharge))
                if p_mana >= 73:
                    states.append((not player_turn, p_hit_points + 2, p_mana - 73, p_mana_spend + 73, boss_hit_points - 2, shield, poison, recharge))
                if p_mana >= 113 and shield == 0:
                    states.append((not player_turn, p_hit_points, p_mana - 113, p_mana_spend + 113, boss_hit_points, 6, poison, recharge))
                if p_mana >= 173 and poison == 0:
                    states.append((not player_turn, p_hit_points, p_mana - 173, p_mana_spend + 173, boss_hit_points, shield, 6, recharge))
                if p_mana >= 229 and recharge == 0:
                    states.append((not player_turn, p_hit_points, p_mana - 229, p_mana_spend + 229, boss_hit_points, shield, poison, 5))
        else:
            p_hit_points -= max(1, boss_damage - player_armor)
            if p_hit_points > 0:
                states.append(
                    (not player_turn, p_hit_points, p_mana, p_mana_spend, boss_hit_points, shield, poison, recharge)
                )

    return min_spend


def part2(data):
    return part1(data, hard=True)


if __name__ == '__main__':

    assert part1(test_1.splitlines(), 10, 250) == 226

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

# 1269 too low