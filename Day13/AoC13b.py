ll = open('AoC_Day13_Input.txt').read().strip().split('\n\n')

def transpose(x):
    return list(map(list, zip(*x)))

def find_reflection(pattern, non_matches):
    pattern = ["".join(x) for x in pattern]
    for i in range(len(pattern) - 1):
        places_where_doesnt_work = 0
        for j in range(len(pattern)):
            if i + 1 + (i - j) in range(len(pattern)) and pattern[j] != pattern[i + 1 + (i - j)]:
                places_where_doesnt_work += len([k for k in range(len(pattern[j])) if pattern[j][k] != pattern[i + 1 + (i - j)][k]])
        if places_where_doesnt_work == non_matches:
            return i
    return None

def solve(pattern, non_matches):
    pattern = [list(x) for x in pattern.split('\n')]
    row = find_reflection(pattern, non_matches)
    if row is not None:
        return 100 * (row + 1)
    col = find_reflection(transpose(pattern), non_matches)
    if col is not None:
        return col + 1

p2 = 0

for i, l in enumerate(ll):
    p2 += solve(l, 2)

print("Part 2:", p2)
