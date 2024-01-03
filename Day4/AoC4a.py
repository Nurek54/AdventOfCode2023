def read_input(file_name):
    with open(file_name) as file:
        return file.read().strip().split('\n')

def calculate_part1(lines):
    part1_result = 0
    for line in lines:
        winning_set = set([int(x) for x in line.split(":")[1].split("|")[0].strip().split()])
        have_list = [int(x) for x in line.split("|")[1].strip().split()]
        have_list = [x for x in have_list if x in winning_set]

        if len(have_list):
            part1_result += 2**(len(have_list) - 1)

    return part1_result

file_name = "AoC_Day4_Input.txt"
lines = read_input(file_name)
result_part1 = calculate_part1(lines)

print("Part 1:", result_part1)
