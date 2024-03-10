def play_guessing_game():
    """
    This function runs a mini quiz game where the user is asked four questions.
    For each correct answer, the user earns one point.
    """
    print("Welcome to my mini game! Let's play Quiz 1: Guessing Game")
    score = 0

    # Prompt the user whether they want to play or not
    user_prompt = input("Do you want to play? (Enter 'yes' to play or any other key to quit) ").lower()

    # Check if the user wants to play or not
    if user_prompt != "yes":
        print("Maybe next time!")
        return

    print("Okay! Let's play :)")

    # Questions and Answers
    questions = [
        "What is the nearest star to planet Earth?",
        "How many colors are in a rainbow?",
        "In what direction does the sunrise?",
        "How many weeks are in one year?"
    ]

    answers = ["sun", "7", "east", "52"]

    # Iterate through questions and get user's answers
    for i, question in enumerate(questions):
        user_answer = input(question + " ").lower()

        # Check if the user's answer is correct and give appropriate feedback
        if user_answer == answers[i]:
            print("You're brilliant! Correct!")
            score += 1
        else:
            print("Oh no, that's wrong.")

    # Calculate the total score and give feedback to the user
    print("Your score: ", score, " out of", len(questions))


# Call the function to run the game
play_guessing_game()


def test_guessing_game():
    # Test correct answers
    assert play_guessing_game(["sun", "7", "east", "52"]) == 4

    # Test wrong answers
    assert play_guessing_game(["moon", "6", "west", "12"]) == 0

    print("All tests passed!")

if __name__ == "__main__":
    test_guessing_game()
