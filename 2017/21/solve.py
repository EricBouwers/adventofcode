#!/usr/bin/env python
from collections import defaultdict

import math

start_image = ".#./..#/###"

example_rules = "../.# => ##./#../...\n.#./..#/### => #..#/..../..../#..#"


def parse_img(img):
    return map(lambda x: map(lambda y: 0 if y == "." else 1, list(x)), img.split("/"))


def print_img(img):
    print format_img(img)


def format_img(img):
    return "/".join(map(lambda x: "".join(map(lambda y: "#" if y else ".", x)), img))


def parse_rules(raw_rules):
    rules = defaultdict(lambda: [])

    for line in raw_rules.split("\n"):
        from_to = line.split(" => ")
        rules[len(from_to[0])].append(from_to)

    return rules


def split_img(img, size):
    result = []
    parsed = parse_img(img)

    step = 2 + (size % 2)

    for r in range(0, size, step):
        for c in range(0, size, step):
            part = []
            for rc in range(0, step):
                part.append(parsed[r+rc][c:c+step])

            result.append(format_img(part))

    return result

offsets = {
    4: {
        2: {0: (0, 0), 1: (2, 0), 2: (0, 2), 3: (2, 2)},
        3: {0: (0, 0), 1: (0, 3), 2: (3, 0), 3: (3, 3)},
    },
    9: {
        3: {0: (0, 0), 1: (0, 3), 2: (0, 6), 3: (3, 0), 4: (3, 3), 5: (3, 6), 6: (6, 0), 7: (6, 3), 8: (6, 6)},
    }
}


def merge_img(parts, size):
    if len(parts) == 1:
        return parts[0]

    start_count = sum(map(count_img, parts))

    parts = map(parse_img, parts)

    img = [[""]*size]*size
    img = map(list, img)

    for ip, p in enumerate(parts):
        len(parts)
        offset = offsets[len(parts)][len(p)][ip]
        for ir, r in enumerate(p):
            for ic, c in enumerate(r):
                img[offset[0] + ir][offset[1] + ic] = c

    result = format_img(img)

    assert start_count == count_img(result)
    return result


def apply_rules(allrules, img):
    size = len(img.split("/")[0])
    parts = split_img(img, size)
    rules = allrules[5 if size % 2 == 0 else 11]
    parts = map(lambda x: apply_rule_to_part(rules, x), parts)
    return merge_img(parts, int(len(parts[0].split("/")) * math.sqrt(len(parts))))


def apply_rule_to_part(allrules, p):
    perms = all_perms(p)
    result1, result2 = None, None
    for i, rule in enumerate(allrules):
        for perm in perms:
            if rule[0] == perm:
                if not result1 and not result2:
                    result1 = rule[1]
                    result2 = rule
                else:
                    print p, perms, rule, result2

    return result1


def all_perms(p):
    results = set()
    parsed = parse_img(p)

    for i in range(0, 9):
        parsed = rotate(parsed)
        results.add(format_img(parsed))
        parsed[0], parsed[-1] = parsed[-1], parsed[0]
        results.add(format_img(parsed))
        parsed[0], parsed[-1] = parsed[-1], parsed[0]

    return results


def rotate(img):
    if len(img) == 2:
        img[0][0], img[0][1], img[1][1], img[1][0] = img[0][1], img[1][1], img[1][0], img[0][0]
    else:
        img[0][0], img[0][1], img[0][2], img[1][2], img[2][2], img[2][1], img[2][0], img[1][0] = \
            img[0][2], img[1][2], img[2][2], img[2][1], img[2][0], img[1][0], img[0][0], img[0][1]

    return img


def count_img(img):
    return sum(map(sum, parse_img(img)))


def process(img, raw_rules, iterations):

    rules = parse_rules(raw_rules)
    images = [img]

    for iter in range(0, iterations):
        images = map(lambda cur_img: apply_rules(rules, cur_img), images)
        size = len(images[0].split("/")[0])
        if size == 9:
            new_images = []
            for i in images:
                new_images += split_img(i, size)
            images = new_images
        print iter

    return sum(map(count_img, images))


if __name__ == "__main__":
    assert process(start_image, example_rules, 2) == 12

    with open("input.txt", "r") as input_file:
        print process(start_image, input_file.read(), 5)

    with open("input.txt", "r") as input_file:
        print process(start_image, input_file.read(), 18)
