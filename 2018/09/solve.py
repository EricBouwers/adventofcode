#!/usr/bin/env python

import sys, re, collections

def part1(players, points):

    scores = { i:0 for i in range(0,players)}
    current_pos = 3
    board = [0, 2, 1, 3]
    board_len = len(board)

    for i in range(4, points+1):
        player = i % players

        if i % 23 == 0:
            scores[player] += i
            new_pos = current_pos - 7
            current_pos = (board_len + new_pos) if new_pos < 0 else new_pos
            scores[player] += board.pop(current_pos)
            board_len -= 1
            print i, points
        else:
            new_pos = (current_pos + 2) % len(board)
            current_pos = board_len if new_pos == 0 else new_pos
            board.insert(current_pos, i)
            board_len += 1

    return max(scores.values())

def part2(data):
    return None

if __name__ == '__main__':

    import time
    print time.time()
    assert part1(9, 25) == 32
    assert part1(10, 1618) == 8317 
    assert part1(13, 7999) == 146373 
    assert part1(17, 1104) == 2764 
    assert part1(21, 6111) == 54718 
    assert part1(30, 5807) == 37305

    print part1(403, 71920)
    print time.time() 
    print part1(403, 71920*100)
    print time.time() 

