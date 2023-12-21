import random

choices = ["rock", "paper", "scissors"]

is_rematch = True

while is_rematch:
    computer_choice = random.choice(choices)
    player_choice = None
    while player_choice not in choices:
        player_choice = input("Rock, paper or scissors? : ").lower()

    print(f"Player choice: {player_choice}")
    print(f"Computer choice: {computer_choice}")

    if computer_choice == player_choice:
        print("It's Tie")
    else:
        if computer_choice == "rock" and player_choice == "paper":
            print("You Lose :(")
        elif computer_choice == "rock" and player_choice == "scissors":
            print("You Win :)")
        elif computer_choice == "paper" and player_choice == "rock":
            print("You Lose :(")
        elif computer_choice == "paper" and player_choice == "scissors":
            print("You Win :)")
        elif computer_choice == "scissors" and player_choice == "paper":
            print("You Lose :(")
        elif computer_choice == "scissors" and player_choice == "rock":
            print("You Win :)")

    is_rematch_input = None
    while True:
        is_rematch_input = input("Want to play again? (y/n): ").lower()
        if is_rematch_input == "y" or is_rematch_input == "n":
            break
    if is_rematch_input == "y":
        pass
    else:
        is_rematch = False
        print("Thanks for playing...")
