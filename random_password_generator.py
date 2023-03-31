# ask user if they want to generate a password
# if yes, request passwprd length
# generate the password
# print the program
# if initial reponse is no, exit no

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

# function that generates password
# make sure the characters are shuffled
def generate_password():
    password_length = int(input("How long would you like the password to be ?"))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))
    
    random.shuffle(password)

    password = "".join(password)
    print(password) 

option = input("Do you want to generate a password? (Yes/No): ").lower()

if option == "yes":
    generate_password()
elif option == "no":
    print("Program ended")
    quit()
else:
    print("Invalid Input please print Yes or No")