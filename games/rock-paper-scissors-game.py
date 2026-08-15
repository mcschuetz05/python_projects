import random

print("Let's play ROCK, PAPER, SCISSORS!")

possibilities = ["rock", "paper", "scissor"]

wins_against = {
    "rock": "scissor",
    "paper": "rock",
    "scissor": "paper"
}

while True:
    won = 0
    lost = 0

    while won < 3 and lost < 3:
        choice = input("Rock, Paper or Scissor?: ").lower()
        fate = random.choice(possibilities)

        if choice not in possibilities:
            print("Please choose one of the options.")
            continue

        if choice == fate:
            print("Arg, it's a tie... Try again!")

        elif wins_against[choice] == fate:
            print(f"I played {fate} - you won!")
            won += 1

        else:
            print(f"I played {fate} - you lost!")
            lost += 1

        print(f"Score: {won} - {lost}")

    print("Nice game!")

    again = input("Do you want to play again? ").lower()

    if not again.startswith("yes"):
        print("Okay, byeeeeee!")
        break

"""
# old version

import random
print("Let's play ROCK, PAPER, SCISSORS!")

possibilities = ["rock", "paper", "scissor"]

won = 0
lost = 0

while True:
    while won < 3 and lost < 3:
        choice = str(input("Rock, Paper or Scissor?: ")).lower()
        fate = random.choice(possibilities)

        if choice in possibilities:
            if choice == fate:
                print("Arg, it's a tie... Try again!")

            elif choice == "rock" and fate == "paper":
                print(f"I played {fate} - you lost!")
                lost += 1

            elif choice == "rock" and fate == "scissor":
                print(f"I played {fate} - you won!")
                won += 1

            elif choice == "paper" and fate == "scissor":
                print(f"I played {fate} - you lost!")
                lost += 1

            elif choice == "paper" and fate == "rock":
                print(f"I played {fate} - you won!")
                won += 1

            elif choice == "scissor" and fate == "rock":
                print(f"I played {fate} - you lost!")
                lost += 1

            elif choice == "scissor" and fate == "paper":
                print(f"I played {fate} - you won!")
                won += 1

        else:
            print("Please choose one of the options.")
            continue

    print("Nice game!")

    again = str(input("Do you want to play again? ")).lower()

    if again.startswith("yes"):
        continue

    elif again == "no":
        print("Okay, byeeeeee!")
        break

    else:
        print("I don't understand.")
"""
