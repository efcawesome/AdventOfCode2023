with open("Day11Input.txt") as f:
    universe = [[z for z in x.strip()] for x in f.readlines()]


def expand_universe():
    empty_rows = []
    empty_cols = []

    for c in range(len(universe[0])):
        is_empty = True
        for r in range(len(universe)):
            if universe[r][c] == "#":
                is_empty = False
                break

        if is_empty:
            empty_cols.append(c)

    for row in range(len(universe)):
        is_empty = True
        for col in range(len(universe[row])):
            if universe[row][col] == "#":
                is_empty = False
                break

        if is_empty:
            empty_rows.append(row)

    cols_added = 0
    for column in empty_cols:
        for num in range(100):
            for i in range(len(universe)):
                universe[i].insert(column + cols_added, ".")

            cols_added += 1

    rows_added = 0
    for roww in empty_rows:
        universe.insert(roww + rows_added, ["." for i in universe[roww]])
        rows_added += 1


def get_expanded_universe():
    empty_rows = []
    empty_cols = []

    for c in range(len(universe[0])):
        is_empty = True
        for r in range(len(universe)):
            if universe[r][c] == "#":
                is_empty = False
                break

        if is_empty:
            empty_cols.append(c)

    for row in range(len(universe)):
        is_empty = True
        for col in range(len(universe[row])):
            if universe[row][col] == "#":
                is_empty = False
                break

        if is_empty:
            empty_rows.append(row)

    return [empty_rows, empty_cols]


def puzzle1():
    expand_universe()
    galaxies = []
    for i in range(len(universe)):
        for k in range(len(universe[i])):
            if universe[i][k] == "#":
                galaxies.append([i, k])

    sum_dist = 0
    for num in range(len(galaxies) - 1):
        for j in range(num + 1, len(galaxies)):
            dist = abs(galaxies[j][1] - galaxies[num][1]) + abs(galaxies[j][0] - galaxies[num][0])

            sum_dist += dist

    print(sum_dist)


def puzzle2(expansion_factor):
    expansion_factor -= 1
    expanded_sectors = get_expanded_universe()
    galaxies = []
    for i in range(len(universe)):
        for k in range(len(universe[i])):
            if universe[i][k] == "#":
                galaxies.append([i, k])

    sum_dist = 0
    for num in range(len(galaxies) - 1):
        for j in range(num + 1, len(galaxies)):
            num_exp_rows = 0
            for exp_gal_rows in expanded_sectors[0]:
                if is_between(exp_gal_rows, galaxies[num][0], galaxies[j][0]):
                    num_exp_rows += 1

            num_exp_cols = 0
            for exp_gal_cols in expanded_sectors[1]:
                if is_between(exp_gal_cols, galaxies[num][1], galaxies[j][1]):
                    num_exp_cols += 1

            if galaxies[j][1] > galaxies[num][1]:
                dist = abs(galaxies[j][1] + expansion_factor*num_exp_cols - galaxies[num][1]) + abs(galaxies[j][0] + expansion_factor*num_exp_rows - galaxies[num][0])
            else:
                dist = abs(galaxies[num][1] + expansion_factor * num_exp_cols - galaxies[j][1]) + abs(galaxies[j][0] + expansion_factor * num_exp_rows - galaxies[num][0])
            sum_dist += dist

    print(sum_dist)


def is_between(num, bound1, bound2):
    return (bound1 < num < bound2) or (bound2 < num < bound1)


puzzle2(1000000)
