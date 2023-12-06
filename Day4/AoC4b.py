lines = open("AoC_Day4_Input.txt").read().strip().split('\n')

part1_result = 0
multiplier = [1 for _ in lines]
part2_result = 0

for i, line in enumerate(lines):
    winning_set = set([int(x) for x in line.split(":")[1].split("|")[0].strip().split()])
    have_list = [int(x) for x in line.split("|")[1].strip().split()]
    have_list = [x for x in have_list if x in winning_set]

    if len(have_list):
        part1_result += 2**(len(have_list) - 1)

    my_mult = multiplier[i]
    for j in range(i + 1, min(i + len(have_list) + 1, len(lines))):
        multiplier[j] += my_mult
    part2_result += my_mult

print(part2_result)
