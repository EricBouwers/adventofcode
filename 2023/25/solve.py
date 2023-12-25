#!/usr/bin/env python
import networkx as nx

test_1 = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr"""
test_2 = """"""


def parse_data(data):
    graph = {}

    for line in data:
        parts = line.split(": ")
        graph[parts[0]] = parts[1].split()

    return graph


def part1(data):
    graph = parse_data(data)

    node_names = set()
    g = nx.Graph()
    for k, v in graph.items():
        node_names.add(k)
        for t in v:
            node_names.add(t)
            g.add_edge(k, t, capacity=1.0),

    node_names = [x for x in node_names]
    first_node = node_names[0]
    for node in node_names[1:]:
        cut_value, partition = nx.minimum_cut(g, first_node, node)
        if cut_value == 3:
            return len(partition[0]) * len(partition[1])



def part2(data):
    parsed = parse_data(data)
    return None


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 54
    assert part2(test_1.splitlines()) == None

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

