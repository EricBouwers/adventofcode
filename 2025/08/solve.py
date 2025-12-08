#!/usr/bin/env python
from collections import defaultdict
from functools import reduce
from itertools import combinations
from operator import mul

test_1 = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""
test_2 = """"""


def parse_data(data):
    return [tuple(map(int, j.split(","))) for j in data]


def distance(b1, b2):
    return sum([(q-p)**2 for p, q in zip(b1, b2)])

def get_distances(boxes):
    distances = defaultdict(lambda: [])
    for b1, b2 in combinations(boxes, 2):
        distances[distance(b1, b2)].append((b1, b2))
    return distances


def merge_for_distance(circuit_to_box, box_to_circuit, distances, dist):
    for b1, b2 in distances[dist]:
        to_circuit = box_to_circuit[b1]
        from_circuit = box_to_circuit[b2]

        if to_circuit != from_circuit:
            for move_box in circuit_to_box[from_circuit]:
                circuit_to_box[to_circuit].add(move_box)
                box_to_circuit[move_box] = to_circuit
            del circuit_to_box[from_circuit]


def part1(data, steps=1000):
    boxes = parse_data(data)

    circuit_to_box = {i:{b} for i, b in enumerate(boxes)}
    box_to_circuit = {b:i for i, b in enumerate(boxes)}
    distances = get_distances(boxes)

    for dist in sorted(distances.keys())[0:steps]:
        merge_for_distance(circuit_to_box, box_to_circuit, distances, dist)

    return reduce(mul, sorted(map(len, circuit_to_box.values()), reverse=True)[0:3], 1)



def part2(data):
    boxes = parse_data(data)

    circuit_to_box = {i:{b} for i, b in enumerate(boxes)}
    box_to_circuit = {b:i for i, b in enumerate(boxes)}
    distances = get_distances(boxes)

    for dist in sorted(distances.keys()):
        merge_for_distance(circuit_to_box, box_to_circuit, distances, dist)
        if len(circuit_to_box.keys()) == 1:
            return distances[dist][0][0][0] * distances[dist][0][1][0]



if __name__ == '__main__':

    assert part1(test_1.splitlines(), steps=10) == 40
    assert part2(test_1.splitlines()) == 25272

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

