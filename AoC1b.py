word_to_digit_mapping = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'zero': 0
}

def find_first_digit_or_word(line):
    current_word = ''
    for char in line:
        if char.isnumeric():
            return int(char)
        elif char.isalpha():
            current_word += char.lower()
            if current_word in word_to_digit_mapping:
                return word_to_digit_mapping[current_word]
        else:
            current_word = ''
    return None

def find_last_digit_or_word(line):
    current_word = ''
    last_digit = None
    for char in reversed(line):
        if char.isnumeric() and last_digit is None:
            last_digit = int(char)
        elif char.isalpha():
            current_word = char.lower() + current_word
            if current_word in word_to_digit_mapping:
                return word_to_digit_mapping[current_word]
        else:
            current_word = ''
    return last_digit




def calculate_calibration_sum(lines):
    total_sum = 0

    for line in lines:
        real_first_digit = find_first_digit_or_word(line)
        real_last_digit = find_last_digit_or_word(line)

        # If at least one numeric digit or word is found in the line
        if real_first_digit is not None or real_last_digit is not None:
            calibration_value = int(str(real_first_digit) + str(real_last_digit) if real_first_digit is not None and real_last_digit is not None else
                                   str(real_first_digit) if real_first_digit is not None else
                                   str(real_last_digit) if real_last_digit is not None else '')
            total_sum += calibration_value
            print(f"Line: {line}, Real First Digit/Word: {real_first_digit}, Real Last Digit/Word: {real_last_digit}, Calibration Value: {calibration_value}")

    return total_sum

# Example usage:
lines = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
result = calculate_calibration_sum(lines)
print("Sum of calibration values:", result)
