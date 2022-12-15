#!/usr/bin/env python

test_1 = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""
test_2 = """"""


def parse_data(data):
    sensors = {}
    for d in data:
        parts = d.replace(",", "").replace(":", "").split(" ")
        sensors[(int(parts[2].split('=')[1]), int(parts[3].split('=')[1]))] = (int(parts[-2].split('=')[1]), (int(parts[-1].split('=')[1])))

    return sensors


def man_dist(x, y):
    return sum([abs(xc - y[i]) for i, xc in enumerate(x)])


def part1(data, y=2000000):
    sensors = parse_data(data)

    covers_y = []
    for sensor, beacon in sensors.items():
        if man_dist(sensor, (sensor[0], y)) <= man_dist(sensor, beacon):
            covers_y.append(sensor)

    covered_coors = set()
    for sensor in covers_y:
        beacon_dist = man_dist(sensor, sensors[sensor])
        y_dist = man_dist(sensor, (sensor[0], y))

        for x in range(0, beacon_dist - y_dist + 1):
            covered_coors.add((sensor[0] + x, y))
            covered_coors.add((sensor[0] - x, y))

    return len(covered_coors - set(sensors.values()))


def part2(data, max_c=4000000):
    sensors = parse_data(data)
    sensor_dists = {sensor: man_dist(sensor, beacon) for sensor, beacon in sensors.items()}

    x, y = 0, 0
    while y < max_c:
        covers_sensors = [s for s,d in sensor_dists.items() if man_dist(s,(x,y)) <= d]
        if len(covers_sensors) == 0:
            return x * 4000000 + y
        else:
            x_jump = max([sensor_dists[s] - man_dist(s, (x, y)) for s in covers_sensors])
            x += x_jump + 1
            if x > max_c:
                x, y = 0, y+1

    return None


if __name__ == '__main__':

    assert part1(test_1.splitlines(), 10) == 26
    assert part2(test_1.splitlines(), 20) == 56000011

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

