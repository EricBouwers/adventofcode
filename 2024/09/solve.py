#!/usr/bin/env python

test_1 = """2333133121414131402"""
test_2 = """"""


def parse_data(data):
    counts = [int(c) for c in data]
    blocks = []
    empties = []
    all_sequential = []

    for file_id, i in enumerate(range(0, len(counts), 2)):
        blocks.append([counts[i], file_id])
        all_sequential.append([counts[i], file_id, False])
        if i + 1 < len(counts):
            empties.append(counts[i + 1])
            all_sequential.append([counts[i+1], 0, True])

    return blocks, empties, all_sequential


def part1(data):
    blocks, empties, _ = parse_data(data)
    cur_block = blocks.pop(0)
    end_block = blocks.pop()
    in_empty = False
    checksum = 0
    cur_i = 0

    while cur_block != end_block or end_block[0] > 0:
        if in_empty:
            to_fill = empties.pop(0)
            for i in range(0, to_fill):
                if end_block[0] == 0:
                    end_block = blocks.pop() if blocks else cur_block
                checksum += cur_i * end_block[1] if end_block[0] > 0 else 0
                end_block[0] -= 1
                cur_i += 1
            in_empty = False
        else:
            for i in range(cur_block[0]):
                checksum += cur_i * cur_block[1]
                cur_i += 1
                cur_block[0] -= 1
            cur_block = blocks.pop(0) if blocks else end_block
            in_empty = True

    return checksum


def defrag(blocks, file_id):
    while file_id > 0:
        block = [b for b in blocks if b[1] == file_id][0]
        new_blocks = []
        processed = False
        for b in blocks:
            if b == block:
                new_blocks.append([b[0], 0, True] if processed else b)
                processed = True
            elif not processed and b[2]:
                if b[0] >= block[0]:
                    new_blocks.append(block)
                    if b[0] - block[0] > 0:
                        new_blocks.append([b[0] - block[0], 0, True])
                    processed = True
                else:
                    new_blocks.append(b)
            else:
                new_blocks.append(b)

        blocks = new_blocks
        file_id -= 1

    return blocks


def part2(data):
    _, __, blocks = parse_data(data)

    blocks = defrag(blocks, max([b[1] for b in blocks if not b[2]]))
    cur_block = blocks.pop(0)
    checksum = 0
    cur_i = 0
    while cur_block:
        for i in range(cur_block[0]):
            checksum += cur_i * cur_block[1]
            cur_i += 1
        cur_block = blocks.pop(0) if blocks else None

    return checksum


if __name__ == '__main__':

    assert part1(test_1.splitlines()[0]) == 1928
    assert part2(test_1.splitlines()[0]) == 2858

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()[0]))
    print(part2(data.splitlines()[0]))
