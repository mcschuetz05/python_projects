import random
import time
import os


def clear_screen():
    """Clear the terminal screen"""
    os.system("cls" if os.name == "nt" else "clear")


print("\nMemory Sequence Game")
print("Remember the sequence and type it back!")

print("\nRules:"
      "\n- Watch as numbers appear one by one"
      "\n- After the sequence is shown, tape it back in order"
      "\n- Each round adds one more number to remember"
      "\n  How far can you go?")

start = input("\nPress enter to start... ")

playing = True
while playing:

    rounds = 0
    seq = []

    game_over = False
    while not game_over:

        number = random.randint(1, 9)
        seq.append(number)

        clear_screen()
        print("\nOkay, here's the sequence:")
        time.sleep(0.5)
        clear_screen()
        for number in seq:
            time.sleep(0.5)
            print(number)
            time.sleep(1)
            print()
            clear_screen()

        rounds += 1

        try:
            answer = [int(number) for number in input("\nNow repeat the sequence by typing each number, seperated by spaces:"
                                                      "\n> ").split()]

            if answer == seq:
                print(f"\nCorrect! You remembered all {len(seq)} numbers!")
                continue
            else:
                print(f"\nArg, wrong sequence! You remembered {rounds - 1}.")
                print(
                    f"The correct sequence was: {" ".join(str(number) for number in seq)}")
                break

        except ValueError:
            print("Please enter a number.")
            game_over = True
            continue

    if not input("\nPlay again? (yes/no) ").lower().strip().startswith("yes"):
        print("\nOkay, byeeeee!")
        playing = False
