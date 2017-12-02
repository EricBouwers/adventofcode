#!/usr/bin/python

import hashlib 

roomkey = "reyedfim"
password = ""
better_password = ["_"]*8
found, found_better = 0, 0
index = 0

while found < 8 or found_better < 8:
    h = hashlib.md5(roomkey + str(index)).hexdigest()[0:7]
    if "".join(h[0:5]) == "00000":
        password += h[5] if found < 8 else ""
        found += 1 if found < 8 else 0

        if h[5] in "01234567" and 0 <= int(h[5]) < 8:
            if better_password[int(h[5])] == "_":
                better_password[int(h[5])] = h[6]
                found_better += 1

        print password, "".join(better_password)
    index += 1

print password, "".join(better_password)
