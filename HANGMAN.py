import random

def hangman():
    words = ["python", "coding", "hangman", "game", "funny"]
    word = random.choice(words).upper()
    guessed_letters = set()
    correct_letters = set(word)
    tries = 6

    print("\n" + "="*40)
    print("🎮 WELCOME TO HANGMAN 🎮".center(40))
    print("="*40)
    print("Guess the word, one letter at a time.")
    print(f"You have {tries} chances to guess it!\n")

    while tries > 0 and correct_letters:
        display_word = [letter if letter in guessed_letters else "_" for letter in word]
        print("Word:", " ".join(display_word))
        print(f"❓ Tries Left: {tries} | ✅ Correct Guesses: {' '.join(sorted(guessed_letters & correct_letters)) or '-'}")
        guess = input("👉 Enter a letter: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a SINGLE valid letter.\n")
            continue
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter. Try another one.\n")
            continue

        guessed_letters.add(guess)

        if guess in correct_letters:
            print("🎉 Nice! Correct guess.\n")
            correct_letters.remove(guess)
        else:
            print("❌ Oops! Wrong guess.\n")
            tries -= 1

    print("="*40)
    if not correct_letters:
        print(f"🎉 CONGRATULATIONS! You guessed the word: {word}\n")
    else:
        print(f"💀 GAME OVER! The word was: {word}\n")
    print("="*40)

if __name__ == "__main__":
    hangman()



















