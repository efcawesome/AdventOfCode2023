with open("Day1Input.txt") as f:
    instructions = [x.strip() for x in f.readlines()]

nums = []


def puzzle1():
    for x in instructions:
        curr_num = ""
        for c in x:
            try:
                num = int(c)
                curr_num += c
                break
            except ValueError:
                print("no")

        for c in x[::-1]:
            try:
                num = int(c)
                curr_num += c
                break
            except ValueError:
                print("no")

        print(curr_num)
        nums.append(curr_num)

    print(add_nums())


def add_nums():
    sum_nums = 0
    for s in nums:
        sum_nums += int(s)
    return sum_nums


def puzzle2():
    num_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for x in instructions:
        curr_num = ""
        first_word = -1
        last_word = -1
        for w in num_words:
            if first_word > x.find(w) > -1 or first_word == -1:
                first_word = x.find(w)
            if x.rfind(w) > last_word:
                last_word = x.rfind(w)
        print(first_word)
        print(last_word)

        first_num = -1
        last_num = -1
        for c in x:
            try:
                num = int(c)
                first_num = x.find(c)
                print(first_num)
                break
            except ValueError:
                continue

        for c in x[::-1]:
            try:
                num = int(c)
                last_num = x.rfind(c)
                print(last_num)
                break
            except ValueError:
                continue

        if (first_num != -1 and first_num < first_word) or first_word == -1:
            curr_num += x[first_num]
        else:
            for w in num_words:
                if x.find(w) == first_word:
                    curr_num += convert_to_num(w)

        if last_num > last_word:
            curr_num += x[last_num]
        else:
            for w in num_words:
                if x.rfind(w) == last_word:
                    curr_num += convert_to_num(w)

        print(curr_num)
        nums.append(curr_num)

    print(add_nums())


def convert_to_num(word_num):
    if word_num == "one":
        return "1"
    elif word_num == "two":
        return "2"
    elif word_num == "three":
        return "3"
    elif word_num == "four":
        return "4"
    elif word_num == "five":
        return "5"
    elif word_num == "six":
        return "6"
    elif word_num == "seven":
        return "7"
    elif word_num == "eight":
        return "8"
    else:
        return "9"


puzzle2()

