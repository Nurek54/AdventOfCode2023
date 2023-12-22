import collections
import inspect
import os

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

with open(os.path.join(cwd, "AoC_Day21_Input.txt"), "r") as f:
    grid = {
        complex(x, y): tile
        for y, row in enumerate(f.read().splitlines())
        for x, tile in enumerate(row.strip())
    }


def get_start(grid=grid):
    return next(pos for pos, tile in grid.items() if tile == "S")


def walk(max_dist, start=get_start(grid), grid=grid):
    queue = collections.deque([(start, 0)])
    tiles = collections.defaultdict(int)
    seen = set()
    size = int(len(list(grid)) ** 0.5)

    while queue:
        pos, dist = queue.popleft()

        if dist == max_dist + 1 or pos in seen:
            continue

        tiles[dist] += 1
        seen.add(pos)

        for neighbor in (1, -1, 1j, -1j):
            n_pos = pos + neighbor

            if grid[complex(n_pos.real % size, n_pos.imag % size)] != "#":
                queue.append((n_pos, dist + 1))

    return tiles


def get_garden_tiles(steps):
    tiles = walk(steps)

    return sum(
        amount for distance, amount in tiles.items() if distance % 2 == steps % 2
    )


print("Part 1:", get_garden_tiles(64))

size = int((len(list(grid.keys()))) ** 0.5)
edge = size // 2

y = [get_garden_tiles(edge + i * size) for i in range(3)]

a = (y[2] - (2 * y[1]) + y[0]) // 2
b = y[1] - y[0] - a
c = y[0]

f = lambda n: a * n**2 + b * n + c

target = (26501365 - edge) // size

print("Part 2:", f(target))
