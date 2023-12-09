def find_next(row):
    return 0 if all(num == 0 for num in row) else row[-1] + find_next([b - a for a, b in zip(row, row[1:])])

with open("AoC_Day9_Input.txt") as file:
    rows = [list(map(int, row.split())) for row in file.read().split("\n")]

total = 0
for row in rows:
    total += find_next(row)

print(total)
