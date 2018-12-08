#!/usr/bin/env python

import sys, re

class Node:

    def __init__(self, children, meta):
        self.meta = meta
        self.children = children

    def __str__(self):
        m = "meta: " + ",".join(map(str, self.meta))
        c = "children: (" + str(len(self.children)) +  ") " +  ",".join(map(str, self.children))
        return m + " - " + c


def parse_nodes(nums):

    meta_sum = 0
    
    childs = nums[0]
    len_meta = nums[1]
    nums = nums[2:]
    
    stack = []

    while len(nums) > 0:
        if childs == 0:
            meta_sum += sum(nums[0:len_meta])    
            nums = nums[len_meta:]
            if len(nums) > 0:
                childs, len_meta = stack.pop()
                
        else:
            childs -= 1
            stack.append((childs, len_meta))

            childs = nums[0]
            len_meta = nums[1]
            nums = nums[2:]

    return meta_sum

def part1(data):
    nums = map(int, data.split(" "))
    meta_sum = parse_nodes(nums)

    return meta_sum

def part2(data):
    return None

if __name__ == '__main__':

    assert part1("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2") == 138
    assert part2("") == None

    data = sys.argv[1]

    print part1(data)
    print part2(data)

