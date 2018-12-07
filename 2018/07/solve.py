#!/usr/bin/env python

import sys, re, collections

test_input = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""

def part1(data):

    pairs = [map(lambda x: x.strip(), re.findall(' [A-Z] ', line)) for line in data.split("\n")]

    all_steps = set([step for pair in pairs for step in pair])

    follow = { step : set() for step in all_steps}
    before = { step : set() for step in all_steps}

    for pair in pairs:
        follow[pair[0]].add(pair[1])
        before[pair[1]].add(pair[0])

    steps = [step for step, b in before.items() if len(b) == 0]
    path = "" 
    seen = set()

    while len(path) != len(all_steps):
        steps = sorted(steps)
        path += steps[0]
        seen.add(steps[0])

        steps = [step for step, b in before.items() if len(b - seen) == 0 and step not in seen]

    return path

def part2(data):
    return None

if __name__ == '__main__':

    assert part1(test_input) == "CABDFE"
    assert part2("") == None

    data = sys.argv[1]

    print part1(data)
    print part2(data)

