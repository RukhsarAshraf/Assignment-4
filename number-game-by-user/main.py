import random

print("Welcome to the User Guess the Number Game!")
print("="*40)
print("In this game, You'll think a number between 1 and 100, and I'll try to guess it.")
print("="*40)

low=1
high=100
attempts=0

while True:
    guess = random.randint(low, high)
    attempts += 1

    user_input = input(f"It is {guess}? (H/L/C) :").strip().upper()

    if user_input == "H":
        high = guess-1
        print("Too High?,   Let me try again...")
    elif user_input == "L":
        high = guess+1
        print("Too Low?,   Let me try again...")
    elif user_input == "C":
        print(f"Yay! I guessed your number {guess}")
        break
    else:
        print("Invalid input. Please enter 'H', 'L', or 'C'.")