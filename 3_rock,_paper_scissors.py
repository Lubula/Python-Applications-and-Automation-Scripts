# import the necessary module
import random

# initialize variables for user and computer wins
user_wins = 0
computer_wins = 0

# create a list of valid options
options = ["rock", "paper", "scissors"]

# loop until the user quits the game
while True:
    # get user input and convert to lowercase
    user_input = input("Type Rock/Paper/Scissors or Q (to quit): ").lower()

    # check if the user wants to quit
    if user_input == "q":
        break

    # check if the user input is valid
    if user_input not in options:
        continue

    # generate a random number to pick a play for the computer
    computer_pick = random.choice(options)
    print("Computer picked", computer_pick + ".")

    # determine the winner of the round based on the user and computer picks
    if user_input == computer_pick:
        print("Both players picked the same. Play again!")
    elif user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1
    else:
        print("Computer wins!")
        computer_wins += 1

# print the final scores and exit the game
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
