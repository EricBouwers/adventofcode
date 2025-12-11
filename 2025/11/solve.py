#!/usr/bin/env python
from collections import defaultdict

test_1 = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""
test_2 = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""


def parse_data(data):
    from_to = defaultdict(list)
    to_from = defaultdict(list)
    for d in data:
        parts = d.split(": ")
        from_node = parts[0]
        to_nodes = parts[1].split(" ")
        from_to[from_node] = to_nodes
        for to_node in to_nodes:
            to_from[to_node].append(from_node)

    return from_to, to_from


def find_nr_of_paths(target_node, from_node, network, memory, allowed_nodes=None):
    new_nodes = network.get(from_node)
    if not new_nodes:
        return 0
    else:
        total_paths = 0
        nodes_to_visit = network[from_node]
        if allowed_nodes is not None:
            nodes_to_visit = [n for n in nodes_to_visit if n in allowed_nodes]

        for to_node in nodes_to_visit:
            if to_node == target_node:
                total_paths += 1
            else:
                if to_node not in memory:
                    memory[to_node] = find_nr_of_paths(target_node, to_node, network, memory, allowed_nodes)
                total_paths += memory[to_node]
        return total_paths


def part1(data):
    from_to, to_from = parse_data(data)

    target_node = "out"
    from_node = "you"

    return find_nr_of_paths(target_node, from_node, from_to, {})


def part2(data):
    from_to, to_from = parse_data(data)

    reachable_from_dac = set()
    reachable_from_dac.add("dac")
    reachable_from_fft = set()
    reachable_from_fft.add("fft")

    for i in range(0, 20):
        for node in [x for x in reachable_from_dac]:
            reachable_from_dac.update(to_from[node])

    for i in range(0, 20):
        for node in [x for x in reachable_from_fft]:
            reachable_from_fft.update(from_to[node])

    nodes_to_follow = reachable_from_fft.intersection(reachable_from_dac)

    step_1 = find_nr_of_paths("out", "dac", from_to, {})
    step_2 = find_nr_of_paths("dac", "fft", from_to, {}, nodes_to_follow)
    step_3 = find_nr_of_paths("svr", "fft", to_from, {})

    return step_1 * step_2 * step_3


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 5
    assert part2(test_2.splitlines()) == 2

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

