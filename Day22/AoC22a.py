input_filename = "AoC_Day22_Input.txt"

with open(input_filename, 'r') as file:
    lines = file.readlines()

bricks = []

for line in lines:
    start, end = line.split("~")
    start = tuple(int(n) for n in start.split(","))
    end = tuple(int(n) for n in end.split(","))

    cubes = [start, end]
    for i in range(2):
        if start[i] != end[i]:
            for j in range(min(start[i], end[i]) + 1, max(start[i], end[i])):
                to_add = list(start)
                to_add[i] = j
                cubes.append(tuple(to_add))
            break

    bricks.append(cubes)

bricks = sorted(bricks, key=lambda bs: min(b[2] for b in bs))


def drop_bricks(bricks):
    settled = set()
    final_bricks = []
    num_fell = 0
    for brick in bricks:
        did_move = False
        while True:
            nxt = []
            for cx, cy, cz in brick:
                nxt.append((cx, cy, cz - 1))

            if any((c[2] == 0 or (c in settled)) for c in nxt):
                break
            else:
                brick = nxt
                did_move = True

        for cube in brick:
            settled.add(cube)
        final_bricks.append(brick)
        if did_move:
            num_fell += 1

    return final_bricks, num_fell

dropped, _ = drop_bricks(bricks)

p1_total = 0
for i in range(len(dropped)):
    without = dropped.copy()
    without.pop(i)
    _, num_fell = drop_bricks(without)
    if num_fell == 0:
        p1_total += 1

print("Part 1:", p1_total)
