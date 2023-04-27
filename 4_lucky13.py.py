import random 

def play_lucky13():
    print("Welcome to Lucky13!")
    
    r_number = random.randint(1, 13) # using random.randint to generate random integers between 1 and 13
    
    attempt = 0
    
    while True:
        attempt += 1
        user_guess = input("Make a guess from 1-13: ")
        
        if user_guess.isdigit() and 1 <= int(user_guess) <= 13: # checking if the user input is a digit between 1 and 13
            user_guess = int(user_guess)
        else:
            print("Invalid input. Please try again.")
            continue
        
        if user_guess == r_number:
            print("Congratulations! You got it!")
            break 
        else:
            if user_guess > r_number:
                print("Too high.")
            else:
                print("Too low.")
    
    print("You got it in", attempt, "attempts!")

play_lucky13()
