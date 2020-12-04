#!/usr/bin/env python
import string

test_1 = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""
test_2 = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""
test_3 = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""


def parse_passwords(data):
    passports = []
    passport = {}
    for line in data:
        if line == '':
            passports.append(passport)
            passport = {}
        else:
            parts = line.split()
            passport.update({f[0]: f[1] for f in [p.split(":") for p in parts]})
    passports.append(passport)
    return passports


def count_valids(data, f):
    passports = parse_passwords(data)
    return sum([f(p) for p in passports])


def has_required_fields(p):
    return len({'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} - p.keys()) == 0


def fields_are_valid(p):
    res = (1920 <= int(p['byr']) <= 2002) and \
          (2010 <= int(p['iyr']) <= 2020) and \
          (2020 <= int(p['eyr']) <= 2030) and \
          (len(p['pid']) == 9 and p['pid'].isdigit()) and \
          (p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) and \
          (len(p['hcl']) == 7 and p['hcl'][0] == '#' and all(c in '0123456789abcdef' for c in p['hcl'][1:])) and \
          (150 <= int(p['hgt'][0:-2]) <= 193 if p['hgt'][-2:] == 'cm' else 59 <= int(p['hgt'][0:-2]) <= 76)
    return res


def part1(data):
    return count_valids(data, has_required_fields)


def part2(data):
    return count_valids(data, lambda x: has_required_fields(x) and fields_are_valid(x))


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 2
    assert part2(test_2.splitlines()) == 0
    assert part2(test_3.splitlines()) == 4

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

