#!/usr/bin/env python

import sys, re

example_input_1_immune = """17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3"""

example_input_1_infection = """801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4"""

class Group(object):

    def __init__(self, name, stats, damage_type, immune, weak):
        self.name = name
        self.units = stats[0]
        self.hit_points = stats[1]
        self.damage = stats[2]
        self.initiative = stats[3]
        self.damage_type = damage_type
        self.immune = immune
        self.weak = weak

    @property
    def power(self):
        return self.units * self.damage

    def __repr__(self):
        return "{}, units: {}, damage: {}, hitpoints: {}".format(self.name, self.units, self.damage, self.hit_points) 
        
    def attack(self, opponent):
        attack_damage = self.would_damage(opponent)
        opponent.receive_damage(attack_damage)

    def would_damage(self, opponent):
        if self.units <= 0 or self.damage_type in opponent.immune:
            attack_damage = 0
        else:
            attack_damage = self.power
            if self.damage_type in opponent.weak:
                attack_damage *= 2
        
        return attack_damage 

    def receive_damage(self, rdamage):
        self.units -= rdamage / self.hit_points

def parse_line(name, line):
    stats = map(int, re.findall("-?\d+", line))
    dt = line.split(" ")[-5]
   
    immune = re.findall(r"immune to ((\w+(, |\)|;))+)", line)
    if immune:
        immune = immune[0][0].replace(";", "").replace(")","").split(", ")

    weak = re.findall(r"weak to ((\w+(, |\)|;))+)", line)
    if weak:
        weak = weak[0][0].replace(";", "").replace(")","").split(", ")

    return Group(name, stats, dt, immune, weak)

def part1(immune, infect, boost=0):

    immune = map(lambda x: parse_line("immune" + str(x[0]), x[1]), enumerate(immune.split("\n")))
    infect = map(lambda x: parse_line("infect" + str(x[0]), x[1]), enumerate(infect.split("\n")))

    for i in immune:
        i.damage += boost

    while len(immune) > 0 and len(infect) > 0:

        total_units = sum([g.units for g in immune + infect])

        pick_immune = [i for i in immune]
        pick_infect = [i for i in infect]
    
        all_groups = [(g, pick_immune) for g in infect] + [(g, pick_infect) for g in immune]
        all_groups.sort(key=lambda t: (-t[0].power, t[0].initiative))
        pairs = []
        
        for group, enemies in all_groups:
            enemies.sort(key=lambda e: (-group.would_damage(e), -e.power, -e.initiative))

            if enemies and group.would_damage(enemies[0]) > 0:
                pairs.append((group, enemies.pop(0)))
    
        pairs.sort(key=lambda x: -x[0].initiative)
        map(lambda x: x[0].attack(x[1]), pairs)

        immune = filter(lambda g: g.units > 0, immune)
        infect = filter(lambda g: g.units > 0, infect)
       
        if total_units <= sum([g.units for g in immune + infect]):
            # no more kills, aborting
            return -1, False
  
    return sum([x.units for x in immune + infect]), len(immune) > 0

def part2(immune, infect):

    immune_won = False
    boost = 0
    result = 0
    while not immune_won:
        result, immune_won = part1(immune, infect, boost=boost)
        boost += 1
    
    return result

if __name__ == '__main__':

    assert part1(example_input_1_immune, example_input_1_infection) == (5216, False)
    assert part1(example_input_1_immune, example_input_1_infection, 1570) == (51, True)
    assert part2(example_input_1_immune, example_input_1_infection) == 51

    immune_data = sys.argv[1]
    infect_data = sys.argv[2]

    print part1(immune_data, infect_data)
    print part2(immune_data, infect_data)

