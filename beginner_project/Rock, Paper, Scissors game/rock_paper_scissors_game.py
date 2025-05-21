import random

while True:
    choices = ('r','p','s')
    emojis = {'r':'🪨','p':'📃','s':'✂️'}
    user_choice = input("Rock, Paper, Scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid choice!")
        continue

    computer_choice = random.choice(choices)
    print(f"Your choice is {emojis[user_choice]}")
    print(f"Computer choice is {emojis[computer_choice]}")
    if (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or
        (user_choice == 'p' and computer_choice == 'r')
    ):
        print("You win")
    else:
        print("You lose")

    should_play = input("Continue(y/n)")
    if should_play == 'n':
        break