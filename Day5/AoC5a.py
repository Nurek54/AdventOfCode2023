def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    seeds = []
    conversion_maps = {}

    current_section = None

    for line in lines:
        words = line.split()
        if not words:
            continue  # Skip empty lines
        if words[0] == "seeds:":
            seeds = list(map(int, words[1:]))
        elif len(words) > 0 and (words[0] == "seed-to-soil" or words[0] == "soil-to-fertilizer" or \
                                 words[0] == "fertilizer-to-water" or words[0] == "water-to-light" or \
                                 words[0] == "light-to-temperature" or words[0] == "temperature-to-humidity" or \
                                 words[0] == "humidity-to-location"):
            current_section = words[0]
            conversion_maps[current_section] = []
        elif current_section:
            conversion_maps[current_section].append(list(map(int, words)))
        else:
            current_section = None

    return seeds, conversion_maps

def convert_number(number, conversion_maps):
    for section, maps in conversion_maps.items():
        for conversion_map in maps:
            dest_start, source_start, length = conversion_map if len(conversion_map) == 3 else (conversion_map[0], 0, 1)
            if source_start <= number < source_start + length:
                return dest_start + (number - source_start)
    return number

def find_lowest_location(seeds, conversion_maps):
    current_numbers = seeds.copy()

    for section in ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water",
                    "water-to-light", "light-to-temperature", "temperature-to-humidity",
                    "humidity-to-location"]:
        maps = conversion_maps.get(section, [])
        current_numbers = [convert_number(number, {section: maps}) for number in current_numbers]

    return min(current_numbers)

file_path = 'AoC_Day5_Input.txt'
seeds, conversion_maps = read_input(file_path)

result = find_lowest_location(seeds, conversion_maps)
print("Part 1:", result)
