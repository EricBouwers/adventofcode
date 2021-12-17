#!/usr/bin/env python

test_1 = """target area: x=20..30, y=-10..-5"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def hits_target(v, target_area, x_end, y_end):
    pos = (0, 0)
    path = []
    while pos[0] < x_end and pos[1] > y_end:
        pos = (pos[0] + v[0], pos[1] + v[1])
        v = (v[0] + (1 if v[0] < 0 else -1 if v[0] > 0 else 0), v[1] - 1)
        path.append(pos)
        if pos in target_area:
            return path

    return None


def part1(x_min, x_max, y_min, y_max):
    target_area = {
        (x, y) for x in range(x_min, x_max+1) for y in range(y_min, y_max+1)
    }

    paths = {}
    for v in [(x, y) for x in range(0, x_max+1) for y in range(y_min-1, -y_min+1)]:
        path = hits_target(v, target_area, max(x_min, x_max), min(y_max, y_min))
        if path is not None:
            paths[v] = path

    return max([max([y for x, y in path]) for path in paths.values()])


def part2(x_min, x_max, y_min, y_max):
    target_area = {
        (x, y) for x in range(x_min, x_max+1) for y in range(y_min, y_max+1)
    }

    paths = {}
    for v in [(x, y) for x in range(0, x_max+1) for y in range(y_min-1, -y_min+1)]:
        path = hits_target(v, target_area, max(x_min, x_max), min(y_max, y_min))
        if path is not None:
            paths[v] = path
    return len(paths.keys())


if __name__ == '__main__':

    assert part1(20, 30, -10, -5) == 45
    assert part2(20, 30, -10, -5) == 112

    with open('input') as f:
        data = f.read()

    print(part1(282, 314, -80, -45))
    print(part2(282, 314, -80, -45))

