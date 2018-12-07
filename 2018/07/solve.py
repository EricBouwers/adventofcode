#!/usr/bin/env python

import sys, re, collections

test_input = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""

def get_parsed_data(data):
    pairs = [map(lambda x: x.strip(), re.findall(' [A-Z] ', line)) for line in data.split("\n")]

    all_steps = set([step for pair in pairs for step in pair])

    before = { step : set() for step in all_steps}

    for pair in pairs:
        before[pair[1]].add(pair[0])

    return all_steps, before

def part1(data):

    all_steps, before = get_parsed_data(data)

    steps = [step for step, b in before.items() if len(b) == 0]
    path = "" 
    seen = set()

    while len(path) != len(all_steps):
        steps = sorted(steps)
        path += steps[0]
        seen.add(steps[0])

        steps = [step for step, b in before.items() if len(b - seen) == 0 and step not in seen]

    return path

def part2(data, workers, add_time):

    all_steps, before = get_parsed_data(data)

    steps = [step for step, b in before.items() if len(b) == 0]
    path = "" 
    seen = set()
    seconds = -1 
    timers = {}
    workers = { w:None for w in range(0, workers) }

    for i, step in enumerate(sorted(all_steps)):
        timers[step] = i+1+add_time

    while len(path) != len(all_steps):
        seconds += 1
        
        steps = sorted(steps)
        for w in workers.keys():
            if workers[w] is None and len(steps) > 0:
                workers[w] = steps[0] 
                steps = steps[1:]
        
        for worker, step in [(w,s) for w,s in workers.items() if s is not None]:
            timers[step] -= 1 

            if timers[step] == 0:
                path += step
                seen.add(step)
                workers[worker] = None

                steps = [step for step, b in before.items() if len(b - seen) == 0 and step not in seen and step not in workers.values()]

    return seconds + 1


if __name__ == '__main__':

    assert part1(test_input) == "CABDFE"
    assert part2(test_input, 2, 0) == 15

    data = sys.argv[1]

    print part1(data)
    print part2(data, 5, 60)

