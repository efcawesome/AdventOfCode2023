from copy import deepcopy

with open("Day12Input.txt") as f:
    records = [[[y for y in x.split(" ")[0]], [int(z) for z in x.strip().split(" ")[1].split(",")]] for x in f.readlines()]


def puzzle1():
    sum_possible = 0
    for line in records:
        sum_p = test_case(line)
        sum_possible += sum_p
        print(sum_p)

    print(sum_possible)


def get_new_record(line):
    new_l = []
    new_c = []
    for i in range(5):
        [new_l.append(l) for l in line[0]]
        if i != 4:
            new_l.append("?")
        [new_c.append(c) for c in line[1]]

    return [new_l, new_c]


def puzzle2():
    sum_possible = 0
    for line in records:
        new_rec = get_new_record(line)
        sum_p = test_case(new_rec)
        sum_possible += sum_p

    print(sum_possible)


def test_case(line):
    if line[0].count("?") == 0 and valid_case(line):
        return 1

    for c in enumerate(line[0]):
        if c[1] == "?":
            new_l_hash = deepcopy(line)
            new_l_hash[0][c[0]] = "#"
            new_l_dot = deepcopy(line)
            new_l_dot[0][c[0]] = "."
            return test_case(new_l_dot) + test_case(new_l_hash)

    return 0


def is_valid_case(line):
    curr_spring_ind = 0
    curr_spring_count = 0
    for c in line[0]:
        if c == "#":
            curr_spring_count += 1
        elif curr_spring_count > 0:
            if curr_spring_ind > len(line[1]) - 1 or curr_spring_count != line[1][curr_spring_ind]:
                return False
            else:
                curr_spring_ind += 1
                curr_spring_count = 0

    if curr_spring_ind < len(line[1]) and line[0][-1] == "#":
        return curr_spring_count == line[1][curr_spring_ind]
    elif curr_spring_ind < len(line[1]):
        return True


def valid_case(line):
    spring_counts = deepcopy(line[1])
    curr_count = 0

    for c in line[0]:
        if c == "#":
            curr_count += 1
            if len(spring_counts) == 0:
                return False
            if curr_count > spring_counts[0]:
                return False
        elif curr_count > 0:
            if len(spring_counts) == 0:
                return False
            elif curr_count == spring_counts[0]:
                curr_count = 0
                spring_counts.remove(spring_counts[0])
            else:
                return False

    if curr_count > 0:
        if curr_count != spring_counts[0]:
            return False
        else:
            spring_counts.remove(spring_counts[0])

    return len(spring_counts) == 0




puzzle2()