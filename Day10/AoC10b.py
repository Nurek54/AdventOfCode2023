import os

def read_input(file_path):
    with open(file_path, "r") as file:
        raw_data = file.read()
    return raw_data

def process_input(raw_data):
    grid_lines = raw_data.split("\n")
    num_rows = len(grid_lines)
    num_cols = len(grid_lines[0])

    obstacle_grid = [[0] * num_cols for _ in range(num_rows)]

    start_x = -1
    start_y = -1
    for i in range(num_rows):
        for j in range(num_cols):
            if "S" in grid_lines[i]:
                start_x = i
                start_y = grid_lines[i].find("S")
    # print(start_x, start_y)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    happiness_patterns = ["-7J", "|LJ", "-FL", "|F7"]
    valid_directions = []
    for i in range(4):
        pos = directions[i]
        new_x = start_x + pos[0]
        new_y = start_y + pos[1]
        if 0 <= new_x < num_rows and 0 <= new_y < num_cols and grid_lines[new_x][new_y] in happiness_patterns[i]:
            valid_directions.append(i)

    # print(valid_directions)
    valid_start = 3 in valid_directions  # Part 2

    transformations = {
        (0, "-"): 0,
        (0, "7"): 1,
        (0, "J"): 3,
        (2, "-"): 2,
        (2, "F"): 1,
        (2, "L"): 3,
        (1, "|"): 1,
        (1, "L"): 0,
        (1, "J"): 2,
        (3, "|"): 3,
        (3, "F"): 0,
        (3, "7"): 2,
    }

    current_direction = valid_directions[0]
    current_x = start_x + directions[current_direction][0]
    current_y = start_y + directions[current_direction][1]
    path_length = 1
    obstacle_grid[start_x][start_y] = 1  # Part 2
    while (current_x, current_y) != (start_x, start_y):
        obstacle_grid[current_x][current_y] = 1  # Part 2
        path_length += 1
        current_direction = transformations[(current_direction, grid_lines[current_x][current_y])]
        current_x += directions[current_direction][0]
        current_y += directions[current_direction][1]

    # print(path_length)
    part1_result = path_length // 2

    enclosed_regions = 0
    for i in range(num_rows):
        inside_region = False
        for j in range(num_cols):
            if obstacle_grid[i][j]:
                if grid_lines[i][j] in "|JL" or (grid_lines[i][j] == "S" and valid_start):
                    inside_region = not inside_region
            else:
                enclosed_regions += inside_region

    return part1_result, enclosed_regions

def test(log):
    values = log.decode_values("""
S---
|L--
-FL-
|J--
    """)
    log.test(process_input(values), ('4', 2))

# Specify the file name
file_name = "AoC_Day10_Input.txt"
file_path = os.path.join(file_name)

raw_data = read_input(file_path)
result = process_input(raw_data)
print("Part 1:", result[0])
print("Part 2:", result[1])
