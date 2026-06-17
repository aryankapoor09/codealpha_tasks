import random

words = ["python", "tiger", "house", "plant", "guitar"]
word = random.choice(words)
masked_word = ["_"] * len(word)
guessed_letters = []
tries = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

while tries > 0 and "_" in masked_word:
    print("\nWord:", " ".join(masked_word))
    print("Incorrect guesses left:", tries)
    guess = input("Enter a letter: ").strip().lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter exactly one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                masked_word[i] = guess
    else:
        print("Wrong guess!")
        tries -= 1

if "_" not in masked_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
