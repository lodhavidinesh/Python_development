import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
emojis = {ROCK:'🪨',PAPER:'📃',SCISSORS:'✂️'}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice =input("Rock, Paper, Scissors? (r/p/s): ").lower()
        if user_choice not in choices:
            print("Invalid choice!")
        else:
            return user_choice
def display_choices(user_choice,computer_choice):
    print(f"Your choice is {emojis[user_choice]}")
    print(f"Computer choice is {emojis[computer_choice]}")
def determine_winner(user_choice,computer_choice):
    if (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)
    ):
        print("You win")
    else:
        print("You lose")

def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)
        display_choices(user_choice,computer_choice)
        determine_winner(user_choice,computer_choice)

        should_play = input("Continue(y/n)")
        if should_play == 'n':
            break
play_game()