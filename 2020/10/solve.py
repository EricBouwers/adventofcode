#!/usr/bin/env python
from functools import reduce
from operator import mul, add

test_1 = """16
10
15
5
1
11
7
19
6
12
4"""
test_2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


def part1(data):
    jolts = sorted([int(j) for j in data])
    cur_jolt = 0
    one_diff, three_diff = 0, 1
    for jolt in jolts:
        if (jolt - cur_jolt) == 1:
            one_diff += 1
        else:
            three_diff += 1
        cur_jolt = jolt

    return one_diff * three_diff


def paths(node, graph, seen):
    if node in seen:
        return seen[node]

    if len(graph[node]) == 0:
        seen[node] = 1
        return paths(node, graph, seen)
    else:
        seen[node] = 1 + (reduce(add, [paths(x, graph, seen) for x in graph[node]]))
        return paths(node, graph, seen)


def part2(data):
    jolts = sorted([int(j) for j in data], reverse=True)
    to_jumps = {x: [y for y in [x + 1, x + 2, x + 3] if y in jolts] for x in jolts}
    from_jumps = {x: [y for y in [x - 1, x - 2, x - 3] if y in jolts] for x in jolts}

    num_paths = {jolts[0]: 1, 1: 0, 2: 0, 3: 0}
    next_visit = from_jumps[jolts[0]]
    while len(next_visit) > 0:
        cur_node = next_visit.pop(0)
        next_visit = next_visit + [y for y in from_jumps[cur_node] if y not in next_visit]
        num_paths[cur_node] = sum([num_paths[x] for x in to_jumps[cur_node]])

    return num_paths[1] + num_paths[2] + num_paths[3]


if __name__ == '__main__':
    assert part1(test_1.splitlines()) == 35
    assert part1(test_2.splitlines()) == 220
    assert part2(test_1.splitlines()) == 8
    assert part2(test_2.splitlines()) == 19208

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
