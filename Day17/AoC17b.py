from heapq import heappop, heappush

def read_input(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()

def gen_neighbors(node, data, ext_cond):
    x, y, v, dir = node
    dx, dy = dir
    l, r = (-dy, dx), (dy, -dx)
    th = 10 if ext_cond else 3

    if v < th and 0 <= x + dx < len(data) and 0 <= y + dy < len(data[0]):
        yield (x + dx, y + dy, v + 1, dir), int(data[x + dx][y + dy])

    for dx, dy in l, r:
        if 0 <= x + dx < len(data) and 0 <= y + dy < len(data[0]) and (not ext_cond or v > 3):
            yield (x + dx, y + dy, 1, (dx, dy)), int(data[x + dx][y + dy])

def pathfind(data, ext_cond):
    Q_v = set()
    s1, s2 = (0, 0, 0, (1, 0)), (0, 0, 0, (0, 1))
    dist = {s1: 0, s2: 0}
    Q = [(0, s1), (0, s2)]
    tgt = (len(data) - 1, len(data[0]) - 1)

    while len(Q):
        _, u = heappop(Q)

        if u in Q_v:
            continue

        Q_v.add(u)

        if u[:2] == tgt and (not ext_cond or u[2] > 3):
            tgt = u
            break

        for v, cost in gen_neighbors(u, data, ext_cond):
            if v in Q_v:
                continue

            alt = dist[u] + cost

            if v not in dist or alt < dist[v]:
                dist[v] = alt
                heappush(Q, (alt, v))

    print(dist[tgt])

data = read_input("AoC_Day17_Input.txt")

print("Part 1: ")
pathfind(data, False)
print("Part 2: ")
pathfind(data, True)
