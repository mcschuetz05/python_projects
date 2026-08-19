import random
from pathlib import Path

file_path = Path(__file__).parent / "studies.txt"

with open(file_path, "r") as file:
    word = [word.strip() for word in file]

print("\nUnscramble the letters to find the word!\n")

while True:
    chosen_word = random.choice(word)
    letters = list(chosen_word)
    random.shuffle(letters)
    scrambled_word = "".join(letters)
    print(f"Scrambled word: {scrambled_word}")

    guess = input("What's the word? ").strip()

    if chosen_word.lower() == guess.lower():
        print("Correct! You win!")
    else:
        print(f"Arg, wrong! The word was {chosen_word}!")

    if not input("Try again? (y/n) ").lower().strip().startswith("y"):
        print("Ok, bye!")
        break
