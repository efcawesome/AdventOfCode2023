with open("Day18Input.txt") as f:
    plans = [x.strip() for x in f.readlines()]

terrain = [["#"]]


def dig_hole(ind, direction):
    match direction:
        case "U":
            if ind < 0:
                pass


def modify_ind(ind, direction):
    match direction:
        case "U":
            return [ind[0] - 1, ind[1]]
        case "D":
            return [ind[0] + 1, ind[1]]
        case "L":
            return [ind[0], ind[1] - 1]
        case "R":
            return [ind[0], ind[1] + 1]


def puzzle1():
    curr_ind = [0, 0]
    for plan in plans:
        direction = plan.split(" ")[0]
        for i in range(int(plan.split(" ")[1])):
            curr_ind = modify_ind(curr_ind, direction)
            dig_hole(curr_ind, direction)
