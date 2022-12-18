#!/usr/bin/env python

test_1 = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""
test_2 = """1,1,1
2,1,1
3,1,1
4,1,1
5,1,1
6,1,1
1,2,1
2,2,1
3,2,1
4,2,1
5,2,1
6,2,1
1,3,1
2,3,1
3,3,1
4,3,1
5,3,1
6,3,1
1,1,2
2,1,2
3,1,2
4,1,2
5,1,2
6,1,2
1,2,2
6,2,2
1,3,2
2,3,2
3,3,2
4,3,2
5,3,2
6,3,2
1,1,3
2,1,3
3,1,3
4,1,3
5,1,3
6,1,3
1,2,3
2,2,3
3,2,3
4,2,3
5,2,3
6,2,3
1,3,3
2,3,3
3,3,3
4,3,3
5,3,3
6,3,3"""


def parse_data(data):
    return set([
        tuple(map(int, d.split(","))) for d in data
    ])


def cube_sides(cube):
    return [
        (cube[0] + 1, cube[1], cube[2]), (cube[0] - 1, cube[1], cube[2]),
        (cube[0], cube[1] + 1, cube[2]), (cube[0], cube[1] - 1, cube[2]),
        (cube[0], cube[1], cube[2] + 1), (cube[0], cube[1], cube[2] - 1),
    ]


def part1(data):
    cubes = parse_data(data)

    uncovered = 0
    for cube in cubes:
        uncovered += sum([side not in cubes for side in cube_sides(cube)])

    return uncovered


def get_sphere_info(cubes):
    sphere_info = {
        'max_x':-100000000, 'max_y':-1000000000, 'max_z': -1000000000,
        'min_x': 100000000, 'min_y':1000000000, 'min_z':1000000000
    }
    for cube in cubes:
        sphere_info['max_x'] = max([sphere_info['max_x'], cube[0]])
        sphere_info['max_y'] = max([sphere_info['max_y'], cube[1]])
        sphere_info['max_z'] = max([sphere_info['max_z'], cube[2]])
        sphere_info['min_x'] = min([sphere_info['min_x'], cube[0]])
        sphere_info['min_y'] = min([sphere_info['min_y'], cube[1]])
        sphere_info['min_z'] = min([sphere_info['min_z'], cube[2]])
    return sphere_info


def side_covered_by_other(cube, cubes, direction, i, max_value, cache):
    travel_cube = (cube[0], cube[1], cube[2])
    hit_cube = False
    while travel_cube[i] != max_value and travel_cube[i] > -5 and not hit_cube:
        travel_cube = (travel_cube[0] + direction[0], travel_cube[1] + direction[1], travel_cube[2] + direction[2])
        hit_cube = travel_cube in cubes

        if (travel_cube, direction) in cache:
            return cache[(travel_cube, direction)]

    cache[(travel_cube, direction)] = hit_cube
    return hit_cube


def get_air_cubes(cubes, sphere_info):
    air_cubes = []
    cache = {}
    for x in range(sphere_info['min_x'], sphere_info['max_x']):
        for y in range(sphere_info['min_y'], sphere_info['max_y']):
            for z in range(sphere_info['min_z'], sphere_info['max_z']):
                if (x, y, z) not in cubes:
                    if sum([
                        side_covered_by_other((x, y, z), cubes, direction, i, max_value, cache) for direction, i, max_value in [
                            ((1, 0, 0), 0, sphere_info['max_x']),
                            ((-1, 0, 0), 0, sphere_info['min_x']),
                            ((0, 1, 0), 1, sphere_info['max_y']),
                            ((0, -1, 0), 1, sphere_info['min_y']),
                            ((0, 0, 1), 2, sphere_info['max_z']),
                            ((0, 0, -1), 2, sphere_info['min_z'])
                        ]
                    ]) == 6:
                        air_cubes.append((x, y, z))
    return air_cubes


def part2(data):
    cubes = parse_data(data)
    sphere_info = get_sphere_info(cubes)

    air_cubes = get_air_cubes(cubes, sphere_info)

    # this needs to be done to weed out the cases in which we have a dent in the droplet :(
    new_air_cubes = [c for c in air_cubes if all([
        n in air_cubes or n in cubes for n in cube_sides(c)
    ])]

    uncovered = 0
    for cube in cubes:
        uncovered += sum([
            side not in cubes and side not in new_air_cubes for side in cube_sides(cube)
        ])

    return uncovered


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 64
    assert part1(test_2.splitlines()) == 108
    assert part2(test_1.splitlines()) == 58
    assert part2(test_2.splitlines()) == 90

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
