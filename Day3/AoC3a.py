from math import prod
from collections import defaultdict

file_name = 'AoC_Day3_Input.txt'

with open(file_name) as file:
    txt = file.read()

lines = txt.split('\n')

d = {}

for x, line in enumerate(lines):
    for y, char in enumerate(line):
        d[x + 1j * y] = char

p1 = 0
gears = defaultdict(list)

for x in range(len(lines)):
    num = ''
    valid = False
    gear_pos = None

    for y in range(len(lines[x])):
        char = d[x + 1j * y]
        if char.isdigit():
            num += char
            if not valid:
                for x1 in range(-1, 2):
                    for y2 in range(-1, 2):
                        coord = x + x1 + 1j * (y + y2)
                        char2 = d.get(coord, '.')
                        if not char2.isdigit() and char2 != '.':
                            valid = True
                            if char2 == '*':
                                gear_pos = coord
        else:
            if valid:
                n = int(num)
                p1 += n
                if gear_pos:
                    gears[gear_pos].append(n)
                valid = False
                gear_pos = None
            num = ''

    if valid:
        n = int(num)
        p1 += n
        if gear_pos:
            gears[gear_pos].append(n)

print("Part 1:", p1)
