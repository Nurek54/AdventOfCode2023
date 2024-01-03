import math

def read_input(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    times = [int(t) for t in lines[0].split(": ")[1].strip().split()]
    distances = [int(d) for d in lines[1].split(": ")[1].strip().split()]

    return times, distances


def ways_to_win(time, record_distance):
    ways = 0
    for i in range(time):
        speed = i
        time_remaining = time - i
        distance = speed * time_remaining
        if distance > record_distance:
            ways += 1
    return ways


def main(file_path):
    times, distances = read_input(file_path)

    total_ways = [ways_to_win(t, d) for t, d in zip(times, distances)]

    time = int("".join([str(t) for t in times]))
    distance = int("".join([str(d) for d in distances]))

    result = ways_to_win(time, distance)
    print(f"Part 2: {result}")


file_path = "AoC_Day6_Input.txt"
main(file_path)
