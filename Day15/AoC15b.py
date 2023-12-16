input_data = open('AoC_Day15_Input.txt').read().strip().split(',')

part1 = 0
part2 = 0

def custom_hash(string):
    hash_value = 0
    for char in string:
        hash_value += ord(char)
        hash_value *= 17
        hash_value %= 256
    return hash_value

lens_boxes = [[] for _ in range(256)]
lens_lengths = [{} for _ in range(256)]

# Process each input element
for index, element in enumerate(input_data):
    part1 += custom_hash(element)

    label = element.split("=")[0].split("-")[0]
    hash_value = custom_hash(label)

    if "-" in element:
        if label in lens_boxes[hash_value]:
            lens_boxes[hash_value].remove(label)
    if "=" in element:
        if label not in lens_boxes[hash_value]:
            lens_boxes[hash_value].append(label)
        lens_lengths[hash_value][label] = int(element.split("=")[1])

for box, lenses in enumerate(lens_boxes):
    for position, lens in enumerate(lenses):
        part2 += (box + 1) * (position + 1) * lens_lengths[box][lens]

print("Part 1:", part1)
print("Part 2:", part2)
