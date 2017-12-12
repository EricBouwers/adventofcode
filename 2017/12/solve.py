#!/usr/bin/env python

import sys
import operator as o
from collections import defaultdict

test = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""


def parse(x):
    graph = defaultdict(lambda:[])

    for line in x.split("\n"):
        parts = line.split(" <-> ")
        graph[parts[0]] += parts[1].replace(" ","").split(",")

    return graph


def add_nodes(g, cur, all_nodes):
    if cur not in all_nodes:
        all_nodes.add(cur)
        for n in g[cur]:
            add_nodes(g, n, all_nodes)


def count_nodes(g):
    nodes = set()
    cur_node = '0'

    add_nodes(g, cur_node, nodes)        
    return len(nodes)


def count_groups(g):
    seen_nodes = set()
    todo = set(g.keys())
    groups = 0

    while len(todo) > 0:
        group_nodes = set()
        cur_node = todo.pop()
        add_nodes(g, cur_node, group_nodes)
        
        groups += 1
        todo = todo - group_nodes
    
    return groups


if __name__ == '__main__':
    
    assert count_nodes(parse(test)) == 6
    assert count_groups(parse(test)) == 2

    g = parse(sys.argv[1])
    print count_nodes(g)
    print count_groups(g)

