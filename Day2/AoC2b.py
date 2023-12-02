import re

total = 0
for line in open("C:\\Users\\g_sie\\OneDrive\\Pulpit\\test.txt"):
    res = re.findall(r'(\d+) (red|blue|green)', line)
    values = {'red': 0, 'blue': 0, 'green': 0}
    for num, color in res:
        values[color] = max(values[color], int(num))
    total += values['red'] * values['green'] * values['blue']
print(total)
