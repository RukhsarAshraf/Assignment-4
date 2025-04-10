import random

print("Welcome to My Guess the Number Game!")
print("-"*40)

print("Hello! I've choose the number between 1 to 100 \n")
secret_number=random.randint(1,100)
attempts=0

while True:
    try:
        user_number=int(input("Enter your guess number :"))
        attempts+=1
        print("-"*40)
        if (user_number < 1 or user_number > 100):
            print("Please enter a number between 1 and 100.")
        elif (user_number < secret_number):
            print("Your guess is too low!")
        elif (user_number > secret_number):
            print("Your guess is too high!")
        else:
            print(f"Congratulations! You've the guess the correct number, that number was {secret_number}")
            print(f"You've guessed it in {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 100.")