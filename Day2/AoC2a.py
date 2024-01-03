import re

threshold = {'red': 12, 'blue': 14, 'green': 13}
total = 0

file_name = "AoC_Day2_Input.txt"

with open(file_name) as file:
    for x, line in enumerate(file, start=1):
        matches = re.findall(r'(\d+) (red|blue|green)', line)
        if not any(int(match[0]) > threshold[match[1]] for match in matches):
            total += x

print("Part 1:", total)
