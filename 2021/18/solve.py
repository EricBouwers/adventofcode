#!/usr/bin/env python
import itertools
from functools import reduce

test_1 = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]"""
test_2 = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""
test_3 = """"""
test_4 = """"""


def add_to_leftest(p, to_add):
    if isinstance(p, int):
        return p + to_add, 0
    else:
        p_0, to_add = add_to_leftest(p[0], to_add)
        if p[0] != p_0:
            return [p_0, p[1]], 0
        else:
            p_1, to_add = add_to_leftest(p[1], to_add)
            return [p[0], p_1], to_add


def add_to_rightest(p, to_add):
    if isinstance(p, int):
        return p + to_add, 0
    else:
        p_1, to_add = add_to_rightest(p[1], to_add)
        if p[1] != p_1:
            return [p[0], p_1], 0
        else:
            p_0, to_add = add_to_rightest(p[0], to_add)
            return [p_0, p[1]], to_add


def explode_pair(p, depth):
    if depth == 4 or isinstance(p, int):
        return p, 0, 0

    l, r = p
    if depth == 3:
        if isinstance(l, list):
            r, to_add = add_to_leftest(r, l[1])
            return [0, r], l[0], to_add
        elif isinstance(r, list):
            l, to_add = add_to_leftest(l, r[0])
            return [l, 0], to_add, r[1]
        else:
            return p, 0, 0
    elif isinstance(l, int) and isinstance(r, int):
        return p, 0, 0
    elif isinstance(l, list):
        new_pair, add_left, add_right = explode_pair(l, depth+1)
        if new_pair == l:
            new_pair, add_left, add_right = explode_pair(r, depth+1)
            if add_left:
                l, add_left = add_to_rightest(l, add_left)
            return [l, new_pair], add_left, add_right
        else:
            if add_right:
                r, add_right = add_to_leftest(r, add_right)
            return [new_pair, r], add_left, add_right
    else:
        new_pair, add_left, add_right = explode_pair(r, depth + 1)
        if add_left:
            l = l + add_left
            add_left = 0
        return [l, new_pair], add_left, add_right


def split_pair(p):
    if isinstance(p, int):
        return p if p < 10 else [int(p/2), p-int(p/2)]
    else:
        p_0 = split_pair(p[0])
        if p[0] != p_0:
            return [p_0, p[1]]
        else:
            p_1 = split_pair(p[1])
            return [p[0], p_1]


def reduce_snail(pair):
    new_pair, add_left, add_right = explode_pair(pair, 0)
    if new_pair != pair:
        return new_pair
    else:
        return split_pair(pair)


def add_pair(left, right):
    new_pair = [left, right]
    reduced_pair = reduce_snail(new_pair)
    while reduced_pair != new_pair:
        new_pair = reduced_pair
        reduced_pair = reduce_snail(new_pair)

    return new_pair


def magnitude(p):
    if isinstance(p, int):
        return p
    else:
        m_l = magnitude(p[0])
        m_r = magnitude(p[1])
        return 3*m_l + 2*m_r


def part1(data):
    result_pair = reduce(add_pair, map(eval, data))
    return magnitude(result_pair)


def part2(data):
    pairs = map(eval, data)
    return max([max(magnitude(add_pair(x, y)), magnitude(add_pair(y, x))) for x,y in itertools.combinations(pairs, 2)])


if __name__ == '__main__':

    assert(reduce_snail([[[[[9,8],1],2],3],4])) == [[[[0,9],2],3],4]
    assert (reduce_snail([7,[6,[5,[4,[3,2]]]]])) == [7,[6,[5,[7,0]]]]
    assert (reduce_snail([[6,[5,[4,[3,2]]]],1])) == [[6,[5,[7,0]]],3]
    assert (reduce_snail([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]) == [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])

    assert add_pair([[[[4,3],4],4],[7,[[8,4],9]]], [1,1]) == [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
    assert add_pair([[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]], [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]) == [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]

    assert magnitude([[1,2],[[3,4],5]]) == 143
    assert magnitude([[[[5,0],[7,4]],[5,5]],[6,6]]) == 1137

    assert part1(test_1.splitlines()) == 3488
    assert part2(test_2.splitlines()) == 3993

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

