import random

COLORS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
FIGURES = [x for x in range(11, 15)] # 11 walet, 12 dama, 13 król, 14 AS
SPOTS = [x for x in range(2, 11)]

FIGURES_DECK = [{'color': x, 'rank': y} for x in COLORS for y in FIGURES]
SPOTS_DECK = [{'color': x, 'rank': y} for x in COLORS for y in SPOTS]


def is_color(hand):
    colors = set()
    for s in hand:
        colors.add(s['color'])
    return len(colors) == 1


def is_two_pairs(hand):
    ranks = {}
    for card in hand:
        if card['rank'] in ranks:
            ranks[card['rank']] = ranks[card['rank']] + 1
        else:
            ranks[card['rank']] = 1
    num_of_pairs = 0
    for k, v in ranks.items():
        if v == 2:
            num_of_pairs += 1
    return num_of_pairs == 2


def is_one_pair(hand):
    ranks = {}
    for card in hand:
        if card['rank'] in ranks:
            ranks[card['rank']] = ranks[card['rank']] + 1
        else:
            ranks[card['rank']] = 1
    num_of_pairs = 0
    for k, v in ranks.items():
        if v == 2:
            num_of_pairs += 1
    return num_of_pairs == 1


def is_three_of_kind(hand):
    ranks = {}
    for card in hand:
        if card['rank'] in ranks:
            ranks[card['rank']] = ranks[card['rank']] + 1
        else:
            ranks[card['rank']] = 1

    for k, v in ranks.items():
        if v == 3:
            return True
    return False


def is_full(hand):
    return is_three_of_kind(hand) and is_one_pair(hand)


def is_straight(hand):
    ranks = []
    for card in hand:
        rk = card['rank']
        ranks.append(rk)

    ranks.sort()
    prev = ranks[0]
    for i in range(1, len(ranks)):
        if ranks[i] != prev + 1:
            return False
        prev = ranks[i]
    return True


def is_poker(hand):
    return is_straight(hand) and is_color(hand)


def is_four_of_kind(hand):
    ranks = {}
    for card in hand:
        if card['rank'] in ranks:
            ranks[card['rank']] = ranks[card['rank']] + 1
        else:
            ranks[card['rank']] = 1

    for k, v in ranks.items():
        if v == 4:
            return True
    return False


def hand_value(hand):
    """
        0 - wysoka karta
        1 - para
        2 - dwie pary
        3 - trójka
        4 - strit
        5 - kolor
        6 - full
        7 - kareta
        8 - poker
        pokera królewskiego nie da się zrobić bo zabraknie 10, w przypadku remisu wygrywa figurant zawsze
    """
    if is_poker(hand):
        return 8
    if is_four_of_kind(hand):
        return 7
    if is_full(hand):
        return 6
    if is_color(hand):
        return 5
    if is_straight(hand):
        return 4
    if is_three_of_kind(hand):
        return 3
    if is_two_pairs(hand):
        return 2
    if is_one_pair(hand):
        return 1
    return 0


def test1():
    fig_wins = 0
    spots_wins = 0
    total = 100000
    for _ in range(0, total):
        fig_deck = random.sample(FIGURES_DECK, 5)
        spots_deck = random.sample(SPOTS_DECK, 5)
        if hand_value(fig_deck) >= hand_value(spots_deck):
            fig_wins += 1
        else:
            spots_wins += 1
    print("\'Uczciwe\' rozdanie")
    print(str((float(fig_wins)/float(total)) * 100.0))


def test2():
    fig_wins = 0
    spots_wins = 0
    total = 100000
    CHEAT_DECK = [{'color': 'Diamonds', 'rank': 6}, {'color': 'Clubs', 'rank': 6}, {'color': 'Clubs', 'rank': 4}, {'color': 'Clubs', 'rank': 6}, {'color': 'Clubs', 'rank': 6}]
    for _ in range(0, total):
        fig_deck = random.sample(FIGURES_DECK, 5)
        spots_deck = random.sample(CHEAT_DECK, 5)
        if hand_value(fig_deck) >= hand_value(spots_deck):
            fig_wins += 1
        else:
            spots_wins += 1
    print("Blotkarz z karetą")
    print(str((float(fig_wins)/float(total)) * 100.0))


def test3():
    fig_wins = 0
    spots_wins = 0
    total = 100000
    CHEAT_DECK = [{'color': 'Clubs', 'rank': 10}, {'color': 'Clubs', 'rank': 9}, {'color': 'Clubs', 'rank': 8}, {'color': 'Clubs', 'rank': 7}, {'color': 'Clubs', 'rank': 6}]
    for _ in range(0, total):
        fig_deck = random.sample(FIGURES_DECK, 5)
        spots_deck = random.sample(CHEAT_DECK, 5)
        if hand_value(fig_deck) >= hand_value(spots_deck):
            fig_wins += 1
        else:
            spots_wins += 1
    print("Blotkarz z pokerem")
    print(str((float(fig_wins)/float(total)) * 100.0))

    
if __name__ == '__main__':
    test1()
    test2()
    test3()