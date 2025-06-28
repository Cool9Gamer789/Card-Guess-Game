import random
import sys

card_list = ["jack", "queen", "king", "ace"]

game_card = random.choice(card_list)

while True:
    guess = input("What's the card? ").rstrip().lower()
    
    if guess not in card_list:
        sys.exit("Invalid card")

    if guess == game_card:
        print(f"Correct. The card was a {game_card}.")
        break
    else:
        print("Nope! Try again.")
        continue
