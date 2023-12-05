# Dictionary that contains a list of questions (quiz)
quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question3": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question4": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question5": {
        "question": "What is the capital of Ghana?",
        "answer": "Accra"
    },
    "question6": {
        "question": "What is the capital of Zambia?",
        "answer": "Lusaka"
    },
    "question7": {
        "question": "What is the capital of Austria?",
        "answer": "Vienna"
    },
    "question8": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
}

# Variable that tracks score
score = 0

# Loop through the dictionary
for key, value in quiz.items():
    # Display the question to the user
    print(value['question'])
    
    # Allow the user to input an answer
    answer = input("Answer? ")

    # Check if the answer is correct
    if answer.lower() == value['answer'].lower():
        print('Correct')
        score += 1
    else:
        print("Wrong! The correct answer is:", value["answer"])

    # Display the current score
    print("Your score is:", score)
    print("\n" + "-" * 30 + "\n")  # Separator for better readability

# Display the final score
print("You got", str(score), "out of", len(quiz), "questions correctly")
print("Your percentage is", str(int(score / len(quiz) * 100)) + "%")
