import re
import math

def process_rows(values, is_part2=False):
    dirs = values[0]
    node_map = {}

    for row in values[2:]:
        match = re.search(r"([A-Z0-9]+) = \(([A-Z0-9]+), ([A-Z0-9]+)\)", row)
        name, l, r = match.group(1), match.group(2), match.group(3)
        node_map[name] = (l, r)

    positions = ["AAA"] if not is_part2 else [x for x in node_map if x.endswith("A")]
    result = []
    for pos in positions:
        steps = 0
        while True:
            pos = node_map[pos][0 if dirs[steps % len(dirs)] == "L" else 1]

            if (is_part2 and pos.endswith("Z")) or (not is_part2 and pos == "ZZZ"):
                break

            steps += 1
        result.append(steps + 1)

    return result[0] if not is_part2 else math.lcm(*result)

def run(log, file_path, is_part2=False):
    with open(file_path) as f:
        values = [x.strip("\r\n") for x in f.readlines()]

    result = process_rows(values, is_part2)
    log(result)

file_name = "AoC_Day8_Input.txt"

print("Part 1:")
run(print, file_name)

print("Part 2:")
run(print, file_name, is_part2=True)
