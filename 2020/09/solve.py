#!/usr/bin/env python

test_1 = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def is_in_prevs(nums, idx, preamble):
    cur_num = nums[idx]
    cur_range = nums[idx-preamble:idx]
    for i in cur_range:
        if cur_num - i in cur_range:
            return True
    return False


def part1(data, preamble):
    nums = [int(i.strip()) for i in data]
    idx = preamble
    while is_in_prevs(nums, idx, preamble):
        idx += 1
    return nums[idx]


def part2(data, preamble):
    nums = [int(i.strip()) for i in data]
    find_num = part1(data, preamble)
    for i in range(0, len(nums)):
        cur_sum, j = 0, 0
        while cur_sum < find_num:
            cur_range = nums[i:i+j]
            if sum(cur_range) == find_num:
                print(cur_range)
                return min(cur_range) + max(cur_range)
            else:
                j += 1
                cur_sum = sum(cur_range)


if __name__ == '__main__':

    assert part1(test_1.splitlines(), 5) == 127
    assert part2(test_1.splitlines(), 5) == 62

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines(), 25))
    print(part2(data.splitlines(), 25))

