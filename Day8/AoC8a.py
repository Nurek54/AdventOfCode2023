import sys
import os
import math
import re

def part1(values):
    dirs = values[0]
    node_map = {}

    for row in values[2:]:
        match = re.search(r"([A-Z0-9]+) = \(([A-Z0-9]+), ([A-Z0-9]+)\)", row)
        name, l, r = match.group(1), match.group(2), match.group(3)
        node_map[name] = (l, r)

    positions = ["AAA"]
    result = []
    for pos in positions:
        steps = 0
        while True:
            pos = node_map[pos][0 if dirs[steps % len(dirs)] == "L" else 1]

            if pos == "ZZZ":
                break

            steps += 1
        result.append(steps + 1)

    return result[0]


def test(log):
    values = log.decode_values("""
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
    """)

    log.test(part1(values), '6')


def run(log, file_path):
    with open(file_path) as f:
        values = [x.strip("\r\n") for x in f.readlines()]

    result = part1(values)
    log(result)

# Specify the file name
file_name = "AoC_Day8_Input.txt"

print("Part 1:")
run(print, file_name)
