import random

# Words used in the game
WORDS = [
    "python",
    "computer",
    "science",
    "programming",
    "database",
    "developer",
    "variable",
    "function",
    "algorithm",
    "software"
]

MAX_ATTEMPTS = 6

# Hangman drawings: index represents incorrect guesses
HANGMAN_STAGES = [
    """
     +---+
     |   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]


def display_word(secret_word, guessed_letters):
    """Show guessed letters and hide the remaining letters."""
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


def get_letter():
    """Read and validate one English letter."""
    guess = input("Enter a letter: ").strip().lower()

    if len(guess) != 1 or not ("a" <= guess <= "z"):
        print("Invalid input! Enter one English letter.")
        return None

    return guess


def play_game():
    """Run one complete Hangman game."""
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = set()

    print("\n================================")
    print("      HANGMAN WORD GAME")
    print("================================")
    print(f"You have {MAX_ATTEMPTS} incorrect guesses available.")

    while len(wrong_guesses) < MAX_ATTEMPTS:
        mistakes = len(wrong_guesses)

        print(HANGMAN_STAGES[mistakes])
        print("Word:", display_word(secret_word, guessed_letters))
        print("Guessed letters:", " ".join(sorted(guessed_letters)) or "None")
        print("Attempts remaining:", MAX_ATTEMPTS - mistakes)

        guess = get_letter()

        if guess is None:
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")

            if all(letter in guessed_letters for letter in secret_word):
                print("\nCongratulations! You won!")
                print("The word was:", secret_word)
                return
        else:
            wrong_guesses.add(guess)
            print("Incorrect guess!")

    # The player has used all six incorrect guesses
    print(HANGMAN_STAGES[MAX_ATTEMPTS])
    print("\nGame over! You ran out of attempts.")
    print("The correct word was:", secret_word)


def main():
    """Start the game and offer replay."""
    while True:
        play_game()

        answer = input("\nWould you like to play again? (y/n): ").strip().lower()

        if answer != "y":
            print("Thank you for playing Hangman!")
            break


if __name__ == "__main__":
    main()