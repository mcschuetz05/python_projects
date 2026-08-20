import time

print("\nCount down from your chosen seconds!")

while True:
    try:
        seconds = int(input("\nEnter seconds to countdown from: "))
    except ValueError:
        print("Please enter a positiv number.")
        continue

    print(f"Starting countdown from {seconds} seconds!")

    if seconds <= 0:
        print("Please enter a positive number!")
        continue

    for remaining in range(seconds, 0, -1):
        print(f"{remaining} seconds remaining", end="")
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
            time.sleep(0.3)
        print()
        seconds -= 1

    print("Countdown complete!")

    again = input(
        "Do you want to start another countdown? (y/n) ").lower().strip()
    if not again.startswith("y"):
        print("Ok, bye!")
        break
