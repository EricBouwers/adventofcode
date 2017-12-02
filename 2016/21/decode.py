#!/usr/bin/python

import sys

password = sys.argv[1]
instructions = sys.argv[2].split("\n")

for ins in instructions:
    parts = ins.split()

    if parts[0] == "swap":
        #swap position X with position Y
        #swap letter X with letter Y
        if parts[1] == "position":
            password = list(password)
            old_char = password[int(parts[2])]
            password[int(parts[2])] = password[int(parts[-1])]
            password[int(parts[-1])] = old_char
            password = "".join(password)
        else:
            password = password.replace(parts[2], "_")
            password = password.replace(parts[-1], parts[2])
            password = password.replace("_", parts[-1])
    elif parts[0] == "rotate":
        if parts[1] == "based":
            n = password.index(parts[-1])
            if n >= 4:
                n += 1
            n += 1
            n = -n
        else:
            n = int(parts[-2])
            if parts[1] == "right":
                n = -n
        
        n = n % len(password)
        password = password[n:] + password[:n]
    elif parts[0] == "reverse":
        x = int(parts[2])
        y = int(parts[-1])
        tmp = password[:x]
        tmp += "".join(reversed(password[x:y+1]))
        tmp += password[y+1:]
        password = tmp
    else:
        #move position X to position Y
        y = int(parts[-1])
        x = int(parts[2])
        char = password[x]
        password = password[:x] + password[x+1:]
        password = password[:y] + char + password[y:]

    print password

print password        
