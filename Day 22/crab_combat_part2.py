import re
import copy


def parse(input):
    match = re.search("Player 1:\n(?P<Player1>.*)\nPlayer 2:\n(?P<Player2>.*)", input, flags=re.DOTALL)
    player_1_cards = [int(x) for x in match.group("Player1").splitlines()]
    player_2_cards = [int(x) for x in match.group("Player2").splitlines()]
    return player_1_cards, player_2_cards


def play_round(player_1_cache, player_2_cache, player_1_cards, player_2_cards):
    if str(player_1_cards) in player_1_cache or str(player_2_cards) in player_2_cache:
        # Instant win for player 1
        return True

    player_1_cache[str(player_1_cards)] = True
    player_2_cache[str(player_2_cards)] = True

    card_1 = player_1_cards.pop(0)
    card_2 = player_2_cards.pop(0)

    if len(player_1_cards) >= card_1 and len(player_2_cards) >= card_2:
        # Play a subgame
        deck_1 = copy.deepcopy(player_1_cards)[:card_1]
        deck_2 = copy.deepcopy(player_2_cards)[:card_2]
        player_1_score, player_2_score = play_game(deck_1, deck_2)
        if player_1_score > 0:
            player_1_cards.append(card_1)
            player_1_cards.append(card_2)
        else:
            player_2_cards.append(card_2)
            player_2_cards.append(card_1)

    else:
        if card_1 > card_2:
            player_1_cards.append(card_1)
            player_1_cards.append(card_2)
        else:
            player_2_cards.append(card_2)
            player_2_cards.append(card_1)

    return False


def play_game(player_1_cards, player_2_cards):
    player_1_cache = {}
    player_2_cache = {}
    done = False
    while (len(player_1_cards) > 0 and len(player_2_cards) > 0) and not done:
        done = play_round(player_1_cache, player_2_cache, player_1_cards, player_2_cards)
    if done:
        print("Player 1 had an instant win")
        return 1, 0
    else:
        return determine_winner(player_1_cards, player_2_cards)


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
        return winner_score, 0
    else:
        winner_score = score(player_2_cards)
        return 0, winner_score


def determine_final_winner(player_1_score, player_2_score):
    if player_1_score != 0:
        print(f"The winner is Player 1 with a score of {player_1_score}")
    else:
        print(f"The winner is Player 2 with a score of {player_2_score}")


with open("Day 22/input.txt", "r") as f:
    input = f.read()

player_1_cards, player_2_cards = parse(input)
score_1, score_2 = play_game(player_1_cards, player_2_cards)
determine_final_winner(score_1, score_2)
