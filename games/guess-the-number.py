import random
import time

print("\nI'm thinking about a number between 1 and 100. You have 10 attempts.\n")

playing = True
while playing:

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    game_over = False

    while attempts < max_attempts and not game_over:

        try:
            guess = int(
                input(f"Attempt {attempts+1}/{max_attempts}. Enter your guess: ").strip())

        except ValueError:
            print("That's not a valid number. Try again!")
            continue

        attempts += 1

        if guess == secret_number:
            print("You guessed the number! Congrants!")
            game_over = True

        elif guess < secret_number:
            print("Too low. Try a higher number!")
            print(f"You have {max_attempts-attempts} attempts left!")

        elif guess > secret_number:
            print("Too high. Try a lower number!")
            print(f"You have {max_attempts-attempts} attempts left!")

        if attempts == max_attempts and not game_over:
            print(
                f"You tried 10 times. The secret number was {secret_number}!")
            game_over = True

    if not input("Do you want to play a new round? (y/n) ").lower().strip().startswith("y"):
        print("Okay, byeeee!")
        playing = False

    else:
        print("New round loading...")
        time.sleep(2)
