with open("Day15Input.txt") as f:
    steps = f.readlines()[0].strip().split(",")


def puzzle1():
    sum_steps = 0
    for step in steps:
        sum_steps += get_hash(step)

    print(sum_steps)


def puzzle2():
    boxes = [{} for i in range(256)]

    for step in steps:
        label = ""
        dash = True
        focal_lens = -1
        for c in enumerate(step):
            if c[1] != "=" and c[1] != "-":
                label += c[1]
            else:
                if c[1] == "=":
                    dash = False
                    focal_lens = int(step.split("=")[1])

                break

        box_num = get_hash(label)

        if dash:
            if label in boxes[box_num]:
                del boxes[box_num][label]
        else:
            if label in boxes[box_num]:
                boxes[box_num][label] = focal_lens
            else:
                boxes[box_num][label] = focal_lens

    print(get_focusing_power(boxes))


def get_focusing_power(boxes):
    sum_foc_lens = 0
    for box in enumerate(boxes):
        box_labels = [l for l in box[1]]
        for lens in enumerate(box_labels):
            sum_foc_lens += (box[0] + 1)*(lens[0] + 1)*(boxes[box[0]][lens[1]])

    return sum_foc_lens


def get_hash(step):
    curr_num = 0
    for c in step:
        curr_num += ord(c)
        curr_num *= 17
        curr_num %= 256

    return curr_num


puzzle2()