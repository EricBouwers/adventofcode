#!/usr/bin/python

import sys, re
import md5

salt = sys.argv[1]
index = 0

seen_hashes = dict()

keys = set()

def get_hash(c):
    current_hash = seen_hashes.get(c)

    if current_hash is None:
        current_hash = md5.new(salt + str(c)).hexdigest()

        for i in range(0, 2016):
            current_hash = md5.new(current_hash).hexdigest()

        seen_hashes[c] = current_hash

    return current_hash


while len(keys) < 64:
    current_hash = get_hash(index)

    matches = re.findall(r"(.)\1\1", current_hash)
    if matches:
        for i in range(index+1, index + 999):
            new_hash = get_hash(i)
            if matches[0][0]*5 in new_hash:
                keys.add(index)

    index += 1
    print index, len(keys)

print sorted(list(keys))
print index
