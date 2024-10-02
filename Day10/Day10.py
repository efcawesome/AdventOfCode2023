from copy import copy

with open("Day10Input.txt") as f:
    ground_pipes = [[x for x in z.strip()] for z in f.readlines()]


def animal_location():
    for i in range(len(ground_pipes)):
        for k in range(len(ground_pipes[i])):
            if ground_pipes[i][k] == "S":
                return [i, k]


def puzzle1():
    al = animal_location()
    distance = 1

    pipe_locs = [Pipe(al[1] - 1, al[0]), Pipe(al[1], al[0] - 1)]
    prev_pipes = [Pipe(al[1], al[0]), Pipe(al[1], al[0])]

    while pipe_locs[0] != pipe_locs[1]:
        for i in range(len(pipe_locs)):
            pipe = ground_pipes[pipe_locs[i].y][pipe_locs[i].x]

            temp_pipe = copy(pipe_locs[i])
            if pipe == "|":
                if prev_pipes[i].y < pipe_locs[i].y: # if previous is above
                    pipe_locs[i] = Pipe(pipe_locs[i].x, pipe_locs[i].y + 1)
                else: # if prev is below
                    pipe_locs[i] = Pipe(pipe_locs[i].x, pipe_locs[i].y - 1)
            elif pipe == "-":
                if prev_pipes[i].x < pipe_locs[i].x: # if previous is left
                    pipe_locs[i] = Pipe(pipe_locs[i].x + 1, pipe_locs[i].y)
                else: # if prev is right
                    pipe_locs[i] = Pipe(pipe_locs[i].x - 1, pipe_locs[i].y)
            elif pipe == "L":
                if prev_pipes[i].y < pipe_locs[i].y: # if previous is above
                    pipe_locs[i] = Pipe(pipe_locs[i].x + 1, pipe_locs[i].y)
                else: # if prev is right
                    pipe_locs[i] = Pipe(pipe_locs[i].x, pipe_locs[i].y - 1)
            elif pipe == "J":
                if prev_pipes[i].y < pipe_locs[i].y: # if previous is above
                    pipe_locs[i] = Pipe(pipe_locs[i].x - 1, pipe_locs[i].y)
                else: # if prev is left
                    pipe_locs[i] = Pipe(pipe_locs[i].x, pipe_locs[i].y - 1)
            elif pipe == "7":
                if prev_pipes[i].y > pipe_locs[i].y: # if previous is below
                    pipe_locs[i] = Pipe(pipe_locs[i].x - 1, pipe_locs[i].y)
                else: # if prev is left
                    pipe_locs[i] = Pipe(pipe_locs[i].x, pipe_locs[i].y + 1)
            elif pipe == "F":
                if prev_pipes[i].y > pipe_locs[i].y: # if previous is below
                    pipe_locs[i] = Pipe(pipe_locs[i].x + 1, pipe_locs[i].y)
                else: # if prev is right
                    pipe_locs[i] = Pipe(pipe_locs[i].x, pipe_locs[i].y + 1)
            prev_pipes[i] = temp_pipe
        distance += 1

    print(distance)


def puzzle2():
    pipe_map = [[[ground_pipes[z][x], False] for x in range(len(ground_pipes[z]))] for z in range(len(ground_pipes))]

    al = animal_location()
    pipe_map[al[0]][al[1]] = ["J", True]

    pipe_locs = [Pipe(al[1] - 1, al[0]), Pipe(al[1], al[0] - 1)]
    prev_pipes = [Pipe(al[1], al[0]), Pipe(al[1], al[0])] # janky af detection

    while pipe_locs[0] != pipe_locs[1]:
        for i in range(len(pipe_locs)):
            pipe = ground_pipes[pipe_locs[i].y][pipe_locs[i].x]

            temp_pipe = copy(pipe_locs[i])
            if pipe == "|":
                if prev_pipes[i].y < pipe_locs[i].y: # if previous is above
                    pipe_locs[i] = Pipe(pipe_locs[i].x, pipe_locs[i].y + 1)
                else: # if prev is below
                    pipe_locs[i] = Pipe(pipe_locs[i].x, pipe_locs[i].y - 1)
            elif pipe == "-":
                if prev_pipes[i].x < pipe_locs[i].x: # if previous is left
                    pipe_locs[i] = Pipe(pipe_locs[i].x + 1, pipe_locs[i].y)
                else: # if prev is right
                    pipe_locs[i] = Pipe(pipe_locs[i].x - 1, pipe_locs[i].y)
            elif pipe == "L":
                if prev_pipes[i].y < pipe_locs[i].y: # if previous is above
                    pipe_locs[i] = Pipe(pipe_locs[i].x + 1, pipe_locs[i].y)
                else: # if prev is right
                    pipe_locs[i] = Pipe(pipe_locs[i].x, pipe_locs[i].y - 1)
            elif pipe == "J":
                if prev_pipes[i].y < pipe_locs[i].y: # if previous is above
                    pipe_locs[i] = Pipe(pipe_locs[i].x - 1, pipe_locs[i].y)
                else: # if prev is left
                    pipe_locs[i] = Pipe(pipe_locs[i].x, pipe_locs[i].y - 1)
            elif pipe == "7":
                if prev_pipes[i].y > pipe_locs[i].y: # if previous is below
                    pipe_locs[i] = Pipe(pipe_locs[i].x - 1, pipe_locs[i].y)
                else: # if prev is left
                    pipe_locs[i] = Pipe(pipe_locs[i].x, pipe_locs[i].y + 1)
            elif pipe == "F":
                if prev_pipes[i].y > pipe_locs[i].y: # if previous is below
                    pipe_locs[i] = Pipe(pipe_locs[i].x + 1, pipe_locs[i].y)
                else: # if prev is right
                    pipe_locs[i] = Pipe(pipe_locs[i].x, pipe_locs[i].y + 1)

            prev_pipes[i] = temp_pipe
            pipe_map[prev_pipes[i].y][prev_pipes[i].x][1] = True

    pipe_map[pipe_locs[0].y][pipe_locs[0].x][1] = True

    interior_num = 0
    for i in range(len(pipe_map)):
        in_pipe = False
        prev_corner = ""
        for k in range(len(pipe_map[i])):
            spot = pipe_map[i][k][0]
            if pipe_map[i][k][1]:
                if spot == "F" or spot == "L":
                    prev_corner = spot

                if spot == "|" or (spot == "7" and prev_corner == "L") or (spot == "J" and prev_corner == "F"):
                    in_pipe = not in_pipe

            if not pipe_map[i][k][1]:
                if in_pipe:
                    pipe_map[i][k][0] = "I"
                    interior_num += 1
                else:
                    pipe_map[i][k][0] = "O"

    [print([x[0] for x in z]) for z in pipe_map]

    print(interior_num)



class Pipe:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

puzzle2()