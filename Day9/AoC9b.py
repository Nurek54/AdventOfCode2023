def find_next(row):
    return 0 if all(num == 0 for num in row) else row[0] - find_next([b - a for a, b in zip(row, row[1:])])

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [list(map(int, row.split())) for row in file.read().split("\n")]

def calculate_total(rows):
    return sum(find_next(row) for row in rows)

file_name = "AoC_Day9_Input.txt"

rows = read_input(file_name)
result = calculate_total(rows)
print("Part 2:", result)
