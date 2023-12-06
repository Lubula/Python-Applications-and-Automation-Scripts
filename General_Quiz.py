# Welcome the user to the game
print("Welcome to my mini game! Let's play Quiz 1: Guessing Game")
score = 0

# Prompt the user whether they want to play or not using input() function
user_prompt = input("Do you want to play? (Enter 'yes' to play or any other key to quit) ").lower()

# Check if the user wants to play or not
if user_prompt == "yes":
    print("Okay! Let's play :)")
else:
    quit()

# Ask the first question and store the user's answer
ans_1 = input("What is the nearest star to planet Earth? ").lower()

# Check if the user's answer is correct and give appropriate feedback
if ans_1 == "sun":
    print("You're brilliant! Correct!")
    score += 1
else:
    print("Oh no, that's wrong. Stop looking down at your smartphone and look up at the sky to see the sun :)")
    
# Ask the second question and store the user's answer
ans_2 = input("How many colors are in a rainbow? ")
    
# Check if the user's answer is correct and give appropriate feedback
if ans_2 == "7":
    print("You're brilliant! Correct!")
    score += 1
else:
    print("Oh no, that's wrong. Look at the rainbow more and count a little more :)")
    
# Ask the third question and store the user's answer
ans_3 = input("In what direction does the sunrise? ").lower()

# Check if the user's answer is correct and give appropriate feedback
if ans_3 =="east":
    print("You're brilliant! Correct!")
    score += 1
else:
    print("Oh no, that's wrong. Maybe you're still sleepy in the morning to know your directions :( ")

# Ask the fourth question and store the user's answer
ans_4 = input("How many weeks are in one year? ")
    
# Check if the user's answer is correct and give appropriate feedback
if ans_4 == "52":
    print("You're brilliant! Correct!")
    score += 1
else:
    print("Oh no, that's wrong. Time to find the calendar :( ")

# Calculate the total score and give feedback to the user
print("Your score: ", score, " out of 4.")
