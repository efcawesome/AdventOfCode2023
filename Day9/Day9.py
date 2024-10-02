with open("Day9Input.txt") as f:
    value_histories = [[int(z) for z in x.strip().split(" ")] for x in f.readlines()]


def all_zeros(value_hist):
    for value in value_hist:
        if value != 0:
            return False

    return True


def puzzle1():
    extrapolate_sum = 0

    for value_hist in value_histories:
        tree = [value_hist]
        while not all_zeros(tree[-1]): #create tree
            new_arr = []
            for i in range(len(tree[-1]) - 1):
                new_arr.append(tree[-1][i + 1] - tree[-1][i])

            tree.append(new_arr)

        #extrapolate tree
        for num in range(len(tree) - 1, 0, -1):
            tree[num - 1].append(tree[num][-1] + tree[num - 1][-1])

        extrapolate_sum += tree[0][-1]

    print(extrapolate_sum)


def puzzle2():
    extrapolate_sum = 0

    for value_hist in value_histories:
        tree = [value_hist]
        while not all_zeros(tree[-1]): #create tree
            new_arr = []
            for i in range(len(tree[-1]) - 1):
                new_arr.append(tree[-1][i + 1] - tree[-1][i])

            tree.append(new_arr)

        #extrapolate tree
        for num in range(len(tree) - 1, 0, -1):
            tree[num - 1].insert(0, tree[num - 1][0] - tree[num][0])

        extrapolate_sum += tree[0][0]

    print(extrapolate_sum)


puzzle2()