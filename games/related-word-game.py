import time
import random

print("\nLet's play a related-word game!")

word_relates_to = {
    "chemistry": ["molecule", "molecules", "laboratory", "lab", "explosion", "substance"],
    "physics": ["force", "Newton", "Einstein", "experiments"],
    "biology": ["plants", "animals", "anatomy", "photosynthesis", "chlorophyll", "live", "genetics"],
    "university": ["love", "hate", "curiosity", "exams", "stress", "learning", "studying"]
}

playing = True
while playing:

    possible_points = 5
    points = 0

    print("\nYour prompt word in ", end="", flush=True)
    for remaining in range(3, 0, -1):
        print(f"\rYour prompt word in {remaining}", end="", flush=True)
        time.sleep(1)
    print()

    prompt_word = random.choice(list(word_relates_to))
    print(f"\nPrompt word: {prompt_word}")

    while True:

        start_time = time.perf_counter()

        guessed_word = input(
            "\nQuick! Type a word related to this prompt!\n> ").lower().strip()

        end_time = time.perf_counter() - start_time

        score = max(1, possible_points - round(end_time))

        if guessed_word not in word_relates_to[prompt_word]:
            print(
                "Arg, I'm not associating this word with my prompt - sorry.\nTry again!")
            continue

        elif guessed_word in word_relates_to[prompt_word]:
            points += score
            print(f"response time: {end_time}")
            print(
                f"Good association! +{points} (answerd in {round(end_time, 1)})")
            print(f"Score: {score}/{possible_points} possible points")
            break

    if not input("\nPlay again? (yes/no) ").lower().strip().startswith("yes"):
        print("Okay, thanks for playing! Byeeeeeeee!")
        playing = False
