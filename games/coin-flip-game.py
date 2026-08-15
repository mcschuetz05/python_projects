import random

print("Guess heads or tails!")

while True:
    guess = str(input("\nEnter your guess: ").lower())

    if guess != "heads" and guess != "tails":
        print("Please enter 'heads' or 'tails'.")
        continue

    coin = ["heads", "tails"]
    flip = random.choice(coin)
    print(f"Coin shows {flip}!")

    if flip == guess:
        print("You guessed correctly! You win!")
    else:
        print("Sorry, wrong guess. Try again!")

    again = str(input("Play again (y/n)? ").lower())

    if again != "y":
        print("Okay, thanks for playing! Byeeeee!")
        break
