import random

# List of words to guess
words = ["apple", "banana", "grape", "orange", "mango"]
secret_word = random.choice(words)
guessed_letters = []
tries = 6

print("Welcome to the Hangman Game!")
print("====================================")
print("Guess the word, one letter at a time.")
print("------------------------------------")

# Function to show current word with blanks and guessed letters.
def display_word():
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

while tries > 0:
    print("\nWord:", display_word())
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter! Try another one.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct guess!")
        if all(letter in guessed_letters for letter in secret_word):
            print(f"\n🎉 Congratulations! You guessed the word '{secret_word}' correctly.")
            break
    else:
        tries -= 1
        print(f"❌ Wrong guess! You have {tries} tries left.")

if tries == 0:
    print(f"\nGame over! The correct word was '{secret_word}'. Better luck next time!")

print("====================================")
print("Thanks for playing!")
