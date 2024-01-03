def find_next(row):
    return 0 if all(num == 0 for num in row) else row[0] - find_next([b - a for a, b in zip(row, row[1:])])

def read_input(file_path):
    with open(file_path, 'r') as file:
        rows = [list(map(int, row.split())) for row in file.read().split("\n")]
    return rows

def calculate_total(rows):
    total = 0
    for row in rows:
        total += find_next(row)
    return total

def test(log):
    values = log.decode_values("""
5 2 9 4
3 5 8 9
1 2 6 8
    """)
    log.test(calculate_total(values), '16')

file_name = "AoC_Day9_Input.txt"

rows = read_input(file_name)
result = calculate_total(rows)
print("Part 2:", result)
