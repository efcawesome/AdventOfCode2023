with open("Day2Input.txt") as f:
    games = [x.strip() for x in f.readlines()]


def puzzle1():
    possible_sum = 0

    for game in games:
        game = game.lstrip("Game ")

        sets = game.split("; ")
        game_num = int(sets[0].split(": ")[0])
        sets[0] = sets[0].split(": ")[1]

        possible = True

        for s in sets:
            cubes = s.split(", ")
            for cube in cubes:
                cube_count = int(cube.split(" ")[0])
                cube_type = cube.split(" ")[1]
                possible = not (cube_count > 14) and not (cube_count > 13 and cube_type != "blue") and not (cube_count > 12 and cube_type != "blue" and cube_type != "green")

                if not possible:
                    break

            if not possible:
                break

        if possible:
            print(game_num)
            possible_sum += game_num

    print(possible_sum)


def puzzle2():
    power_sum = 0

    for game in games:
        maxes = {"red": 0, "blue": 0, "green": 0}
        game = game.lstrip("Game ")

        sets = game.split("; ")
        sets[0] = sets[0].split(": ")[1]

        for s in sets:
            cubes = s.split(", ")
            for cube in cubes:
                cube_count = int(cube.split(" ")[0])
                cube_type = cube.split(" ")[1]

                if maxes[cube_type] < cube_count:
                    maxes[cube_type] = cube_count

        power_sum += maxes["red"]*maxes["blue"]*maxes["green"]

    print(power_sum)


puzzle2()
