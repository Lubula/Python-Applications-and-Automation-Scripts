import random

while True:
    user_wins = 0
    computer_wins = 0
    options = ["rock", "paper", "scissors"]

    while True:
        user_input = input("Type Rock/Paper/Scissors or Q (to quit): ").lower()

        if user_input == "q":
            break

        if user_input not in options:
            continue

        computer_pick = random.choice(options)
        print(f"Computer picked {computer_pick}.")

        if user_input == computer_pick:
            print("Both players picked the same. Play again!")
        elif (user_input == "rock" and computer_pick == "scissors") or \
             (user_input == "paper" and computer_pick == "rock") or \
             (user_input == "scissors" and computer_pick == "paper"):
            print("You win!")
            user_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1

    print(f"You won {user_wins} times.")
    print(f"The computer won {computer_wins} times.")
    print("Goodbye!")
    break
