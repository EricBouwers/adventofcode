#!/usr/bin/env python

test_1 = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
test_2 = """"""


class Node:

    def __init__(self, parent=None, name='/', is_dir=True, size=0):
        self.parent = parent
        self.meta = {'name': name, 'size': size, 'dir': is_dir}
        self.children = {}

    def __str__(self):
        return self.meta['name'] + "(" + str(self.meta['size']) + ")"

    def is_dir(self):
        return self.meta['dir']

    def meta_sum(self):
        return self.meta['size'] + sum([c.meta_sum() for c in self.children.values()])

    def add_child(self, name, size, is_dir):
        self.children[name] = Node(self, name, is_dir, size)

    def get_child(self, name):
        return self.children[name]

    def get_parent(self):
        return self.parent


def parse_tree(data, root_node):
    cur_node = root_node
    dirs = []

    for d in data:
        if d == '$ ls':
            continue
        elif d == '$ cd ..':
            cur_node = cur_node.get_parent()
        elif d.startswith('$ cd '):
            cur_node = cur_node.get_child(d.split(" ")[2])
        elif d.startswith('dir '):
            cur_node.add_child(d.split(" ")[1], 0, True)
            dirs.append(cur_node.get_child(d.split(" ")[1]))
        else:
            cur_node.add_child(d.split(" ")[1], int(d.split(" ")[0]), False)

    return dirs


def print_tree(node, indent=""):
    print(indent + str(node))
    list(map(lambda n: print_tree(n, " " + indent), node.children.values()))


def part1(data):
    root_node = Node(None, '/', True, 0)
    dirs = parse_tree(data[1:], root_node)

    return sum(x.meta_sum() for x in dirs if (x.is_dir() and x.meta_sum() < 100000))


def part2(data):
    root_node = Node(None, '/', True, 0)
    dirs = parse_tree(data[1:], root_node)

    needed_space = 30000000 - (70000000 - root_node.meta_sum())
    viable_dirs = [x for x in dirs if x.meta_sum() > needed_space]

    return sorted(viable_dirs, key=lambda x: x.meta_sum())[0].meta_sum()


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 95437
    assert part2(test_1.splitlines()) == 24933642

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

