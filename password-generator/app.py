import random
import string  
import re

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # include all alphabets upper and lower case

    if use_digits:
        characters += string.digits  # provide numbers 0 to 9

    if use_special:
        characters += string.punctuation  # Add special characters

    return ''.join(random.choice(characters) for _ in range(length))

def check_password_strength(password):
    if len(password) < 6:
        return "❌ Weak Password - Too short (Minimum 6 characters required)",
    elif not re.search(r"[A-Z]", password):
        return "⚠️ Weak Password - Add at least one uppercase letter",
    elif not re.search(r"\d", password):
        return "⚠️ Weak Password - Add at least one number",
    elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "⚠️ Medium Password - Add a special character (!@#$%^&*)",
    else:
        return "✅ Strong Password! 🔥",

def main():
    print("🔐 PASGEN & CHECKER 🔐")
    print("-----------------------")
    
    while True:
        print("\nSelect an option:")
        print("1. Check Password Strength")
        print("2. Generate Secure Password")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            password = input("💡 Enter your password for strength checking: ")
            message = check_password_strength(password)
            print(f"\nResult: {message}")

        elif choice == '2':
            try:
                length = int(input("📏 Select Your Password Length (6-20): "))
                if length < 6 or length > 20:
                    print("❗ Please enter a number between 6 and 20.")
                    continue
            except ValueError:
                print("❗ Invalid number. Please enter digits only.")
                continue

            use_digits = input("🔢 Include Digits? (y/n): ").strip().lower() == 'y'
            use_special = input("🔣 Include Special Characters? (y/n): ").strip().lower() == 'y'

            password = generate_password(length, use_digits, use_special)
            print(f"\n🔑 Here is your strong password: {password} 🔐")

        elif choice == '3':
            print("\n🚀 Note: This tool is built by Rukhsar Ashraf for education purpose only.")
            print("👋 Exiting... Stay safe!")
            break

        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
