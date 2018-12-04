#!/usr/bin/env python

import sys, re, collections

test_input_1 = """
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
"""

def get_guard_data(data): 
    guard_minutes = {}
    guard_total = {}
    cur_guard = None
    cur_minutes = None
    begin = None
    end = None

    for line in data.split("\n"):
        digits = map(int, re.findall("\d+", line))
        
        if "Guard" in line:
            cur_guard = digits[-1]
            begin = None
            end = None

        if "falls" in line:
            begin = digits[-1]

        if "wakes" in line:
            if cur_guard not in guard_minutes.keys():
                cur_minutes = collections.Counter()
                guard_minutes[cur_guard] = cur_minutes
                guard_total[cur_guard] = 0
            else:
                cur_minus = guard_minutes[cur_guard]
            
            end = digits[-1]
            guard_total[cur_guard] += end - begin
            guard_minutes[cur_guard].update(range(begin, end))
            begin = None

    return guard_total, guard_minutes


def part1(data):
    guard_total, guard_minutes = get_guard_data(data)

    best_guard = collections.Counter(guard_total).most_common()[0][0]
    most_minutes = guard_minutes[best_guard].most_common()[0][0]

    return best_guard * most_minutes


def part2(data):
    guard_total, guard_minutes = get_guard_data(data)

    totals = collections.Counter()
    for gid,counter in guard_minutes.items():
        most = counter.most_common()[0]
        totals.update([gid*most[0]] * most[1])

    return totals.most_common()[0][0] 

if __name__ == '__main__':

    assert part1(test_input_1) == 240
    assert part2(test_input_1) == 4455

    data = sys.argv[1]

    print part1(data)
    print part2(data)

