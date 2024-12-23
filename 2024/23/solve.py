#!/usr/bin/env python
from collections import defaultdict

test_1 = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""
test_2 = """"""


def parse_data(data):
    graph = defaultdict(list)
    for d in data:
        f, t = d.split("-")
        graph[f].append(t)
        graph[t].append(f)
    return graph


def find_components(graph):
    components = set()
    for n in graph.keys():
        for nb1 in graph[n]:
            for nb2 in graph[nb1]:
                if n in graph[nb2]:
                    components.add(tuple(sorted([n, nb1, nb2])))
    return components


def is_valid(option, graph):
    for n in option:
        if len(set(option) - set(graph[n] + [n])) > 0:
            return False

    return True


def part1(data):
    graph = parse_data(data)
    components = find_components(graph)
    return len([c for c in components if c[0].startswith('t') or ',t' in ','.join(list(c))])


def part2(data):
    graph = parse_data(data)

    to_test = [n for n in graph.keys()]
    biggest = []
    while to_test:
        to_check = to_test.pop()
        options = [graph[to_check] + [to_check]]
        while options:
            option = options.pop()
            if is_valid(option, graph):
                biggest = option
            elif len(option) - 1 > len(biggest):
                for x in option:
                    options.append([y for y in option if y != x])

    return ','.join(sorted(biggest))


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 7
    assert part2(test_1.splitlines()) == "co,de,ka,ta"

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

