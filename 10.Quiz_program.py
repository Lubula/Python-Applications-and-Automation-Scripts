# dictionary that contains a list of questions (quiz)
# generate the score to all correct questions (a counter)
# a dictionary that stores questions and ansers
# a variable that tracks the scroe (a counter)
# loop through the dictionary that usesd the key value pairs
# display each question to the user and allow them to the user
# display if they are right or wrong 

quiz= {
    "question1": {
        "question": "what is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "what is the capital of Italy?",
        "answer": "Rome"
    },
    "question3": {
        "question": "what is the capital of Spain?",
        "answer": "Madrid"
    },
    "question4": {
        "question" : "what is the capital of Germany?",
        "answer": "Berlin"
    },
     "question5": {
        "question": "what is the capital of Ghana?",
        "answer": "Accra"
    },
    "question6": {
        "question": "what is the capital of Zambia?",
        "answer": "Lusaka"
    },
    "question7": {
        "question": "what is the capital of Austria?",
        "answer": "Vienna"
    },
    "question8": {
        "question": "what is the capital of Portugal?",
        "answer": "Lisbon"
    },
}

# variable that tracks score
score = 0

# loop through a dictionary
for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score += 1
        print("Your score is: ", str(score))
        print("")
        print("")
    else:
        print("wrong !")
        print("The answer is: ", value["answer"])
        print("Your score is: ", str(score))
        print("")
        print("")

print("You got" + str(score)+ "out of 7 qestions correctly")
print("Yor percentage is " + str(int(score/7 *100)) + "%")