with open("Day17Input.txt") as f:
    blocks = [[int(z) for z in x.strip()] for x in f.readlines()]


def solve_maze(ind, last_ind):
    row = ind[0]
    col = ind[1]
    if row == len(blocks) - 1 and col == len(blocks[row]) - 1:
        return blocks[row][col]

    min_loc_temp = (100, [])

    if row > 0 and [row - 1, col] != last_ind:  # up
        if blocks[row - 1][col] < min_loc_temp[0]:
            min_loc_temp = (blocks[row - 1][col], [row - 1, col])

    if row < len(blocks) - 1 and [row + 1, col] != last_ind:  # down
        if blocks[row + 1][col] < min_loc_temp[0]:
            min_loc_temp = (blocks[row + 1][col], [row + 1, col])

    if col > 0 and [row, col - 1] != last_ind:
        if blocks[row][col - 1] < min_loc_temp[0]:  # left
            min_loc_temp = (blocks[row][col - 1], [row, col - 1])

    if col < len(blocks[row]) and [row, col + 1] != last_ind:
        if blocks[row][col + 1] < min_loc_temp[0]:  # right
            min_loc_temp = (blocks[row][col + 1], [row, col + 1])

    if ind == [0, 0]:
        return blocks[0][0] + min_loc_temp[0] + solve_maze(min_loc_temp[1], [row, col])
    else:
        return min_loc_temp[0] + solve_maze(min_loc_temp[1], [row, col])


def puzzle1():
    print(solve_maze([0, 0], [0, 0]))


puzzle1()