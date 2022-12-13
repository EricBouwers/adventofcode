#!/usr/bin/env python
import functools
import json

test_1 = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""
test_2 = """"""


def parse_data(data):
    l = None
    r = None
    pairs = []
    for d in data:
        if d and l is None:
            l = json.loads(d)
        elif d and r is None:
            r = json.loads(d)
        else:
            pairs.append((l, r))
            l, r = None, None
    pairs.append((l, r))
    return pairs


def right_order(l, r):
    if isinstance(l, int) and isinstance(r, int):
        return None if l == r else l < r
    elif isinstance(l, list) and isinstance(r, int):
        return right_order(l, [r])
    elif isinstance(l, int) and isinstance(r, list):
        return right_order([l], r)
    else:
        for i, li in enumerate(l):
            if i >= len(r):
                return False
            else:
                compare = right_order(li, r[i])
                if compare is not None:
                    return compare
        return None if len(l) == len(r) else True


def part1(data):
    right_order_count = 0
    for i, pair in enumerate(parse_data(data)):
        right_order_count += i+1 if right_order(*pair) else 0

    return right_order_count


def compare_packets(l, r):
    order = right_order(l, r)
    if order is None:
        return 0
    else:
        return -1 if order else 1


def part2(data):
    packets = [json.loads(d) for d in data if d]
    packets.append([[2]])
    packets.append([[6]])

    packets.sort(key=functools.cmp_to_key(compare_packets))

    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 13
    assert part2(test_1.splitlines()) == 140

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

