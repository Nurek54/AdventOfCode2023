file_name = 'AoC_Day1_Input.txt'

with open(file_name) as file:
    data = [line.strip() for line in file]

numbers = [
    "one", "two", "three",
    "four", "five", "six",
    "seven", "eight", "nine"
]

count = 0

for string in data:
    first_digit = 0
    second_digit = 0

    i = 0
    found = False
    while i < len(string) and not found:
        if string[i].isdigit():
            first_digit = int(string[i])
            break

        for x in range(len(numbers)):
            if string[i:].startswith(numbers[x]):
                found = True
                first_digit = x + 1
                break

        i += 1

    j = len(string) - 1
    found = False
    while j >= 0 and not found:
        if string[j].isdigit():
            second_digit = int(string[j])
            break

        for x in range(len(numbers)):
            if string[:j + 1].endswith(numbers[x]):
                found = True
                second_digit = x + 1
                break

        j -= 1

    calibration = first_digit * 10 + second_digit
    count += calibration

print("Part 2:", count)
