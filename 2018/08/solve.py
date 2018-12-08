#!/usr/bin/env python

import sys, re

class Node:

    def __init__(self):
        self.meta = []
        self.children = []

    def __str__(self):
        m = "meta: " + ",".join(map(str, self.meta))
        c = "children: (" + str(len(self.children)) +  ") " +  ",".join(map(str, self.children))
        return m + " - " + c

    def meta_sum(self):
        return sum(self.meta) + sum([c.meta_sum() for c in self.children])

    def val_sum(self):
        value = 0
        
        if len(self.children) == 0:
            value = sum(self.meta)
        else:
            child_count = len(self.children)
            for c in map(lambda x: x - 1, self.meta):
                if c < child_count:
                    value += self.children[c].val_sum()

        return value

def parse_nodes(nums):

    meta_sum = 0
    
    childs = nums[0]
    len_meta = nums[1]
    nums = nums[2:]
    parent = Node()

    stack = []

    while len(nums) > 0:
        if childs == 0:
            parent.meta = nums[0:len_meta]    
            nums = nums[len_meta:]
            if len(nums) > 0:
                childs, len_meta, old_parent = stack.pop()
                old_parent.children.append(parent)
                parent = old_parent
                
        else:
            childs -= 1
            stack.append((childs, len_meta, parent))

            childs = nums[0]
            len_meta = nums[1]
            nums = nums[2:]
            parent = Node()

    return parent

def part1(data):
    nums = map(int, data.split(" "))
    tree = parse_nodes(nums)

    return tree.meta_sum()

def part2(data):
    nums = map(int, data.split(" "))
    tree = parse_nodes(nums)

    return tree.val_sum()

if __name__ == '__main__':

    assert part1("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2") == 138
    assert part2("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2") == 66

    data = sys.argv[1]

    print part1(data)
    print part2(data)

