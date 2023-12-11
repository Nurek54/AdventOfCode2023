def read_data(file_path):
    with open(file_path) as file:
        return [list(line) for line in file.read().split("\n")]

def calculate_distance(stars, expand, expand_col, part):
    distance = 0
    distance2 = 0

    for i in range(len(stars) - 1):
        for j in range(i + 1, len(stars)):
            (x1, y1), (x2, y2) = stars[i], stars[j]

            for num in expand:
                if x1 < num < x2 or x2 < num < x1:
                    distance += 1
                    distance2 += 999999

            for num in expand_col:
                if y1 < num < y2 or y2 < num < y1:
                    distance += 1
                    distance2 += 999999

            distance += abs(x1 - x2) + abs(y2 - y1)

    if part == 1:
        return distance
    elif part == 2:
        return distance2
    else:
        return None

def main():
    file_path = "AoC_Day11_Input.txt"
    data = read_data(file_path)

    expand_rows = [x for x, line in enumerate(data) if all(char == "." for char in line)]
    expand_cols = [col for col in range(len(data[0])) if all(data[row][col] == "." for row in range(len(data)))]
    stars = [(x, y) for x, line in enumerate(data) for y, col in enumerate(line) if col == "#"]

    distance = calculate_distance(stars, expand_rows, expand_cols, part=1)

    print("Part 1:", distance)

if __name__ == "__main__":
    main()
