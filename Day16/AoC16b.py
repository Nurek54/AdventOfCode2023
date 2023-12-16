input_file_path = 'AoC_Day16_Input.txt'
input_data = open(input_file_path).read().strip().split()

def explore_beam(starting_position):
    visited_positions = set()
    beams_to_explore = [starting_position]

    while any(beams_to_explore):
        for i, beam in enumerate(beams_to_explore):
            if not beam:
                continue
            (x, y), (dx, dy) = beam
            if beam in visited_positions:
                beams_to_explore[i] = None
            else:
                visited_positions.add(beam)
                x += dx
                y += dy
                if min(x, y) < 0 or y >= len(input_data) or x >= len(input_data[0]):
                    beams_to_explore[i] = None
                    continue
                cell = input_data[y][x]
                if cell == '/':
                    dx, dy = -dy, -dx
                elif cell == '\\':
                    dx, dy = dy, dx
                elif cell == '-' and dy:
                    dx, dy = 1, 0
                    beams_to_explore.append(((x, y), (-1, 0)))
                elif cell == '|' and dx:
                    dx, dy = 0, 1
                    beams_to_explore.append(((x, y), (0, -1)))
                beams_to_explore[i] = (x, y), (dx, dy)

    return len({p for p, _ in visited_positions}) - 1

start_position_part1 = ((-1, 0), (1, 0))
print('Part 1:', explore_beam(start_position_part1))

start_positions_part2 = [
    ((i, -1), (0, 1)) for i in range(len(input_data[0]))] + [
    ((i, len(input_data)), (0, -1)) for i in range(len(input_data[0]))] + [
    ((-1, i), (1, 0)) for i in range(len(input_data))] + [
    ((len(input_data[0]), i), (-1, 0)) for i in range(len(input_data))]

print('Part 2:', max(explore_beam(start_position) for start_position in start_positions_part2))
