from math import prod
from collections import defaultdict

with open('AoC_Day3_Input.txt') as f:
    txt = f.read()

lines = txt.split('\n')

d = {}

for x,l in enumerate(lines):
    for y,c in enumerate(l):
        d[x+1j*y] = c

p1 = 0
gears = defaultdict(list)

for x in range(len(lines)):
    num = ''
    valid = False
    gear_pos = None

    for y in range(len(l)):
        c = d[x+1j*y]
        if c.isdigit():
            num += c
            if not valid:
                for x1 in range(-1, 2):
                    for y2 in range(-1, 2):
                        coord = x+x1+1j*(y+y2)
                        c2 = d.get(coord, '.')
                        if not c2.isdigit() and c2 != '.':
                            valid = True
                            if c2 == '*':
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

print(sum(prod(gn) for gn in gears.values() if len(gn) == 2))