#!/usr/bin/env python
import math

test_1 = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""
test_2 = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""


LOW = 0
HIGH = 1


class BaseModule:
    def __init__(self, name, to):
        self.name = name
        self.to = [t for t in to]
        self.inputs = {}

    def add_input(self, name):
        self.inputs[name] = LOW

    def __call__(self, source, signal):
        return [(self.name, t, signal) for t in self.to]

    def __str__(self):
        return self.__class__.__name__ + ' ' + self.name + ':' + ','.join(self.to)


class FlipFlop(BaseModule):

    def __init__(self, name, to):
        super().__init__(name, to)
        self._on = False

    def __call__(self, source, signal):
        if signal == LOW:
            self._on = not self._on
            return [(self.name, t, HIGH if self._on else LOW) for t in self.to]
        return []


class Conjunction(BaseModule):

    def __call__(self, source, signal):
        self.inputs[source] = signal
        pulse_to_send = LOW if sum(self.inputs.values()) == len(self.inputs.keys()) else HIGH
        return [(self.name, t, pulse_to_send) for t in self.to]


class Output(BaseModule):

    def __call__(self, source, signal):
        return []


def parse_data(data):
    modules = {'output': Output('output', [])}
    for line in data:
        name, outputs = line.split(" -> ")
        outputs = outputs.split(', ')
        if name == 'broadcaster':
            modules['broadcaster'] = BaseModule(name, outputs)
        else:
            type_char = name[0]
            name = name[1:]
            modules[name] = FlipFlop(name, outputs) if type_char == '%' else Conjunction(name, outputs)

    for k, v in modules.items():
        for output in v.to:
            if output in modules.keys():
                modules[output].add_input(k)

    return modules


def part1(data):
    modules = parse_data(data)

    totals = [0, 0]
    for i in range(0, 1000):
        signals = [('button', 'broadcaster', LOW)]
        while signals:
            new_signals = []
            for f, t, pulse in signals:
                totals[pulse] += 1
                new_signals += modules[t](f, pulse) if t in modules.keys() else []
            signals = new_signals

    return totals[0] * totals[1]


def part2(data):
    modules = parse_data(data)

    going_to_rx = [m for m in modules.values() if m.to == ['rx']][0]
    assert going_to_rx.__class__ == Conjunction

    to_figure_out = going_to_rx.inputs
    first_seens = {}
    cycles = {}
    i = 0

    while len(cycles.keys()) != len(to_figure_out):
        signals = [('button', 'broadcaster', LOW)]
        while signals:
            new_signals = []
            for f, t, pulse in signals:
                if f in to_figure_out and pulse == 1:
                    if f not in first_seens:
                        first_seens[f] = i
                    elif f not in cycles:
                        cycles[f] = i - first_seens[f]
                new_signals += modules[t](f, pulse) if t in modules.keys() else []
            signals = new_signals
        i += 1

    return math.lcm(*cycles.values())


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 32000000
    assert part1(test_2.splitlines()) == 11687500

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

