import os

file_name = "AoC_Day1_Input.txt"

with open(file_name, 'r') as file:
    input_str = file.read()

lines = [line.strip() for line in input_str.split('\n')]

total_sum = 0

for line in lines:
    digits = [char for char in line if char.isdigit()]
    if digits:
        first_digit = int(digits[0])
        last_digit = int(digits[-1])

        value = 10 * first_digit + last_digit
        total_sum += value

print("Part 1:", total_sum)
