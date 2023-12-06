import string
import random

# Using string.printable for the character pool
characters = list(string.printable)

def generate_password():
    while True:
        try:
            password_length = int(input("How long would you like the password to be? "))
            if password_length <= 0:
                print("Please enter a positive integer for password length.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    random.shuffle(characters)
    password = random.choices(characters, k=password_length)

    print("Generated Password:", "".join(password))

option = input("Do you want to generate a password? (Yes/No): ").lower()

if option == "yes":
    generate_password()
elif option == "no":
    print("Program ended.")
else:
    print("Invalid input. Please enter Yes or No.")
