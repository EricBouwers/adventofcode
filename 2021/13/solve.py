#!/usr/bin/env python
from collections import defaultdict

test_1 = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def print_map(m, max_x, max_y):
    for y in range(0, max_y+1):
        line = ''
        for x in range(0, max_x+1):
            line += "#" if m[(y, x)] == 1 else "."
        print(line)


def parse_data(data):
    paper = defaultdict(lambda: 0)
    folds = []
    max_x = 0
    max_y = 0
    for d in data:
        if d.startswith("fold along "):
            folds.append(d)
        elif d:
            c = d.split(",")
            paper[(int(c[1]), int(c[0]))] = 1
            max_x = max(max_x, int(c[0]))
            max_y = max(max_y, int(c[1]))
    return paper, folds, max_x, max_y


def fold_paper(paper, fold, max_x, max_y):
    fold = fold.split("=")
    start = int(fold[1])

    if fold[0].endswith("y"):
        for x in range(0, max_x+1):
            for y in range(0, max_y-start+1):
                paper[(start - y, x)] = max(paper[(start + y, x)], paper[(start - y, x)])
        max_y = max_y - start - 1
    else:
        for y in range(0, max_y+1):
            for x in range(0, max_x-start+1):
                paper[(y, start-x)] = max(paper[(y, start-x)], paper[(y, start+x)])
        max_x = max_x - start - 1

    return paper, max_x, max_y


def part1(data):
    paper, folds, max_x, max_y = parse_data(data)
    paper, max_x, max_y = fold_paper(paper, folds[0], max_x, max_y)
    return sum([v for k,v in paper.items() if k[0] <= max_y and k[1] <= max_x])


def part2(data):
    paper, folds, max_x, max_y = parse_data(data)
    for f in folds:
        paper, max_x, max_y = fold_paper(paper, f, max_x, max_y)
    print_map(paper, max_x, max_y)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 17

    with open('input') as f:
        data = f.read()

    # not 647
    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

