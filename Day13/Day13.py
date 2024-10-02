from copy import copy, deepcopy

with open("Day13Input.txt") as f:
    lines = [x.strip() for x in f.readlines()]


def get_patterns():
    patterns = []
    pattern = []
    for line in lines:
        if line != "":
            pattern.append([line[i] for i in range(len(line))])
        else:
            patterns.append(pattern)
            pattern = []

    patterns.append(pattern)

    return patterns


def get_horiz_symm_num(pattern):
    for i in range(len(pattern)):
        j = 1
        is_symm = False
        while i - j > -1 and i + j - 1 < len(pattern):
            if pattern[i - j] == pattern[i + j - 1]:
                is_symm = True
            else:
                is_symm = False
                break
            j += 1

        if is_symm:
            return i

    return 0


def get_vert_symm_sum(pattern):
    for j in range(len(pattern[0])):
        k = 1
        is_symm = False
        while j - k > -1 and j + k - 1 < len(pattern[0]):
            col1 = ""
            col2 = ""
            for i in range(len(pattern)):
                col1 += pattern[i][j - k]
                col2 += pattern[i][j + k - 1]

            if col1 == col2:
                is_symm = True
            else:
                is_symm = False
                break
            k += 1

        if is_symm:
            return j

    return 0


def get_new_horiz_symm_num(pattern, old_pattern):
    for i in range(len(pattern)):
        j = 1
        is_symm = False
        while i - j > -1 and i + j - 1 < len(pattern):
            if pattern[i - j] == pattern[i + j - 1]:
                is_symm = True
            else:
                is_symm = False
                break
            j += 1

        if is_symm and i != get_horiz_symm_num(old_pattern):
            return i

    return 0


def get_new_vert_symm_sum(pattern, old_pattern):
    for j in range(len(pattern[0])):
        k = 1
        is_symm = False
        while j - k > -1 and j + k - 1 < len(pattern[0]):
            col1 = ""
            col2 = ""
            for i in range(len(pattern)):
                col1 += pattern[i][j - k]
                col2 += pattern[i][j + k - 1]

            if col1 == col2:
                is_symm = True
            else:
                is_symm = False
                break
            k += 1

        if is_symm and j != get_vert_symm_sum(old_pattern):
            return j

    return 0


def puzzle1():
    patterns = get_patterns()
    horiz_sum = 0
    vert_sum = 0
    for pattern in patterns:
        horiz_sum += get_horiz_symm_num(pattern)
        vert_sum += get_vert_symm_sum(pattern)

    print(vert_sum + 100*horiz_sum)


def get_smudge(pattern):

    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            new_pat = deepcopy(pattern)
            if new_pat[i][j] == "#":
                new_pat[i][j] = "."
            else:
                new_pat[i][j] = "#"

            if get_new_horiz_symm_num(new_pat, pattern) != 0 and get_new_horiz_symm_num(new_pat, pattern) != get_horiz_symm_num(pattern):
                return get_new_horiz_symm_num(new_pat, pattern), "h"

            if get_new_vert_symm_sum(new_pat, pattern) != 0 and get_new_vert_symm_sum(new_pat, pattern) != get_vert_symm_sum(pattern):
                return get_new_vert_symm_sum(new_pat, pattern), "v"


def puzzle2():
    patterns = get_patterns()

    horiz_sum = 0
    vert_sum = 0

    for pattern in patterns:
        if get_smudge(pattern)[1] == "h":
            horiz_sum += get_smudge(pattern)[0]
        else:
            vert_sum += get_smudge(pattern)[0]

    print(vert_sum + horiz_sum*100)



puzzle2()
