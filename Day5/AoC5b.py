def read_input(file_path):
    with open(file_path, 'r') as file:
        inp = file.read()

    parts = inp.split("\n\n")
    seeds = [int(x) for x in parts[0].split(":")[1].split()]
    ref = []
    for i in range(1, len(parts)):
        ref.append([[int(x) for x in s.split()] for s in parts[i].split("\n")[1:]])

    return seeds, ref


def get_state(seed_num, ref):
    cur = seed_num
    for i in range(len(ref)):
        for j in range(len(ref[i])):
            if ref[i][j][1] <= cur < ref[i][j][1] + ref[i][j][2]:
                cur = ref[i][j][0] + cur - ref[i][j][1]
                break
    return cur


def intersect(a, b, c, d):
    return not (b < c or d < a)


def get_min(ranges, ref):
    for i in range(len(ref)):
        new_ranges = []
        for j in range(len(ref[i])):
            if len(ranges) > 0:
                istart = ref[i][j][1]
                iend = ref[i][j][1] + ref[i][j][2] - 1
                cut_ranges = []
                for r in ranges:
                    if intersect(istart, iend, r[0], r[1]):
                        c1 = max(istart, r[0])
                        c2 = min(iend, r[1])
                        new_ranges.append((c1 + ref[i][j][0] - ref[i][j][1], c2 + ref[i][j][0] - ref[i][j][1]))
                        if r[0] < c1:
                            cut_ranges.append((r[0], c1 - 1))
                        if r[1] > c2:
                            cut_ranges.append((c2 + 1, r[1]))
                    else:
                        cut_ranges.append(r)
                ranges = cut_ranges

        ranges = cut_ranges + new_ranges
    return min(r[0] for r in ranges) if ranges else float('inf')


def solve_problem(file_path):
    seeds, ref = read_input(file_path)

    rs = [(seeds[i], seeds[i + 1] + seeds[i] - 1) for i in range(0, len(seeds), 2)]

    result = get_min(rs, ref)
    print("Part 1:", result)


file_path = 'AoC_Day5_Input.txt'
solve_problem(file_path)

