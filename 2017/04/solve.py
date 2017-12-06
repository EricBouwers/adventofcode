#!/usr/bin/env python

import sys
import itertools as it

def is_unique(phrase):
    words = phrase.split()
    return len(words) == len(set(words))

def uniques(pwd_list):
    result = 0
    
    for phrase in pwd_list.split("\n"):
        if is_unique(phrase):
            result = result + 1

    return result

def is_unique_anagram(phrase):
    words = map(lambda x: "".join(sorted(x)), phrase.split())
    return len(words) == len(set(words))

def unique_anagrams(pwd_list):
    result = 0
    
    for phrase in pwd_list.split("\n"):
        if is_unique_anagram(phrase):
            result = result + 1

    return result


if __name__ == '__main__':
    assert is_unique("aa bb cc dd ee") == True
    assert is_unique("aa bb cc dd aa") == False
    assert is_unique("aa bb cc dd aaa") == True

    assert is_unique_anagram("abcde fghij") == True
    assert is_unique_anagram("abcde xyz ecdab") == False
    assert is_unique_anagram("a ab abc abd abf abj") == True
    assert is_unique_anagram("iiii oiii ooii oooi oooo") == True
    assert is_unique_anagram("oiii ioii iioi iiio") == False

    print uniques(sys.argv[1])
    print unique_anagrams(sys.argv[1])

