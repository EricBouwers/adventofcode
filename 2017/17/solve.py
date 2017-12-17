#!/usr/bin/env python

import sys


def process(steps):
    result = [0, 1]
    index = 1

    for i in range(2, 2018):
        index = (index + steps) % i
        result.insert(index+1, i)
        index += 1

    return result[index + 1]


def process_two(steps):
    result = 1
    index = 1

    for i in range(2, 50000000):
        index = (index + steps) % i
        if index == 0:
            result = i
        index += 1

    return result


if __name__ == '__main__':
    
    assert process(3) == 638
    print process(366)
    print process_two(366)


