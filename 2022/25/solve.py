#!/usr/bin/env python

test_1 = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""
test_2 = """"""


SNAFUS = {
    "2": 2, "1": 1, "0": 0, "-": -1, "=": -2
}


def part1(data):
    sum_snafu = 0
    for d in data:
        snafu = 0
        pos = 1
        for c in reversed(d):
            snafu += pos * SNAFUS[c]
            pos *= 5
        sum_snafu += snafu

    return to_snafu(sum_snafu)


def to_snafu(n, step=None):
    if step is None:
        step = 1
        while step*2 < n:
            step *= 5
    elif step == 0:
        step = 1

    new_ns = [n + 2*step, n + step, n, n - step, n - 2 * step]
    new_ns_abs = [abs(x) for x in new_ns]
    min_ns = min(new_ns_abs)
    index_ns = new_ns_abs.index(min_ns)
    new_char = ["=", "-", "0", "1", "2"][index_ns]

    if new_ns[index_ns] == 0 and step == 1:
        return new_char
    else:
        return new_char + to_snafu(new_ns[index_ns], step / 5)


def part2(data):
    return None


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == "2=-1=0"
    assert part2(test_1.splitlines()) == None

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

