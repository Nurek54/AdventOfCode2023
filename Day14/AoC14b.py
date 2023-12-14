def tilt(height, width, round, square, dx, dy):
    moved = True
    while moved:
        moved = False
        for rock in round:
            x, y = rock
            x += dx
            y += dy
            if y < 0 or x < 0:
                continue
            if y >= height or x >= width:
                continue
            if (x, y) in square or (x, y) in round:
                continue
            round.remove(rock)
            round.add((x, y))
            moved = True
    return round

def load(round, height):
    return sum([height - y for _, y in round])

def part1(height, width, round, square):
    return load(tilt(height, width, round, square, 0, -1), height)

def part2(height, width, round, square):
    count = 0
    cycle = {}
    while True:
        cycle[frozenset(round)] = count
        count += 1
        round = tilt(height, width, round, square, 0, -1)
        round = tilt(height, width, round, square, -1, 0)
        round = tilt(height, width, round, square, 0, 1)
        round = tilt(height, width, round, square, 1, 0)
        if frozenset(round) in cycle.keys():
            repeat = count - cycle[frozenset(round)]
            if (1000000000 - count) % repeat == 0:
                return load(round, height)

with open("AoC_Day14_Input.txt") as file:
    input_lines = file.readlines()

height = len(input_lines)
width = len(input_lines[0].strip())

square = {(x, y) for y, line in enumerate(input_lines) for x, c in enumerate(line) if c == '#'}
round = {(x, y) for y, line in enumerate(input_lines) for x, c in enumerate(line) if c == 'O'}

print("Part1: ", part1(height, width, round, square))
print("Part2: ", part2(height, width, round, square))
