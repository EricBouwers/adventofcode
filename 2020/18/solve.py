#!/usr/bin/env python

test_1 = """1 + 2 * 3 + 4 * 5 + 6"""
test_2 = """2 * 3 + (4 * 5)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""
test_3 = """"""
test_4 = """"""


class MyNum1:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return MyNum1(self.n + other.n)

    def __sub__(self, other):
        return MyNum1(self.n * other.n)


class MyNum2:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return MyNum2(self.n * other.n)

    def __mul__(self, other):
        return MyNum2(self.n + other.n)


def evaluate_line(line, c):
    line = line.replace('(', ' ( ')
    line = line.replace(')', ' ) ')
    line = ''.join(c + "(" + p + ")" if p.isdigit() else p for p in line.split(" "))
    return eval(line).n


def part1(data):
    sums = []
    for line in data:
        line = line.replace('*', '-')
        sums.append(evaluate_line(line, 'MyNum1'))
    return sum(sums)


def part2(data):
    sums = []
    for line in data:
        line = line.replace('*', '-')
        line = line.replace('+', '*')
        line = line.replace('-', '+')
        sums.append(evaluate_line(line, 'MyNum2'))
    return sum(sums)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 71
    assert part1(test_2.splitlines()) == 25898
    assert part2(test_1.splitlines()) == 231
    assert part2(test_2.splitlines()) == 46+669060+23340

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

