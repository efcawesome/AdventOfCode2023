from copy import deepcopy

with open("Day14Input.txt") as f:
    platform = [[z for z in x.strip()] for x in f.readlines()]


def get_load(p):
    load = 0
    for plat in enumerate(p):
        for space in enumerate(plat[1]):
            if space[1] == "O":
                load += len(p) - plat[0]

    return load


def tilt_north():
    did_something = True
    while did_something:
        did_something = False
        for plat in enumerate(platform):
            if plat[0] != 0:
                for space in enumerate(plat[1]):
                    if space[1] == "O" and platform[plat[0] - 1][space[0]] != "#" and platform[plat[0] - 1][space[0]] != "O":
                        platform[plat[0] - 1][space[0]] = "O"
                        platform[plat[0]][space[0]] = "."
                        did_something = True


def tilt_west():
    did_something = True
    while did_something:
        did_something = False
        for col in enumerate(platform[0]):
            if col[0] != 0:
                for row in enumerate(platform):
                    if platform[row[0]][col[0]] == "O" and platform[row[0]][col[0] - 1] != "#" and platform[row[0]][col[0] - 1] != "O":
                        platform[row[0]][col[0] - 1] = "O"
                        platform[row[0]][col[0]] = "."
                        did_something = True


def tilt_south():
    did_something = True
    while did_something:
        did_something = False
        for plat in enumerate(platform):
            if plat[0] != len(platform) - 1:
                for space in enumerate(plat[1]):
                    if space[1] == "O" and platform[plat[0] + 1][space[0]] != "#" and platform[plat[0] + 1][space[0]] != "O":
                        platform[plat[0] + 1][space[0]] = "O"
                        platform[plat[0]][space[0]] = "."
                        did_something = True


def tilt_east():
    did_something = True
    while did_something:
        did_something = False
        for col in enumerate(platform[0]):
            if col[0] != len(platform[0]) - 1:
                for row in enumerate(platform):
                    if platform[row[0]][col[0]] == "O" and platform[row[0]][col[0] + 1] != "#" and platform[row[0]][col[0] + 1] != "O":
                        platform[row[0]][col[0] + 1] = "O"
                        platform[row[0]][col[0]] = "."
                        did_something = True


def do_cycle():
    tilt_north()
    tilt_west()
    tilt_south()
    tilt_east()


def puzzle1():
    tilt_north()

    print(get_load(platform))


def puzzle2():
    prev_cycles = []
    cycle = 0
    while True:
        prev_cycles.append(deepcopy(platform))
        do_cycle()
        cycle += 1
        if platform in prev_cycles:
            break

    repeat_num = cycle - prev_cycles.index(platform)

    jump_cycle = prev_cycles.index(platform) + int((1000000000 - prev_cycles.index(platform))/repeat_num)*repeat_num

    while jump_cycle < 1000000000:
        do_cycle()
        jump_cycle += 1

    print(get_load(platform))

puzzle2()
