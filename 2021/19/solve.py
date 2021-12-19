#!/usr/bin/env python
import itertools
from collections import defaultdict
from math import sqrt

test_1 = """--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def parse_scanners(data):
    scan_num = 0
    scanners = {}
    scanner = []
    for line in data[1:]:
        if "---" in line:
            scanners[scan_num] = scanner
            scan_num += 1
            scanner = []
        elif line:
            scanner.append(tuple([x for x in map(int, line.split(","))]))
    scanners[scan_num] = scanner
    return scanners

# from https://stackoverflow.com/questions/16452383/how-to-get-all-24-rotations-of-a-3-dimensional-array
def roll(v): return (v[0],v[2],-v[1])
def turn(v): return (-v[1],v[0],v[2])
def sequence (v):
    for cycle in range(2):
        for step in range(3):  # Yield RTTT 3 times
            v = roll(v)
            yield(v)           #    Yield R
            for i in range(3): #    Yield TTT
                v = turn(v)
                yield(v)
        v = roll(turn(roll(v)))  # Do RTR


def rotated_systems(coors):
    new_coors = defaultdict(list)
    for c in coors:
        for i, s in enumerate(sequence(c)):
            new_coors[i].append(s)
    return new_coors


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])


def add_points(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1], p1[2] + p2[2])


def sub_points(p1, p2):
    return (p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2])


def detect_overlap(s1, s2):
    for t, r in rotated_systems(s2).items():
        s2_posses = defaultdict(lambda:[])
        for c1 in s1:
            for c2 in r:
                s2_posses[sub_points(c1, c2)].append((c1, c2))
        if len(s2_posses.keys()) != 625:
            for k in s2_posses.keys():
                if len(s2_posses[k]) >= 12:
                    return k, s2_posses[k], r

    return None, [], []


def part1(data):
    scanner_pos, scanners = detect_scanners(data)

    beacons = set()
    for s, pos in scanner_pos.items():
        for b in scanners[s]:
            beacons.add(add_points(pos, b))

    return len(beacons)


def detect_scanners(data):
    scanners = parse_scanners(data)
    scanner_pos = {0: (0, 0, 0)}
    to_discover = {k for k in scanners.keys() if k not in scanner_pos}
    to_compare = {0}
    while to_discover:
        p1 = to_compare.pop()
        for p2 in to_discover:
            s_pos, matches, r = detect_overlap(scanners[p1], scanners[p2])
            if s_pos:
                scanner_pos[p2] = add_points(scanner_pos[p1], s_pos)
                scanners[p2] = r
                to_compare.add(p2)
        to_discover = {k for k in scanners.keys() if k not in scanner_pos}
    return scanner_pos, scanners


def part2(data):
    scanner_pos, scanners = detect_scanners(data)
    return max([
        distance(scanner_pos[s1], scanner_pos[s2]) for s1, s2 in itertools.combinations(scanner_pos.keys(), 2)
    ])


if __name__ == '__main__':

    rs = rotated_systems([(-1,-1,1),(-2,-2,2),(-3,-3,3),(-2,-3,1),(5,6,-4),(8,0,7)]).values()
    assert([(-1,-1,1),(-2,-2,2),(-3,-3,3),(-2,-3,1),(5,6,-4),(8,0,7)] in rs)
    assert([(1, -1, 1),(2, -2, 2),(3, -3, 3),(2, -1, 3),(-5, 4, -6),(-8, -7, 0)] in rs)
    assert([(-1,-1,-1),(-2,-2,-2),(-3,-3,-3),(-1,-3,-2),(4,6,5),(-7,0,8)] in rs)
    assert([(1,1,-1),(2,2,-2),(3,3,-3),(1,3,-2),(-4,-6,5),(7,0,8)] in rs)
    assert([(1,1,-1),(2,2,-2),(3,3,-3),(1,3,-2),(-4,-6,5),(7,0,8)] in rs)
    assert([(1,1,1),(2,2,2),(3,3,3),(3,1,2),(-6,-4,-5),(0,7,-8)] in rs)

    assert part1(test_1.splitlines()) == 79
    assert part2(test_1.splitlines()) == 3621

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

