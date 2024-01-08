input_file = r"AoC_Day12_Input.txt"
ll = [x.strip() for x in open(input_file).readlines()]
import functools
@functools.lru_cache(maxsize=None)
def solve(s, withinRun, remain):
    if not s:
        if withinRun is None and len(remain) == 0:
            return 1
        if len(remain) == 1 and withinRun is not None and withinRun == remain[0]:
            return 1
        return 0
    possibleMore = 0
    for ch in s:
        if ch == '#' or ch == '?':
            possibleMore += 1
    if withinRun is not None and possibleMore + withinRun < sum(remain):
        return 0
    if withinRun is None and possibleMore < sum(remain):
        return 0
    if withinRun is not None and len(remain) == 0:
        return 0
    poss = 0
    if s[0] == '.' and withinRun is not None and withinRun != remain[0]:
        return 0
    if s[0] == '.' and withinRun is not None:
        poss += solve(s[1:], None, remain[1:])
    if s[0] == '?' and withinRun is not None and withinRun == remain[0]:
        poss += solve(s[1:], None, remain[1:])
    if (s[0] == '#' or s[0] == '?') and withinRun is not None:
        poss += solve(s[1:], withinRun+1, remain)
    if (s[0] == '?' or s[0] == '#') and withinRun is None:
        poss += solve(s[1:], 1, remain)
    if (s[0] == '?' or s[0] == '.') and withinRun is None:
        poss += solve(s[1:], None, remain)
    return poss

p1 = 0
p2 = 0
for l in ll:
    s = l.split(" ")[0]
    v = tuple([int(x) for x in l.split(" ")[1].split(",")])
    p1 += solve(s, None, v)
    news = ""
    for j in range(5):
        news += "?"
        news += s
    p2 += solve(news[1:], None, v*5)
print("Part 1: ", p1)
print("Part 2: ", p2)