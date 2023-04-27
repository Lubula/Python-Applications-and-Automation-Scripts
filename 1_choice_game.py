print("Welcome to my first EVER game: How to Make a Decision!")
name = input("What is your name? ")
age = int(input("How old are you? "))
intuition = 0

if age >= 14:
    print("You are old enough! I wonder if you are mature enough though...")
    wants_to_play = input("Do you want to play? (yes/no) ").lower()

    if wants_to_play == "yes":
        print("Welcome,", name, ". You are", age, "years old. I wonder how mature you are? Your level of intuition is at", intuition, "%.")
        print("Let's begin!")

        first_choice = input("What do you depend on to make a decision? Head or Heart? (head/heart) ").lower()

        if first_choice == "heart":
            print("Heart = intuition! Do you identify the problem or define the problem?")
            intuition += 15
            ans = input("Type 'identify' or 'define': ").lower()

            if ans == "identify":
                print("Recognizing that something is not as it should be is the key first step.")
                intuition += 15
            
            elif ans == "define": 
                print("Clearly understanding the nature of the issue, its scope, and its underlying causes is important.")
                intuition += 5

            ans = input("Now gather information & evaluate options. Do you then take action or make a decision? (action/decide) ").lower()

            if ans == "decide": 
                print("Making a decision is the key. You're gaining intuition!")
                intuition += 15

                if intuition >= 30:
                    print("Your intuition level is at", intuition, "%. Well done!")
                else:
                    print("Your intuition level is less than 30%. GAME OVER <RESTART>")

            elif ans == "action":
                print("Being too hasty and taking action before making a decision is a critical error.")
                intuition -= 20

                if intuition <= 30:
                    print("Your intuition level is less than 30%. GAME OVER <RESTART>")
                else:
                    print("Your intuition level is at", intuition, "%. Well done!")
            else:
                print("You're lost now. You can't take action without making a decision first. Critical error! GAME OVER <RESTART>")

        else:
            print("Trust your intuition and follow your heart more. Leave the data crunching to the calculators. GAME OVER <RESTART>")

    else:
        print("BYE")

else:
    print("Still too young to play!")
