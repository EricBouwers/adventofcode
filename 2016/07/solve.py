#!/usr/bin/python

import sys, re

ips= sys.argv[1].split("\n")
correct = 0
supports_ssl = 0

for ip in ips:
    has_match = False
    has_match_in_brackets = False
    idx = 0
    parts = re.split(r'\[|\]', ip)
    for part in parts:
        for e in xrange(4, len(part)+1):
            word = part[e-4:e]
            if word == word[::-1] and word[0] != word[1]:
                if idx % 2:
                    has_match_in_brackets = True
                else:
                    has_match = True
        idx += 1

    correct += 1 if has_match and not has_match_in_brackets else 0
    
    abas = []
    for i in xrange(0, len(parts), 2):
        for e in xrange(3, len(parts[i])+1):
            word = parts[i][e-3:e]
            if word == word[::-1] and word[0] != word[1]:
                abas.append(word)

    found_ssl_support = False
    for aba in abas:
        for i in xrange(1, len(parts), 2):
            found_ssl_support = found_ssl_support or (aba[1] + aba[0] + aba[1]) in parts[i]            

    supports_ssl += 1 if found_ssl_support else 0

print correct, supports_ssl
