with open("Day3Input.txt") as f:
    schematic = [x.strip() for x in f.readlines()]


def puzzle1():
    part_sum = 0
    for i in range(len(schematic)):
        print(schematic[i])
        print(len(schematic[i]))
        curr_num = ""
        for j in range(len(schematic[i])):
            if schematic[i][j].isnumeric():
                curr_num += schematic[i][j]

            if (not schematic[i][j].isnumeric() and curr_num != "") or (j == len(schematic[i]) - 1 and curr_num != ""):
                if j == len(schematic[i]) - 1 and schematic[i][j].isnumeric():
                    location = j + 1 - len(curr_num)
                else:
                    location = j - len(curr_num)

                if is_part_num(i, location, len(curr_num)):
                    print(curr_num)
                    part_sum += int(curr_num)

                curr_num = ""

    print(part_sum)


def is_part_num(i, location, num_len):
    if location == 0:
        if is_symbol(schematic[i][num_len]): #in front
            return True

        for k in range(num_len + 1):
            if i != len(schematic) - 1: #below
                if is_symbol(schematic[i + 1][location + k]):
                    return True
            if i != 0: #above
                if is_symbol(schematic[i - 1][location + k]):
                    return True

    elif location == len(schematic[i]) - num_len:
        print("meow")
        if is_symbol(schematic[i][location - 1]):
            return True

        for k in range(num_len + 1):
            if i != len(schematic) - 1: #below
                if is_symbol(schematic[i + 1][location - 1 + k]):
                    return True
            if i != 0: #above
                if is_symbol(schematic[i - 1][location - 1 + k]):
                    return True
    else:
        if is_symbol(schematic[i][location - 1]) or is_symbol(schematic[i][location + num_len]):
            return True

        for k in range(num_len + 2):
            if i != len(schematic) - 1: #below
                if is_symbol(schematic[i + 1][location - 1 + k]):
                    return True
            if i != 0: #above
                if is_symbol(schematic[i - 1][location - 1 + k]):
                    return True


def is_symbol(c):
    return c != "." and not c.isnumeric()


def puzzle2():
    gear_sum = 0

    for row in range(len(schematic)):
        print(schematic[row])
        for col in range(len(schematic[row])):
            if schematic[row][col] == "*":
                num_indexes = []
                gear_ratio = 1
                # above
                if schematic[row - 1][col - 1].isnumeric() and schematic[row - 1][col].isnumeric() and schematic[row - 1][col + 1].isnumeric():
                    num_indexes.append([row - 1, col - 1])
                elif not schematic[row - 1][col - 1].isnumeric() and schematic[row - 1][col].isnumeric() and not schematic[row - 1][col + 1].isnumeric():
                    num_indexes.append([row - 1, col])
                else:
                    if schematic[row - 1][col - 1].isnumeric():
                        num_indexes.append([row - 1, col - 1])
                    if schematic[row - 1][col + 1].isnumeric():
                        num_indexes.append([row - 1, col + 1])

                # sides
                if schematic[row][col - 1].isnumeric():
                    num_indexes.append([row, col - 1])
                if schematic[row][col + 1].isnumeric():
                    num_indexes.append([row, col + 1])

                # below
                if schematic[row + 1][col - 1].isnumeric() and schematic[row + 1][col].isnumeric() and schematic[row + 1][col + 1].isnumeric():
                    num_indexes.append([row + 1, col - 1])
                elif not schematic[row + 1][col - 1].isnumeric() and schematic[row + 1][col].isnumeric() and not schematic[row + 1][col + 1].isnumeric():
                    num_indexes.append([row - 1, col])
                else:
                    if schematic[row + 1][col - 1].isnumeric():
                        num_indexes.append([row + 1, col - 1])
                    if schematic[row + 1][col + 1].isnumeric():
                        num_indexes.append([row + 1, col + 1])

                if len(num_indexes) == 2:
                    for ind in num_indexes:
                        r = ind[0]
                        c = ind[1]

                        i = c
                        while i >= 0 and schematic[r][i].isnumeric():
                            i -= 1

                        i += 1

                        num = ""
                        while i < len(schematic[r]) and schematic[r][i].isnumeric():
                            num += schematic[r][i]
                            i += 1

                        print(num, end=",")

                        gear_ratio *= int(num)
                    print()
                    gear_sum += gear_ratio

    print(gear_sum)


puzzle2()
