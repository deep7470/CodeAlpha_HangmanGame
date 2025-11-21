import random

# A list of words for the game
WORDS = ["python", "program", "hangman", "developer", "logic", "coding", "algorithm", "variable"]


def hangman_simple():
    """Main function to run the simple Hangman game."""
    # Choose a word and convert to uppercase for easier processing
    word_to_guess = random.choice(WORDS).upper()
    guessed_letters = set()
    max_attempts = 6
    attempts_left = max_attempts

    # Initialize the display word with underscores
    display_word_list = ["_"] * len(word_to_guess)

    print("--- 🧠 Welcome to Hangman! ---")
    print("Guess the word:")
    print(" ".join(display_word_list))
    print("-" * 30)

    while attempts_left > 0:
        # Check for a win
        if "".join(display_word_list) == word_to_guess:
            print(f"\n🎉 CONGRATULATIONS! You guessed the word: **{word_to_guess}**")
            return

        print(f"\nAttempts remaining: **{attempts_left}**")
        # Display used letters in a sorted, easy-to-read format
        print(f"Used letters: **{', '.join(sorted(list(guessed_letters)))}**")

        # Take input and convert it to uppercase
        guess = input("Enter a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter only one alphabet.")
            continue

        if guess in guessed_letters:
            print(f"⚠️ You already used the letter '{guess}'.")
            continue

        # Add the guess to the used set
        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("✅ Good guess!")
            # Update the display word
            for i, char in enumerate(word_to_guess):
                if char == guess:
                    display_word_list[i] = guess
        else:
            attempts_left -= 1
            print(f"🔥 Wrong guess! Remaining attempts: {attempts_left}")

        # Display the current state of the word
        print("Current word: " + " ".join(display_word_list))
        print("-" * 30)

    # Game Over (attempts_left is 0)
    print(f"\n☠️ GAME OVER! You ran out of attempts.")
    print(f"The correct word was: **{word_to_guess}**")


if __name__ == "__main__":
    hangman_simple()