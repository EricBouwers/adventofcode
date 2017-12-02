#!/usr/bin/env python

import sys

def do_captcha(captcha):
    result = 0

    if captcha[0] == captcha[-1]:
        result += int(captcha[0])

    for i in range(0, len(captcha)-1):
        if captcha[i] == captcha[i+1]:
            result += int(captcha[i])

    return result

def do_second_captcha(captcha):
    result = 0

    captcha_length = len(captcha) 
    steps = captcha_length / 2

    for i in range(0, len(captcha)):
        compare_i = (i + steps) % captcha_length
        if captcha[i] == captcha[compare_i]:
            result += int(captcha[i])

    return result

if __name__ == '__main__':
    
    assert do_captcha("1122") == 3
    assert do_captcha("1111") == 4
    assert do_captcha("1234") == 0
    assert do_captcha("91212129") == 9

    assert do_second_captcha("1212") == 6
    assert do_second_captcha("1221") == 0
    assert do_second_captcha("123425") == 4
    assert do_second_captcha("123123") == 12
    assert do_second_captcha("12131415") == 4

    print do_captcha(sys.argv[1])
    print do_second_captcha(sys.argv[1])

