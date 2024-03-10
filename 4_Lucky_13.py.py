import random

def play_lucky13():
    """
    This function runs the Lucky13 game where the user has to guess a random number between 1 and 13.
    """
    print("Welcome to Lucky13!")

    # Generate a random number between 1 and 13
    random_number = random.randint(1, 13)
    attempts = 0
    
    while True:
        attempts += 1
        user_guess = input("Make a guess from 1-13: ")

        # Check if the user input is a digit between 1 and 13
        if user_guess.isdigit() and 1 <= (user_guess := int(user_guess)) <= 13:
            pass
        else:
            print("Invalid input. Please enter a digit between 1 and 13.")
            continue

        # Check if the user's guess matches the random number
        if user_guess == random_number:
            print("Congratulations! You got it!")
            break 
        else:
            if user_guess > random_number:
                print("Too high.")
            else:
                print("Too low.")
    
    print("You got it in", attempts, "attempts!")

# Call the function to play the game
play_lucky13()
