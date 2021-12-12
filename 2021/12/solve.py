#!/usr/bin/env python
from collections import defaultdict
from functools import reduce
from operator import add

test_1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
test_2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""
test_3 = """"""
test_4 = """"""


def part1(data):
    edges = defaultdict(list)
    for edge in data:
        ft = edge.split("-")
        edges[ft[0]].append(ft[1])
        edges[ft[1]].append(ft[0])

    complete_paths = set()
    to_explore = [["start"]]
    while to_explore:
        cur_path = to_explore.pop()
        if cur_path[-1] == "end":
            complete_paths.add(",".join(cur_path))
        else:
            for next_step in edges[cur_path[-1]]:
                if (next_step.islower() and next_step not in cur_path) or next_step.isupper():
                    to_explore.append(cur_path + [next_step])

    return len(complete_paths)


def part2(data):
    edges = defaultdict(list)
    for edge in data:
        ft = edge.split("-")
        if ft[1] != "start":
            edges[ft[0]].append(ft[1])
        if ft[0] != "start":
            edges[ft[1]].append(ft[0])

    complete_paths = set()
    to_explore = [(["start"], False)]
    while to_explore:
        cur_path, has_small_cave_twice = to_explore.pop()
        if cur_path[-1] == "end":
            complete_paths.add(",".join(cur_path))
        else:
            for next_step in edges[cur_path[-1]]:
                if next_step.islower():
                    if next_step not in cur_path:
                        to_explore.append((cur_path + [next_step], has_small_cave_twice))
                    elif not has_small_cave_twice:
                        to_explore.append((cur_path + [next_step], True))
                else:
                    to_explore.append((cur_path + [next_step], has_small_cave_twice))

    return len(complete_paths)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 10
    assert part1(test_2.splitlines()) == 19
    assert part2(test_1.splitlines()) == 36
    assert part2(test_2.splitlines()) == 103

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

