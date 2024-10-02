with open("Day6Input.txt") as f:
    races = [x.strip() for x in f.readlines()]

def puzzle1():
    times = [int(t) for t in races[0].strip("Time: ").split(" ") if t.isnumeric()]
    distances = [int(d) for d in races[1].strip("Distance: ").split(" ") if d.isnumeric()]

    error_margin = 1

    for i in range(len(times)):
        num_wins = 0
        for num in range(times[i] + 1):
            dist = (times[i] - num) * num
            if dist > distances[i]:
                num_wins += 1

        error_margin *= num_wins

    print(error_margin)


def puzzle2():
    time = 55826490
    distance = 246144110121111

    first_win = 0
    num = 0
    while num < time:
        dist = (time - num) * num
        if dist > distance:
            first_win = num
            break

        num += 1

    last_win = 0
    num = time
    while num > 0:
        dist = (time - num) * num
        if dist > distance:
            last_win = num
            break

        num -= 1

    print(last_win - first_win + 1)


puzzle2()
