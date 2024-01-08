import re

def load_input_file(file_path):
    with open(file_path) as file:
        return file.read().rstrip()

def is_accepted(current_condition, instructions, sss):
    if current_condition == 'A':
        return True

    if current_condition == 'R':
        return False

    condition_list = instructions[current_condition]

    for condition in condition_list:
        if ':' in condition:
            tokens = condition.split(':')

            if '>' in tokens[0]:
                z = tokens[0].split('>')
                if sss[z[0]] > int(z[1]):
                    return is_accepted(tokens[1], instructions, sss)
                else:
                    continue

            if '<' in tokens[0]:
                z = tokens[0].split('<')
                if sss[z[0]] < int(z[1]):
                    return is_accepted(tokens[1], instructions, sss)
                else:
                    continue

            raise Exception('Błąd')

        return is_accepted(condition, instructions, sss)

def first_part(task_input):
    instructions, coordinates = task_input.split('\n\n')

    instruct = dict()
    for i in instructions.splitlines():
        tmp = i.split('{')
        name = tmp[0]
        instruct[name] = list(tmp[1][:-1].split(','))

    result = 0
    for c in coordinates.splitlines():
        g = re.match(r'{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}', c)
        if g:
            sss = {
                'x': int(g[1]),
                'm': int(g[2]),
                'a': int(g[3]),
                's': int(g[4])
            }

            if is_accepted('in', instruct, sss):
                result += sum(sss.values())

        else:
            assert False

    return result

def valid_combinations(current_condition, instructions, sss, index):
    if current_condition == 'A':
        return (sss['x'][1] - sss['x'][0] + 1) * \
               (sss['m'][1] - sss['m'][0] + 1) * \
               (sss['a'][1] - sss['a'][0] + 1) * \
               (sss['s'][1] - sss['s'][0] + 1)

    if current_condition == 'R':
        return 0

    condition_list = instructions[current_condition]
    condition = condition_list[index]

    if ':' in condition:
        tokens = condition.split(':')
        next_condition = tokens[1]

        if '>' in tokens[0]:
            z = tokens[0].split('>')
            from_what = z[0]
            value = int(z[1])

            if value < sss[from_what][0]:
                return valid_combinations(next_condition, instructions, sss, 0)

            if value > sss[from_what][1]:
                return 0

            ss = sss.copy()
            ss[from_what] = (sss[from_what][0], value)
            a = valid_combinations(current_condition, instructions, ss, index + 1)

            ss[from_what] = (value + 1, sss[from_what][1])
            b = valid_combinations(next_condition, instructions, ss, 0)

            return a + b

        if '<' in tokens[0]:
            z = tokens[0].split('<')
            from_what = z[0]
            value = int(z[1])

            if value < sss[from_what][0]:
                return 0

            if value > sss[from_what][1]:
                return valid_combinations(next_condition, instructions, sss, 0)

            ss = sss.copy()
            ss[from_what] = (sss[from_what][0], value - 1)
            a = valid_combinations(next_condition, instructions, ss, 0)

            ss[from_what] = (value, sss[from_what][1])
            b = valid_combinations(current_condition, instructions, ss, index + 1)

            return a + b

        raise Exception('Błąd')

    return valid_combinations(condition, instructions, sss, 0)

file_path = "AoC_Day19_Input.txt"

input_data = load_input_file(file_path)

result_first_part = first_part(input_data)
print("Part 1:", result_first_part)
