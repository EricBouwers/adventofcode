#!/usr/bin/env python

test_1 = """120"""
test_2 = """"""

def parse_data(data):
    return int(data[0])

# fast solution found here https://stackoverflow.com/questions/70635382/fastest-way-to-produce-a-list-of-all-divisors-of-a-number
def get_divisors(N):
    factors = {1}
    maxP  = int(N**0.5)
    p,inc = 2,1
    while p <= maxP:
        while N%p==0:
            factors.update([f*p for f in factors])
            N //= p
            maxP = int(N**0.5)
        p,inc = p+inc,2
    if N>1:
        factors.update([f*N for f in factors])
    return sorted(factors)


def part1(data):
    wanted_presents = parse_data(data)
    for h in range(0, 100000000):
        presents_gotten = sum([e * 10 for e in get_divisors(h)])
        if presents_gotten >= wanted_presents:
            return h


def part2(data, start):
    wanted_presents = parse_data(data)
    for h in range(start, 100000000):
        presents_gotten = sum([e * 11 for e in get_divisors(h) if h // e <= 50])
        if presents_gotten >= wanted_presents:
            return h


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 6
    with open('input') as f:
        data = f.read()

    part1_result = part1(data.splitlines())
    print(part1_result)
    print(part2(data.splitlines(), part1_result))
