from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

is_play_game = input("Do you want to play blackjack? (y/n) ")

def game_over(player_cards, computer_cards):
    if sum(player_cards) == 21:
        print(f"You win with blackjack! Your final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    elif sum(computer_cards) == 21:
        print(f"Computer wins with blackjack!! Your final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    elif sum(player_cards) > 21:
        print(f"Computer wins! Your final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    elif sum(player_cards) < sum(computer_cards):
        print(f"Computer wins! Your final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    else:
        print(f"You win! Your final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

def play_blackjack():
    print(logo)
    player_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]

    if sum(player_cards) == 21 or sum(computer_cards) == 21:
        game_over(player_cards, computer_cards)

    print(f"Your cards are {player_cards}, total score is {sum(player_cards)}")
    print(f"Computer first card is {computer_cards[0]}")

    get_more_cars = input("Do you want to get more cards? (y/n) ")
    while get_more_cars == "y":
            player_cards.append(random.choice(cards))
            print(f"Your cards are {player_cards}, total score is {sum(player_cards)}")
            if sum(player_cards) > 20:
                get_more_cars = "n"
            else:
                get_more_cars = input("Do you want to get more cards? (y/n) ")

    print(f"Computer second card is {computer_cards[1]}")
    game_over(player_cards, computer_cards)

while is_play_game == 'y':
    play_blackjack()
    is_play_game = input("Do you want to play blackjack? (y/n)")

