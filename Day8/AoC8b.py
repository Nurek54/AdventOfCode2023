import sys
import os
import math
import re


def part2(values):
    dirs = values[0]
    node_map = {}

    for row in values[2:]:
        match = re.search(r"([A-Z0-9]+) = \(([A-Z0-9]+), ([A-Z0-9]+)\)", row)
        name, l, r = match.group(1), match.group(2), match.group(3)
        node_map[name] = (l, r)

    positions = [x for x in node_map if x.endswith("A")]
    result = []
    for pos in positions:
        steps = 0
        while True:
            pos = node_map[pos][0 if dirs[steps % len(dirs)] == "L" else 1]

            if pos.endswith("Z"):
                break

            steps += 1
        result.append(steps + 1)

    return math.lcm(*result)


def test(log):
    values = log.decode_values("""
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
    """)

    log.test(part2(values), '6')


def run(log, file_path):
    with open(file_path) as f:
        values = [x.strip("\r\n") for x in f.readlines()]

    result = part2(values)
    log(result)

# Specify the file name
file_name = "AoC_Day8_Input.txt"

print("Part 2:")
run(print, file_name)
