#!/usr/bin/env python
from collections import defaultdict

test_1 = """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#.."""
test_2 = """"""


def parse_data(data):
    elves = []
    for y, d in enumerate(data):
        for x, e in enumerate(d):
            if e == "#":
                elves.append((x, y))
    return elves


def print_region(elves):
    min_x = min([c[0] for c in elves])
    min_y = min([c[1] for c in elves])
    max_x = max([c[0] for c in elves])
    max_y = max([c[1] for c in elves])

    for y in range(min_y, max_y+1):
        line = []
        for x in range(min_x, max_x+1):
            line.append("#" if (x,y) in elves else ".")
        print("".join(line))


def part1(data, rounds=10):
    elves = parse_data(data)

    get_neighbours = lambda x, y: [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]
    to_check_list = [[0, 1, 2], [4, 5, 6], [0, 7, 6], [2, 3, 4]]
    for i in range(0, rounds):

        proposals = defaultdict(list)
        for elf in elves:
            neighbours = get_neighbours(*elf)
            surrounding = [e in elves for e in neighbours]
            if sum(surrounding) == 0:
                proposals[elf].append(elf)
            else:
                proposal = None
                cur_check = 0
                while proposal is None and cur_check < 4:
                    check_list = to_check_list[cur_check]
                    if sum([surrounding[p] for p in check_list]) == 0:
                        proposal = neighbours[check_list[1]]
                    cur_check += 1
                if proposal is not None:
                    proposals[proposal].append(elf)
                else:
                    proposals[elf].append(elf)

        new_elves = []
        for k, v in proposals.items():
            if len(v) == 1:
                new_elves.append(k)
            else:
                new_elves += v

        if new_elves == elves:
            return i+1
        else:
            elves = new_elves

        rotate_check = to_check_list.pop(0)
        to_check_list.append(rotate_check)

    min_x = min([c[0] for c in elves])
    min_y = min([c[1] for c in elves])
    max_x = max([c[0] for c in elves])
    max_y = max([c[1] for c in elves])

    empty = 0
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            empty += (x, y) not in elves

    return empty


def part2(data):
    return part1(data, 10000)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 110
    assert part2(test_1.splitlines()) == 20

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

