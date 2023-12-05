import random 

def play_lucky13():
    print("Welcome to Lucky13!")

    random_number = random.randint(1, 13)
    attempts = 0
    
    while True:
        attempts += 1
        user_guess = input("Make a guess from 1-13: ")

        # Checking if the user input is a digit between 1 and 13
        if user_guess.isdigit() and 1 <= (user_guess := int(user_guess)) <= 13:
            pass
        else:
            print("Invalid input. Please enter a digit between 1 and 13.")
            continue

        if user_guess == random_number:
            print("Congratulations! You got it!")
            break 
        else:
            if user_guess > random_number:
                print("Too high.")
            else:
                print("Too low.")
    
    print("You got it in", attempts, "attempts!")

play_lucky13()
