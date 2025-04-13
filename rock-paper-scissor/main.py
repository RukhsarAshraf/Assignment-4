import random

print("Hello from Rock, Paper, Scissor!")
print("-"*40)
print("You vs The Computer, Let's play!")
print("="*40)

while True:
    user = input("Choose one between them (Rock, Paper, Scissor): ").strip().lower()
    print("-"*40)
    if user not in ["rock", "paper", "scissor"]:
        print("Invalid input, please try again.")

    computer =  random.choice(["rock", "paper", "scissor"])
    print(f"Your choice: {user}")
    print(f"Computer choice: {computer}")
    print("Let's see who wins!")
    print("="*40)

    # Check for a tie, win, or lose
    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissor") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissor" and computer == "paper"):
        print("You win!")
    else:
        print("Computer wins, You lose!")
    print("="*40)

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("-"*40)
        print("As You Wish! Thanks for playing.")
        break

print("Game Over!")
print("="*40)