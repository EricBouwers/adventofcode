#!/usr/bin/env python

import sys, re, collections

def part1(players, points):

    scores = { i:0 for i in range(0,players)}
    board = collections.deque([0, 2, 1, 3])

    for i in range(4, points+1):
        player = i % players

        if i % 23 == 0:
            scores[player] += i
            board.rotate(7)
            scores[player] += board.popleft()
        else:
            board.rotate(-2)
            board.appendleft(i)

    return max(scores.values())

if __name__ == '__main__':

    assert part1(9, 25) == 32
    assert part1(10, 1618) == 8317 
    assert part1(13, 7999) == 146373 
    assert part1(17, 1104) == 2764 
    assert part1(21, 6111) == 54718 
    assert part1(30, 5807) == 37305

    print part1(403, 71920)
    print part1(403, 71920*100)

