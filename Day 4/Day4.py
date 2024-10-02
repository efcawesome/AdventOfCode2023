with open("Day4Input.txt") as f:
    cards = [x.strip() for x in f.readlines()]


def puzzle1():
    sum_points = 0
    for i in range(len(cards)):
        winning_nums = get_wcard_nums(i)
        card_nums = get_card_nums(i)

        sum_points += get_card_points(winning_nums, card_nums)

    print(sum_points)


def get_wcard_nums(i):
    card = cards[i]
    nums = card.split(": ")[1]
    winning_nums = [int(s) for s in nums.split(" | ")[0].split(" ") if s.isnumeric()]

    return winning_nums


def get_card_nums(i):
    card = cards[i]
    nums = card.split(": ")[1]
    card_nums = [int(t) for t in nums.split(" | ")[1].split(" ") if t.isnumeric()]

    return card_nums


def get_card_points(wc, c):
    points = 0
    for wnum in wc:
        for cnum in c:
            if wnum == cnum:
                if points == 0:
                    points = 1
                else:
                    points *= 2
                break

    return points


def get_card_matches(wc, c):
    matches = 0
    for wnum in wc:
        for cnum in c:
            if wnum == cnum:
                matches += 1
                break

    return matches


def puzzle2(row, orig):
    card_total = 1
    winning_nums = get_wcard_nums(row)
    nums = get_card_nums(row)

    matches = get_card_matches(winning_nums, nums)

    if matches != 0:
        for r in range(matches):
            card_total += puzzle2(row + r + 1, False)

    if orig and row != len(cards) - 1:
        card_total += puzzle2(row + 1, True)

    return card_total


def sum_list(listy):
    sum_l = 0
    for term in listy:
        sum_l += term

    return sum_l


print(puzzle2(0, True))