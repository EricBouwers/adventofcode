#!/usr/bin/env python

test_1 = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""
test_2 = """"""


DIRECTIONS = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}


def parse_data(data):
    start = (data[0].index(".") - 1, -1)
    end = (data[-1].index(".") - 1, len(data) - 2)

    blizzards = []
    for y, d in enumerate(data[1:len(data)-1]):
        for x, c in enumerate(d, start=-1):
            if c in ["<", ">", "^", "v"]:
                blizzards.append(((x, y), DIRECTIONS[c]))

    return start, end, blizzards


def move_blizzard(blizzard, max_x, max_y):
    return (blizzard[0][0] + blizzard[1][0]) % max_x, (blizzard[0][1] + blizzard[1][1]) % max_y


def possible_steps(mins, cur_pos, my_blizzards_pos, max_x, max_y, end):
    mins += 1

    new_states = [(mins, cur_pos)] if cur_pos not in my_blizzards_pos else []
    for pos in DIRECTIONS.values():
        new_pos = (cur_pos[0] + pos[0], cur_pos[1] + pos[1])
        if new_pos == end:
            return [(mins, end)]
        elif 0 <= new_pos[0] <= max_x and 0 <= new_pos[1] < max_y and new_pos not in my_blizzards_pos:
            new_states.append((mins, new_pos))
    return new_states


def comp_blizzard_states(blizzards, max_x, max_y):
    blizzard_states = []

    blizzards_pos = [b[0] for b in blizzards]
    while blizzards_pos not in blizzard_states:
        blizzard_states.append(blizzards_pos)
        blizzards = [(move_blizzard(b, max_x, max_y), b[1]) for b in blizzards]
        blizzards_pos = [b[0] for b in blizzards]

    return blizzard_states


def part1(data):
    start, end, blizzards = parse_data(data)

    max_x, max_y = end[0] + 1, end[1]

    states = [(0, start)]
    seen_states = set()

    blizzard_states = comp_blizzard_states(blizzards, max_x, max_y)
    nr_of_states = len(blizzard_states)
    print(nr_of_states)

    while len(states) > 0:
        mins, cur_pos = states.pop(0)

        while (mins, cur_pos) in seen_states and states:
            mins, cur_pos = states.pop(0)
        seen_states.add((mins, cur_pos))

        print(mins, cur_pos)
        if cur_pos == end:
            return mins
        else:
            states = states + possible_steps(mins, cur_pos, blizzard_states[(mins+1) % nr_of_states], max_x, max_y, end)

    return None


def part2(data):
    start, end, blizzards = parse_data(data)

    max_x, max_y = end[0] + 1, end[1]

    states = [(0, start)]
    seen_states = set()

    blizzard_states = comp_blizzard_states(blizzards, max_x, max_y)
    nr_of_states = len(blizzard_states)

    my_end = end
    end_count = 0
    while len(states) > 0:
        mins, cur_pos = states.pop(0)

        while (mins, cur_pos) in seen_states and states:
            mins, cur_pos = states.pop(0)
        seen_states.add((mins, cur_pos))

        print(mins, cur_pos)
        if cur_pos == my_end:
            if end_count == 2:
                return mins
            else:
                end_count += 1
                my_end = start if my_end == end else end
                states = [(mins, cur_pos)]
                seen_states = set()
        else:
            states = states + possible_steps(mins, cur_pos, blizzard_states[(mins+1) % nr_of_states], max_x, max_y, my_end)

    return None


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 18
    assert part2(test_1.splitlines()) == 54

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))  # not correct, it is 1 plus?
    print(part2(data.splitlines()))  # but this is correct! so maybe a bug which solves itself :)

