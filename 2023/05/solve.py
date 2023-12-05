#!/usr/bin/env python

test_1 = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
test_2 = """"""


def create_func(start1, start2, range):
    change = (start1 - start2) if start1 < start2 else abs(start2 - start1)
    return lambda x: x + change if start2 <= x <= (start2 + range) else x


def create_reverse_func(start1, start2, range):
    change = abs(start1 - start2) if start1 < start2 else (start2 - start1)
    return lambda x: x + change if start1 <= x <= (start1 + range) else x


def parse_data(data):
    seeds = [int(s) for s in data[0].split(": ")[1].split(" ")]
    function_lists = []
    rev_function_lists = []

    cur_list = []
    cur_rev_list = []
    for line in data[1:]:
        if line == "" and cur_list:
            function_lists.append(cur_list)
            cur_list = []

            rev_function_lists.append(cur_rev_list)
            cur_rev_list = []
        elif line and line[0].isdigit():
            digits = [int(d) for d in line.split(" ")]
            cur_list.append(create_func(*digits))
            cur_rev_list.append(create_reverse_func(*digits))

    function_lists.append(cur_list)
    rev_function_lists.append(cur_rev_list)

    return seeds, function_lists, rev_function_lists


def calc_locations(seeds, function_lists):
    transformed = []
    for seed in seeds:
        for function_list in function_lists:
            applied = False
            for function in function_list:
                if not applied:
                    new_seed = function(seed)
                    if new_seed != seed:
                        seed = new_seed
                        applied = True

        transformed.append(seed)

    return transformed


def part1(data):
    seeds, function_lists, _ = parse_data(data)
    transformed = calc_locations(seeds, function_lists)
    return min(transformed)


def part2(data):
    seeds, _, function_lists = parse_data(data)

    ranges = []
    for x in range(0, len(seeds), 2):
        ranges.append((seeds[x], seeds[x]+seeds[x+1]))

    for seed in range(0, 579440000):
        location = seed
        for function_list in reversed(function_lists):
            applied = False
            for function in function_list:
                if not applied:
                    new_seed = function(seed)
                    if new_seed != seed:
                        seed = new_seed
                        applied = True
        for r in ranges:
            if r[0] <= seed <= r[1]:
                return location


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 35
    assert part2(test_1.splitlines()) == 46

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

