#!/usr/bin/env python

import sys
import itertools as it

example = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""

def parse_input(lines):
    nodes = {}
    edges = {}
    for l in lines.split("\n"):
        parts = l.split(" -> ")
        node_parts = parts[0].split(" (")
        nodes[node_parts[0]] = int(node_parts[1].replace(")",""))
        
        if len(parts) > 1:
            edges[node_parts[0]] = parts[1].split(", ")

    return nodes,edges


def bottom_program(lines):
    nodes, edges = parse_input(lines)

    all_edges = []
    for e in edges.values():
        all_edges += e
    
    for n in nodes:
        if n not in all_edges:
            return n
    
    return None

def weight_problem(lines):
    nodes, edges = parse_input(lines)

    node_total_weights = {}
    is_balanced = {}
    for n in nodes:
        add_weight(n, edges, nodes, node_total_weights, is_balanced)

    source_node = None
    for e in edges:
        if not is_balanced[e] and all([is_balanced[l] for l in edges[e]]):
            source_node = e

    leave_weights = [node_total_weights[l] for l in edges[source_node]]    
    max_weight = max(leave_weights)
    min_weight = min(leave_weights)
    offending_weight = max_weight if leave_weights.count(max_weight) < leave_weights.count(min_weight) else min_weight
    weight_diff = max_weight - min_weight
    for l in edges[source_node]:
        if node_total_weights[l] == offending_weight:     
            return nodes[l] - weight_diff

def add_weight(node, edges, own_weights, all_weights, is_balanced):
    leaves = edges.get(node,[])
    all_weights[node] = own_weights[node]

    leave_weights = []
    for l in leaves:
        if l not in all_weights:
            add_weight(l, edges, own_weights, all_weights, is_balanced)
        all_weights[node] += all_weights[l]    
        leave_weights.append(all_weights[l])

    is_balanced[node] = all([w == min(leave_weights) for w in leave_weights])


if __name__ == '__main__':
    assert bottom_program(example) == "tknk"
    assert weight_problem(example) == 60

    print bottom_program(sys.argv[1])
    print weight_problem(sys.argv[1])

