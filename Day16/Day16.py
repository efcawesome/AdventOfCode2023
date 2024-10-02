from copy import deepcopy

with open("Day16Input.txt") as f:
    contraption = [[z for z in x.strip()] for x in f.readlines()]

energized_inds = set("")

used_starting_params = []


def reflect_mirror(row_col, dir):
    new_rc = deepcopy(row_col)

    if f"{row_col} {dir}" in used_starting_params:
        return None
    else:
        used_starting_params.append(f"{row_col} {dir}")

    match dir:
        case "U":
            while new_rc[0] >= 0:
                energized_inds.add(f"{new_rc}")

                match contraption[new_rc[0]][new_rc[1]]:
                    case "-":
                        reflect_mirror(new_rc, "L")
                        reflect_mirror(new_rc, "R")
                        return None
                    case "/":
                        if new_rc[1] < len(contraption[0]) - 1:
                            reflect_mirror([new_rc[0], new_rc[1] + 1], "R")
                        return None
                    case "\\":
                        if new_rc[1] > 0:
                            reflect_mirror([new_rc[0], new_rc[1] - 1], "L")
                        return None
                    case _:
                        new_rc[0] -= 1
        case "D":
            while new_rc[0] < len(contraption):
                energized_inds.add(f"{new_rc}")

                match contraption[new_rc[0]][new_rc[1]]:
                    case "-":
                        reflect_mirror(new_rc, "L")
                        reflect_mirror(new_rc, "R")
                        return None
                    case "/":
                        if new_rc[1] > 0:
                            reflect_mirror([new_rc[0], new_rc[1] - 1], "L")
                        return None
                    case "\\":
                        if new_rc[1] < len(contraption[0]) - 1:
                            reflect_mirror([new_rc[0], new_rc[1] + 1], "R")
                        return None
                    case _:
                        new_rc[0] += 1
        case "L":
            while new_rc[1] >= 0:
                energized_inds.add(f"{new_rc}")

                match contraption[new_rc[0]][new_rc[1]]:
                    case "|":
                        reflect_mirror(new_rc, "U")
                        reflect_mirror(new_rc, "D")
                        return None
                    case "/":
                        if new_rc[0] < len(contraption) - 1:
                            reflect_mirror([new_rc[0] + 1, new_rc[1]], "D")
                        return None
                    case "\\":
                        if new_rc[0] > 0:
                            reflect_mirror([new_rc[0] - 1, new_rc[1]], "U")
                        return None
                    case _:
                        new_rc[1] -= 1
        case "R":
            while new_rc[1] < len(contraption[0]):
                energized_inds.add(f"{new_rc}")

                match contraption[new_rc[0]][new_rc[1]]:
                    case "|":
                        reflect_mirror(new_rc, "U")
                        reflect_mirror(new_rc, "D")
                        return None
                    case "/":
                        if new_rc[0] > 0:
                            reflect_mirror([new_rc[0] - 1, new_rc[1]], "U")
                        return None
                    case "\\":
                        if new_rc[0] < len(contraption) - 1:
                            reflect_mirror([new_rc[0] + 1, new_rc[1]], "D")
                        return None
                    case _:
                        new_rc[1] += 1


def puzzle1():
    print(get_energized_count([0, 0], "R"))


def get_energized_count(start, direction):
    energized_inds.clear()
    used_starting_params.clear()
    reflect_mirror(start, direction)
    count = len(energized_inds)
    used_starting_params.clear()
    energized_inds.clear()
    return count


def puzzle2():
    energized_counts = []

    for col in range(len(contraption[0])):
        energized_counts.append(get_energized_count([0, col], "D"))
        energized_counts.append(get_energized_count([len(contraption) - 1, col], "U"))

    for row in range(len(contraption)):
        energized_counts.append(get_energized_count([row, 0], "R"))
        energized_counts.append(get_energized_count([row, len(contraption[0]) - 1], "L"))

    print(max(energized_counts))


puzzle2()
