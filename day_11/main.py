from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

is_play_game = input("Do you want to play blackjack? (y/n) ")

def game_over(player_cards, computer_cards):
    if sum(player_cards) == 21:
        print("You win with blackjack!")
    elif sum(computer_cards) == 21:
        print("Computer wins with blackjack!")
    elif sum(player_cards) > 21:
        print("Computer wins!")
    elif sum(computer_cards) > 21:
        print("You win!")
    elif sum(player_cards) < sum(computer_cards):
        print("Computer wins!")
    elif sum(player_cards) > sum(computer_cards):
        print("You win!")
    else:
        print("Draw!")

    print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

def play_blackjack():
    print(logo)
    player_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]

    print(f"Your cards are {player_cards}, total score is {sum(player_cards)}")
    print(f"Computer first card is {computer_cards[0]}")

    if sum(player_cards) == 21 or sum(computer_cards) == 21:
        game_over(player_cards, computer_cards)
    else:
        get_more_cars = input("Do you want to get more cards? (y/n) ")
        while get_more_cars == "y":
                player_cards.append(random.choice(cards))
                if sum(player_cards) > 20:
                    if sum(player_cards) == 21:
                        get_more_cars = "n"
                    elif sum(player_cards) > 21 and 11 in player_cards:
                        player_cards.remove(11)
                        player_cards.append(1)
                    else:
                        get_more_cars = "n"
                print(f"Your cards are {player_cards}, total score is {sum(player_cards)}")
                if sum(player_cards) < 21:
                    get_more_cars = input("Do you want to get more cards? (y/n) ")
        print(f"Computer second card is {computer_cards[1]}")
        if sum(player_cards) < 22:
            while sum(computer_cards) < 17:
                computer_next_card = random.choice(cards)
                if (sum(computer_cards) + computer_next_card) > 21:
                    if computer_next_card == 11:
                        computer_next_card = 1
                    elif 11 in computer_cards:
                        computer_cards.remove(11)
                        computer_cards.append(1)
                computer_cards.append(computer_next_card)
                print(f"Computer get {computer_next_card} card, computer score is {sum(computer_cards)}")
        game_over(player_cards, computer_cards)

while is_play_game == 'y':
    play_blackjack()
    is_play_game = input("Do you want to play blackjack? (y/n) ")

