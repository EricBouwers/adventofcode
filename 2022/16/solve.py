#!/usr/bin/env python
from collections import defaultdict
from itertools import permutations

test_1 = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""
test_2 = """"""


def parse_data(data):
    valves, edges = {}, defaultdict(list)
    for d in data:
        parts = d.replace(";", "").replace(",", "").split(" ")
        valve = parts[1]
        valves[valve] = int(parts[4].split("=")[1])
        for v in parts[9:]:
            edges[valve].append(v)
    return valves, edges


# def potential_score(minutes_left, parent_valves, new_valve, valves, edges, open_valves):
#     if minutes_left == 0:
#         return 0
#     else:
#         open_score = valves[new_valve] * minutes_left - 1 if new_valve not in open_valves else 0
#         without_open_descents = sum([
#             potential_score(minutes_left-1, parent_valves + [new_valve], v, valves, edges, open_valves)
#             for v in edges[new_valve] if v not in parent_valves
#         ])
#         with_open_descents = sum([
#             potential_score(minutes_left-2, parent_valves + [new_valve], v, valves, edges, open_valves+[new_valve])
#             for v in edges[new_valve] if v not in parent_valves
#         ])
#         return max([without_open_descents, open_score + with_open_descents])
#
#
    # for i in range(30, 0, -1):
    #     print(i, cur_valve)
    #     open_score = i * valves[cur_valve] if cur_valve not in open_valves else 0
    #     move_scores = {
    #         to_valve: potential_score(i-1, [cur_valve], to_valve, valves, edges, open_valves)
    #         for to_valve in edges[cur_valve]
    #     }
    #
    #     max_move = max(move_scores.values())
    #     if open_score > max_move:
    #         open_valves.append(cur_valve)
    #     else:
    #         for v, s in move_scores.items():
    #             if s == max_move:
    #                 cur_valve = v
    #
    #     released_pressure += sum([valves[v] for v in open_valves])
    # return released_pressure

def calc_shortest_path(s, e, edges):
    states = [(0, s)]
    seen_states = set()

    while len(states) > 0:
        current_state = states.pop(0)

        while current_state[1] in seen_states and states:
            current_state = states.pop(0)
        seen_states.add(current_state[1])

        cur_pos = current_state[1]
        if cur_pos == e:
            return current_state[0]
        else:
            states = states + [(current_state[0]+1, e) for e in edges[current_state[1]]]


def calculate_dists(valves, edges):
    dists = {}

    for v1 in valves:
        for v2 in valves:
            if v1 != v2 and (v1, v2) not in dists:
                dists[(v1, v2)] = calc_shortest_path(v1, v2, edges) + 1

    return dists


def been_here(open_valves, cur_valve, cur_score, cache):
    cache_key = tuple(sorted(open_valves + [cur_valve]))
    prev_score = cache.get(cache_key)
    if prev_score is None or prev_score < cur_score:
        cache[cache_key] = cur_score
    else:
        return prev_score
    return None


def path_value(open_valves, overall_minutes, dists, valves):
    value = 0
    minutes = overall_minutes
    for step in zip(open_valves, open_valves[1:]):
        minutes -= dists[step]
        value += minutes * valves[step[1]]

    return value


def max_value_for_valve(open_valves, cur_valve, score, overall_minutes, minutes_left, valves, dists, cache):
    has_seen = been_here(open_valves, cur_valve, score, cache)
    if has_seen is not None:
        return has_seen

    scores = [score]
    options = [v for v in valves.keys() if v not in open_valves and v != cur_valve and minutes_left - dists[(cur_valve, v)] >= 0]
    for new_valve in options:
        new_valve_minutes_left = minutes_left - dists[(cur_valve, new_valve)]
        sub_score = max_value_for_valve(
           open_valves + [new_valve],
           new_valve,
           path_value(open_valves + [new_valve], overall_minutes, dists, valves),
           overall_minutes,
           new_valve_minutes_left,
           valves,
           dists,
           cache)
        scores.append(sub_score)

    return max(scores)


def part1(data):
    valves, edges = parse_data(data)
    positive_valves = {v:r for v,r in valves.items() if r > 0}
    dists = calculate_dists(list(positive_valves.keys()) + ['AA'], edges)
    answer = max_value_for_valve(['AA'], 'AA', 0, 30, 30, positive_valves, dists, {})

    return answer


def part2(data):
    valves, edges = parse_data(data)
    positive_valves = {v:r for v,r in valves.items() if r > 0}
    dists = calculate_dists(list(positive_valves.keys()) + ['AA'], edges)

    cache = {}
    max_value_for_valve(['AA'], 'AA', 0, 26, 26, positive_valves, dists, cache)

    max_flow = 0
    for me, ollie in permutations(cache.keys(), 2):
        if len(set(me).intersection(ollie) - {'AA'}) == 0:
            max_flow = max([max_flow, cache[me] + cache[ollie]])

    return max_flow


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 1651
    assert part2(test_1.splitlines()) == 1707

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines())) # 2316 <-- too low, someone else, 2520
