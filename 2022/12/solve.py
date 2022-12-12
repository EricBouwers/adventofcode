#!/usr/bin/env python

test_1 = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
test_2 = """"""

def parse_map(data):
    hmap = {}
    start = None
    end = None

    for y, d in enumerate(data):
        for x, h in enumerate(d):
            if h == 'S':
                start = (x, y)
                hmap[(x, y)] = ord('a')
            elif h == 'E':
                end = (x, y)
                hmap[(x, y)] = ord('z')
            else:
                hmap[(x, y)] = ord(h)
    return hmap, start, end


def get_possible_steps(hmap, cur_pos, distance):
    new_pos = [
        (cur_pos[0], cur_pos[1]+1),
        (cur_pos[0]+1, cur_pos[1]),
        (cur_pos[0], cur_pos[1]-1),
        (cur_pos[0]-1, cur_pos[1]),
    ]

    return [(distance+1, step) for step in new_pos if step in hmap and hmap[step] - hmap[cur_pos] < 2]


def find_shortest(hmap, start, end, cur_shortest):
    states = [(0, start)]
    seen_states = set()

    while len(states) > 0:
        current_state = states.pop(0)

        while current_state[1] in seen_states and states:
            current_state = states.pop(0)
        seen_states.add(current_state[1])

        cur_pos = current_state[1]
        if cur_pos[0] == end[0] and cur_pos[1] == end[1]:
            return current_state[0]
        elif current_state[0] > cur_shortest:
            return cur_shortest + 1
        else:
            states += get_possible_steps(hmap, current_state[1], current_state[0])


def part1(data):
    hmap, start, end = parse_map(data)
    return find_shortest(hmap, start, end, 10**10000)


def part2(data):
    hmap, start, end = parse_map(data)
    starts = [k for k, v in hmap.items() if v == ord('a')]

    shortest = 10**10000
    for s in starts:
        s_dist = find_shortest(hmap, s, end, shortest)
        if s_dist and s_dist < shortest:
            shortest = s_dist

    return shortest


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 31
    assert part2(test_1.splitlines()) == 29

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
