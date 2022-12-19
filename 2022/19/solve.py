#!/usr/bin/env python
import functools

test_1 = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""
test_2 = """"""


def parse_data(data):
    blueprints = {}
    for d in data:
        nums = [int(x) for x in d.replace(":", "").split(" ") if x.isdigit()]
        blueprints[nums[0]] = {
            'ore': nums[1],
            'clay': nums[2],
            'obsidian': (nums[3], nums[4]),
            'geode': (nums[5], nums[6])
        }

    return blueprints


def take_step(old, new):
    return old[0] + new[0], old[1] + new[1], old[2] + new[2], old[3] + new[3]


def get_possible_steps(blueprint, state):
    new_min = state[2] + 1
    new_collected = take_step(state[0], state[1])

    cur_collected = state[1]
    cur_robots = state[0]
    new_states = [(cur_robots, new_collected, new_min)]
    if blueprint['ore'] <= cur_collected[0]:
        new_states.append((take_step((1,0,0,0), cur_robots), take_step(new_collected, (-blueprint['ore'], 0, 0, 0)), new_min))

    if blueprint['clay'] <= cur_collected[0]:
        new_states.append((take_step((0,1,0,0), cur_robots), take_step(new_collected, (-blueprint['clay'], 0, 0, 0)), new_min))

    if blueprint['obsidian'][0] <= cur_collected[0] and blueprint['obsidian'][1] <= cur_collected[1]:
        new_states.append((take_step((0,0,1,0), cur_robots), take_step(new_collected, (-blueprint['obsidian'][0], -blueprint['obsidian'][1], 0, 0)), new_min))

    if blueprint['geode'][0] <= cur_collected[0] and blueprint['geode'][1] <= cur_collected[2]:
        new_states.append((take_step((0,0,0,1), cur_robots), take_step(new_collected, (-blueprint['geode'][0], 0, -blueprint['geode'][1], 0)), new_min))

    return new_states


def state_worth(state, minutes):
    time_left = minutes - state[2]
    return 10000*state[1][3] + 1000*state[1][2] + 100*state[1][1] + state[1][0] + \
           time_left*100000*state[0][3] + time_left*10000*state[0][2] + time_left*1000*state[0][1] + time_left*100*state[0][0]


def best_path(blueprint, minutes=24):
    states = [((1, 0, 0, 0), (0, 0, 0, 0), 0)]

    max_val = 0
    depth = 0
    while len(states) > 0:
        current_state = states.pop(0)

        cur_min = current_state[2]
        if cur_min > depth and cur_min != minutes:
            states = list(set(states))
            states.sort(key=lambda x: state_worth(x, minutes), reverse=True)
            states = states[:10000]
            depth = cur_min

        if cur_min == minutes:
            max_val = max(max_val, current_state[1][3])
        else:
            states += get_possible_steps(blueprint, current_state)

    return max_val


def part1(data):
    blueprints = parse_data(data)

    total_score = 0
    for k, bp in blueprints.items():
        score = best_path(bp)
        total_score += k * score

    return total_score


def part2(data):
    blueprints = parse_data(data)

    total_score = 1
    total_score *= best_path(blueprints[1], minutes=32)
    total_score *= best_path(blueprints[2], minutes=32)

    if len(blueprints) > 2:
        total_score *= best_path(blueprints[3], minutes=32)

    return total_score


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 33
    assert part2(test_1.splitlines()) == 62 * 56

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

