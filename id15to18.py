# encoding: utf-8
"""
身份证15位转18位
"""

wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1]
vi = [1, 0, "X", 9, 8, 7, 6, 5, 4, 3, 2]


def get_verity(eighteen_card):
    """

    :param eighteen_card:
    :return:
    """
    ai = []
    remaining = ""
    if len(eighteen_card) == 18:
        eighteen_card = eighteen_card[0:-1]
    if len(eighteen_card) == 17:
        s = 0
        for i in eighteen_card:
            ai.append(int(i))
        for i in range(17):
            s = s + wi[i] * ai[i]
        remaining = s % 11
    return "X" if remaining == 2 else str(vi[remaining])


def up_to_eighteen(fifteen_card):
    """
    15位转18位
    :param fifteen_card:
    :return:
    """
    eighteen_card = fifteen_card[0:6] + "19" + fifteen_card[6:15]
    return eighteen_card + get_verity(eighteen_card)


def down_to_fifteen(eighteen_card):
    """
    18位转15位
    :param eighteen_card:
    :return:
    """
    return eighteen_card[0:6] + eighteen_card[8:17]


if __name__ == "__main__":
    # 15位转18位
    card_1 = up_to_eighteen("632123820927051")
    print(card_1)
    # 18位转15位
    card_2 = down_to_fifteen("410125199908222000")
    print(card_2)
