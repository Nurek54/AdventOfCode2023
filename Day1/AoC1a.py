import os

file_path = r"C:\Users\g_sie\OneDrive\Pulpit\test.txt"

with open(file_path, 'r') as file:
    input_str = file.read()

lines = input_str.strip().split('\n')

total_sum = 0

for line in lines:
    digits = [char for char in line if char.isdigit()]
    if digits:
        first_digit = int(digits[0])
        last_digit = int(digits[-1])

        value = 10 * first_digit + last_digit
        total_sum += value

print(f"The sum of all calibration values is {total_sum}.")