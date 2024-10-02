with open("Day7Input.txt") as f:
    fr = f.readlines()
    hands = [x.strip().split(" ")[0] for x in fr]
    bids = [x.strip().split(" ")[1] for x in fr]

card_type_inds = {"five_kind": [], "four_kind": [], "full_house": [], "three_kind": [], "two_pair": [], "one_pair": [], "high": []}
card_type_names = ["five_kind", "four_kind", "full_house", "three_kind", "two_pair", "one_pair", "high"]


def card_to_num(card): #modified for pt 2
    face_to_num = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}
    if card == "A" or card == "K" or card == "Q" or card == "J" or card == "T":
        return face_to_num[card]
    else:
        return int(card)


def get_hand_type(hand):
    qualify_5, qualify_4, qualify_fh, qualify_3, qualify_2x2, qualify_2 = False, False, False, False, False, False
    for c in hand:
        if c != "J":
            if hand.count(c) + hand.count("J") == 5:
                qualify_5 = True
            elif hand.count(c) + hand.count("J") == 4:
                qualify_4 = True
            elif hand.count(c) + hand.count("J") == 3 and get_hand_type(hand.replace(c, "").replace("J", "")) == "one_pair":
                qualify_fh = True
            elif hand.count(c) + hand.count("J") == 3 and get_hand_type(hand.replace(c, "")) != "four_kind":
                qualify_3 = True
            elif hand.count(c) + hand.count("J") == 2 and get_hand_type(hand.replace(c, "").replace("J", "")) == "one_pair":
                qualify_2x2 = True
            elif hand.count(c) + hand.count("J") == 2:
                qualify_2 = True
    if hand == "JJJJJ":
        return "five_kind"
    elif qualify_5:
        return "five_kind"
    elif qualify_4:
        return "four_kind"
    elif qualify_fh:
        return "full_house"
    elif qualify_3:
        return "three_kind"
    elif qualify_2x2:
        return "two_pair"
    elif qualify_2:
        return "one_pair"
    else:
        return "high"


def puzzle1():
    for i in range(len(hands)):
        print(hands[i] + ": " + get_hand_type(hands[i]))
        card_type_inds[get_hand_type(hands[i])].append([i, bids[i]])

    #sort dicts
    for card_type in card_type_names:
        for j in range(len(card_type_inds[card_type]) - 1):
            for k in range(j + 1, len(card_type_inds[card_type])):
                hand1 = hands[card_type_inds[card_type][j][0]]
                hand2 = hands[card_type_inds[card_type][k][0]]
                for c in range(len(hand1)):
                    if card_to_num(hand1[c]) > card_to_num(hand2[c]):
                        temp_ind = card_type_inds[card_type][j]
                        card_type_inds[card_type][j] = card_type_inds[card_type][k]
                        card_type_inds[card_type][k] = temp_ind
                        break
                    elif card_to_num(hand1[c]) == card_to_num(hand2[c]):
                        continue
                    elif card_to_num(hand1[c]) < card_to_num(hand2[c]):
                        break

    winnings = 0
    curr_rank = 1
    for card_type in card_type_names[::-1]:
        for i in range(len(card_type_inds[card_type])):
            winnings += curr_rank * int(card_type_inds[card_type][i][1])
            curr_rank += 1

    print(card_type_inds)
    for ct in card_type_names:
        for cind in card_type_inds[ct]:
            print(hands[cind[0]])
    print(winnings)


puzzle1()