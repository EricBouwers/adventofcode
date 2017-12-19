#!/usr/bin/env python


example = "    |          \n    |  +--+    \n    A  |  C    \nF---|----E|--+ \n    |  |  |  D \n    +B-+  +--+ "


def process(x):
    grid = []

    for l in x.split("\n"):
        grid.append(list(l.replace(".", " ")))

    pos = [grid[0].index("|"), 0]

    width = len(grid[0])
    height = len(grid)
    direction = (0, 1)
    result = ""
    steps = 1

    while 0 <= pos[0] < width and 0 <= pos[1] < height and grid[pos[1]][pos[0]] != "F":
        steps += 1
        if grid[pos[1]][pos[0]] != "+":
            pos[0] += direction[0]
            pos[1] += direction[1]
        else:
            if direction[0] == 0:
                possibilities = [(1, 0), (-1, 0)]
            else:
                possibilities = [(0, 1), (0, -1)]

            direction = None
            for p in possibilities:
                new_x = pos[0] + p[0]
                new_y = pos[1] + p[1]
                if not direction and 0 <= new_x < width and 0 <= new_y < height and grid[new_y][new_x] != " ":
                    direction = p
                    pos[0] = new_x
                    pos[1] = new_y

        if grid[pos[1]][pos[0]] not in ["-", "|", "+", " "]:
            result += grid[pos[1]][pos[0]]

    return result, steps


if __name__ == "__main__":
    assert process(example) == ("ABCDEF", 38)

    with open("input.txt", "r") as input_file:
        print process(input_file.read())
