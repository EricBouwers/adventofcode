#!/usr/bin/env python
from functools import reduce
from operator import mul

test_1 = """8A004A801A8002F478"""
test_2 = """620080001611562C8802118E34"""
test_3 = """C0015000016115A2E0802F182340"""
test_4 = """A0016C880162017C3686B18A3D4780"""


def parse_packets(bits, num_packets=None):
    packets = []
    while bits and "1" in bits and (num_packets is None or len(packets) < num_packets):
        bits, packet = parse_packet(bits)
        packets.append(packet)
    return packets, bits


def parse_packet(bits):
    version = int(bits[0:3], 2)
    ptype = int(bits[3:6], 2)
    data = []

    bits = bits[6:]
    if ptype == 4:
        while bits[0] == "1":
            group = bits[1:5]
            data.append(group)
            bits = bits[5:]

        group = bits[1:5]
        data.append(group)
        data = [int("".join(data), 2)]
        bits = bits[5:]

    else:
        if bits[0] == "1":
            num_packets = int(bits[1:12], 2)
            data, bits = parse_packets(bits[12:], num_packets)
        else:
            num_bits = int(bits[1:16], 2)
            data, _ = parse_packets(bits[16:16+num_bits])
            bits = bits[16+num_bits:]

    return bits, (version, ptype, data)


def sum_versions(packets):
    total = 0
    for v, t, d in packets:
        # return v if t == 4 else v + sum_versions(d)
        total += v
        if t != 4:
            total += sum_versions(d)
    return total


ops = {
    0: sum,
    1: lambda x: reduce(mul, x, 1),
    2: min,
    3: max,
    5: lambda x: 1 if x[0] > x[1] else 0,
    6: lambda x: 1 if x[0] < x[1] else 0,
    7: lambda x: 1 if x[0] == x[1] else 0
}


def evaluate_packet(packet):
    _, t, d = packet
    if t == 4:
        return d[0]
    else:
        args = [x for x in map(evaluate_packet, d)]
        return ops[t](args)


def part1(data):
    data = data[0]
    bits = "".join([bin(int(d, 16))[2:].zfill(4) for d in data])

    packets, bits = parse_packets(bits)
    return sum_versions(packets)


def part2(data):
    data = data[0]
    bits = "".join([bin(int(d, 16))[2:].zfill(4) for d in data])

    packets, bits = parse_packets(bits)
    return evaluate_packet(packets[0])


if __name__ == '__main__':

    assert part1("D2FE28".splitlines()) == 6
    assert part1(test_1.splitlines()) == 16
    assert part1(test_2.splitlines()) == 12
    assert part1(test_3.splitlines()) == 23
    assert part1(test_4.splitlines()) == 31

    assert part2("C200B40A82".splitlines()) == 3
    assert part2("04005AC33890".splitlines()) == 54
    assert part2("880086C3E88112".splitlines()) == 7
    assert part2("CE00C43D881120".splitlines()) == 9
    assert part2("D8005AC2A8F0".splitlines()) == 1
    assert part2("F600BC2D8F".splitlines()) == 0
    assert part2("9C005AC2F8F0".splitlines()) == 0
    assert part2("9C0141080250320F1802104A08".splitlines()) == 1

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

