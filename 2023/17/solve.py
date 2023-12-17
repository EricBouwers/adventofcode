#!/usr/bin/env python
import heapq
from collections import defaultdict
from heapq import heapify

test_1 = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""
test_2 = """111111111111
999999999991
999999999991
999999999991
999999999991"""


def parse_data(data):
    grid = {}
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = int(c)
    return grid


LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

POSSIBLE_STEPS = {
    LEFT: [LEFT, UP, DOWN],
    RIGHT: [RIGHT, UP, DOWN],
    UP: [LEFT, RIGHT, UP],
    DOWN: [LEFT, RIGHT, DOWN],
}


def take_step(p1, p2):
    return p1[0]+p2[0], p1[1]+p2[1]


def get_possible_steps1(grid, cur_pos, last_dir, dir_steps):
    possible_steps = []
    for poss_dir in POSSIBLE_STEPS[last_dir]:
        next_pos = take_step(poss_dir, cur_pos)
        if next_pos in grid and (poss_dir != last_dir or dir_steps < 3):
            possible_steps.append(poss_dir)

    return possible_steps


def get_possible_steps2(grid, cur_pos, last_dir, dir_steps):
    possible_steps = []
    if dir_steps < 4:
        next_pos = take_step(last_dir, cur_pos)
        return [last_dir] if next_pos in grid else []
    else:
        for poss_dir in POSSIBLE_STEPS[last_dir]:
            next_pos = take_step(poss_dir, cur_pos)
            if next_pos in grid and (poss_dir != last_dir or dir_steps < 10):
                possible_steps.append(poss_dir)

        return possible_steps


def man_dist(x, y):
    return sum([abs(x[i] - y[i]) for i in range(0, 2)])


def part1(data):
    grid = parse_data(data)

    states = [(0, (0, 0), RIGHT, 0), (0, (0, 0), DOWN, 0)]
    heapify(states)
    end = (len(data[0]) - 1, len(data) - 1)

    seens = {}
    while len(states) > 0:
        cur_loss, cur_pos, cur_dir, dir_steps = heapq.heappop(states)
        if cur_pos == end:
            return cur_loss
        else:
            possible_steps = get_possible_steps1(grid, cur_pos, cur_dir, dir_steps)
            for step in possible_steps:
                next_pos = take_step(cur_pos, step)
                next_loss = cur_loss + grid[next_pos]
                dir_steps_taken = 1 if step != cur_dir else (dir_steps + 1)
                next_key = (next_pos, step, dir_steps_taken)
                if next_key not in seens or seens[next_key] > next_loss:
                    seens[next_key] = next_loss
                    heapq.heappush(states, (next_loss, next_pos, step, dir_steps_taken))


def part2(data):
    grid = parse_data(data)

    states = [(0, (0, 0), RIGHT, 0), (0, (0, 0), DOWN, 0)]
    heapify(states)
    end = (len(data[0]) - 1, len(data) - 1)

    seens = {}
    while len(states) > 0:
        cur_loss, cur_pos, cur_dir, dir_steps = heapq.heappop(states)
        if cur_pos == end and dir_steps >= 4:
            return cur_loss
        else:
            possible_steps = get_possible_steps2(grid, cur_pos, cur_dir, dir_steps)
            for step in possible_steps:
                next_pos = take_step(cur_pos, step)
                next_loss = cur_loss + grid[next_pos]
                dir_steps_taken = 1 if step != cur_dir else (dir_steps + 1)
                next_key = (next_pos, step, dir_steps_taken)
                if next_key not in seens or seens[next_key] > next_loss:
                    seens[next_key] = next_loss
                    heapq.heappush(states, (next_loss, next_pos, step, dir_steps_taken))


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 102
    assert part2(test_1.splitlines()) == 94
    assert part2(test_2.splitlines()) == 71

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

