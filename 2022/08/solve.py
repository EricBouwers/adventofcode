#!/usr/bin/env python

test_1 = """30373
25512
65332
33549
35390"""
test_2 = """"""


def parse_map(data):
    treemap = {}
    for y, row in enumerate(data):
        for x, h in enumerate(row):
            treemap[(x,y)] = int(h)

    return treemap, len(data[0]), len(data)


def part1(data):
    treemap, max_x, max_y = parse_map(data)
    visiblemap = {}

    for row in range(0, max_y):
        max_height = -1
        for c in range(0, max_x):
            if treemap[(c, row)] > max_height:
                visiblemap[(c, row)] = 1
                max_height = treemap[(c, row)]

        max_height = -1
        for c in range(max_x-1, -1, -1):
            if treemap[(c, row)] > max_height:
                visiblemap[(c, row)] = 1
                max_height = treemap[(c, row)]

    for col in range(0, max_x):
        max_height = -1
        for r in range(0, max_y):
            if treemap[(col, r)] > max_height:
                visiblemap[(col, r)] = 1
                max_height = treemap[(col, r)]

        max_height = -1
        for r in range(max_y-1, -1, -1):
            if treemap[(col, r)] > max_height:
                visiblemap[(col, r)] = 1
                max_height = treemap[(col, r)]

    return sum(visiblemap.values())


def take_step(tree, dir):
    return tree[0] + dir[0], tree[1] + dir[1]


def visible_trees(treemap, tree, step, until):
    height = treemap[tree]
    trees = 0

    next_tree = take_step(tree, step)
    while next_tree[0] != until and next_tree[1] != until:
        trees += 1
        if treemap[next_tree] >= height:
            return trees
        else:
            next_tree = take_step(next_tree, step)

    return trees


def part2(data):
    treemap, max_x, max_y = parse_map(data)
    scenic_map = {}

    directions_to_check = {(1, 0): max_x, (0, 1): max_y, (-1, 0): -1, (0, -1): -1}
    for tree in treemap.keys():
        scenic_score = 1
        for step, until in directions_to_check.items():
            scenic_score *= visible_trees(treemap, tree, step, until)
        scenic_map[tree] = scenic_score

    return max(scenic_map.values())


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 21
    assert part2(test_1.splitlines()) == 8

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

