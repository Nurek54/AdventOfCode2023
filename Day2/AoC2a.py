import re

threshold = {'red': 12, 'blue': 14, 'green': 13}
total = 0

with open("C:\\Users\\g_sie\\OneDrive\\Pulpit\\AoC_Day2_Input.txt") as file:
    for x, line in enumerate(file, start=1):
        res = re.findall(r'(\d+) (red|blue|green)', line)
        if not any(int(match[0]) > threshold[match[1]] for match in res):
            total += x

print(total)
