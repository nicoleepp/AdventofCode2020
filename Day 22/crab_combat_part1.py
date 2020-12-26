import re


def parse(input):
    match = re.search("Player 1:\n(?P<Player1>.*)\nPlayer 2:\n(?P<Player2>.*)", input, flags=re.DOTALL)
    player_1_cards = [int(x) for x in match.group("Player1").splitlines()]
    player_2_cards = [int(x) for x in match.group("Player2").splitlines()]
    return player_1_cards, player_2_cards


def play_round(player_1_cards, player_2_cards):
    card_1 = player_1_cards.pop(0)
    card_2 = player_2_cards.pop(0)
    if card_1 > card_2:
        player_1_cards.append(card_1)
        player_1_cards.append(card_2)
    else:
        player_2_cards.append(card_2)
        player_2_cards.append(card_1)


def play_game(player_1_cards, player_2_cards):
    while len(player_1_cards) > 0 and len(player_2_cards) > 0:
        play_round(player_1_cards, player_2_cards)

    determine_winner(player_1_cards, player_2_cards)


def score(cards):
    multiplier = 1
    curr_score = 0
    for card in reversed(cards):
        curr_score += card * multiplier
        multiplier += 1
    return curr_score


def determine_winner(player_1_cards, player_2_cards):
    if len(player_1_cards) != 0:
        winner_score = score(player_1_cards)
        print(f"The winner is Player 1 with a score of {winner_score}")
    else:
        winner_score = score(player_2_cards)
        print(f"The winner is Player 2 with a score of {winner_score}")



with open("Day 22/input.txt", "r") as f:
    input = f.read()

player_1_cards, player_2_cards = parse(input)
play_game(player_1_cards, player_2_cards)
