#!/usr/bin/env python
from collections import deque

test_1 = """1
2
-3
3
-2
0
4"""
test_2 = """"""


def parse_data(data):
    return [int(d) for d in data]


def unmix(nums, rounds):
    unique_num_dict = {str(num) + "_" + str(i): num for i, num in enumerate(nums)}
    unique_nums = [str(num) + "_" + str(i) for i, num in enumerate(nums)]
    mixed = deque(unique_nums)

    num_len = len(nums)
    for i in range(0, num_len*rounds):
        cur_num = nums[i % num_len]
        unique_num = str(cur_num) + "_" + str(i % num_len)

        cur_i = mixed.index(unique_num)

        mixed.rotate(-cur_i)
        val = mixed.popleft()

        mixed.rotate(-unique_num_dict[val])
        mixed.insert(0, val)

    zero_unique = "0_" + str(nums.index(0))
    cur_i = mixed.index(zero_unique)
    mixed.rotate(-cur_i)

    coordinate = 0
    mixed.rotate(-1000)
    coordinate += unique_num_dict[mixed[0]]
    mixed.rotate(-1000)
    coordinate += unique_num_dict[mixed[0]]
    mixed.rotate(-1000)
    coordinate += unique_num_dict[mixed[0]]

    return coordinate


def part1(data):
    nums = parse_data(data)
    return unmix(nums, 1)


def part2(data):
    nums = [x * 811589153 for x in parse_data(data)]
    return unmix(nums, 10)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 3
    assert part2(test_1.splitlines()) == 1623178306

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines())) # -978 is incorrect
    print(part2(data.splitlines()))

