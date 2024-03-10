import string
import random

# Using string.printable for the character pool
characters = list(string.printable)

def generate_password():
    """
    This function generates a random password based on user input for the password length.
    """
    while True:
        try:
            # Get the desired password length from the user
            password_length = int(input("How long would you like the password to be? "))
            if password_length <= 0:
                print("Please enter a positive integer for password length.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Shuffle the character pool and select characters for the password
    random.shuffle(characters)
    password = random.choices(characters, k=password_length)

    # Print the generated password
    print("Generated Password:", "".join(password))

def main():
    """
    Main function to interact with the user and generate passwords.
    """
    option = input("Do you want to generate a password? (Yes/No): ").lower()

    if option == "yes":
        generate_password()
    elif option == "no":
        print("Program ended.")
    else:
        print("Invalid input. Please enter Yes or No.")

if __name__ == "__main__":
    main()
