def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    seeds = []
    conversion_maps = {}

    current_section = None

    for line in lines:
        if line.startswith("seeds:"):
            seeds = list(map(int, line.split()[1:]))
        elif line.startswith("seed-to-soil map:"):
            current_section = "seed-to-soil"
            conversion_maps[current_section] = []
        elif line.startswith("soil-to-fertilizer map:"):
            current_section = "soil-to-fertilizer"
            conversion_maps[current_section] = []
        elif line.startswith("fertilizer-to-water map:"):
            current_section = "fertilizer-to-water"
            conversion_maps[current_section] = []
        elif line.startswith("water-to-light map:"):
            current_section = "water-to-light"
            conversion_maps[current_section] = []
        elif line.startswith("light-to-temperature map:"):
            current_section = "light-to-temperature"
            conversion_maps[current_section] = []
        elif line.startswith("temperature-to-humidity map:"):
            current_section = "temperature-to-humidity"
            conversion_maps[current_section] = []
        elif line.startswith("humidity-to-location map:"):
            current_section = "humidity-to-location"
            conversion_maps[current_section] = []
        elif current_section:
            conversion_maps[current_section].append(list(map(int, line.split())))
        else:
            current_section = None

    return seeds, conversion_maps

def convert_number(number, conversion_maps):
    for section, maps in conversion_maps.items():
        for conversion_map in maps:
            if conversion_map:
                dest_start, source_start, length = conversion_map if len(conversion_map) == 3 else (conversion_map[0], 0, 1)
                if number >= source_start and number < source_start + length:
                    return dest_start + (number - source_start)
    return number


def find_lowest_location(seeds, conversion_maps):
    current_numbers = seeds.copy()

    for section in ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water",
                    "water-to-light", "light-to-temperature", "temperature-to-humidity",
                    "humidity-to-location"]:
        maps = conversion_maps.get(section, [])
        next_numbers = []
        for number in current_numbers:
            next_number = convert_number(number, {section: maps})
            next_numbers.append(next_number)
        current_numbers = next_numbers

    return min(current_numbers)

file_path = 'AoC_Day5_Input.txt'
seeds, conversion_maps = read_input(file_path)

result = find_lowest_location(seeds, conversion_maps)
print(result)
