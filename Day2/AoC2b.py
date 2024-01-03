import re

total = 0

file_name = "AoC_Day2_Input.txt"

for line in open(file_name):
    matches = re.findall(r'(\d+) (red|blue|green)', line)
    values = {'red': 0, 'blue': 0, 'green': 0}

    for num, color in matches:
        values[color] = max(values[color], int(num))

    total += values['red'] * values['green'] * values['blue']

print("Part 2:", total)
