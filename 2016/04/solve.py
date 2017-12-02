#!/usr/bin/python

import sys

rooms = sys.argv[1].split("\n")
total = 0

for room in rooms:
    decrypted = []
    name_parts = room.split("-")
    data = name_parts[-1]
   
    zone_id = int(data.split("[")[0])
    rot = zone_id % 26

    checksum = data.split("[")[1]
    checksum = checksum.replace("]","")

    del name_parts[-1]
    counter = dict()

    for name_part in name_parts:
        for char in name_part:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1

            decrypt = ord(char) + rot
            decrypt = decrypt - 26 if decrypt > ord("z") else decrypt
            decrypted.append(chr(decrypt))
        decrypted.append(" ")    

    sorted_counts = sorted(counter.items(), key=lambda x: (-x[1], x[0]))[0:5]
    checksum_room = map(lambda x: x[0], sorted_counts)

    if checksum == "".join(checksum_room):
        total += zone_id

        print "".join(decrypted), zone_id
        
   
print total
