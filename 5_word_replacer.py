def word_replacer():
    # Sample input text
    input_text = "Nsansa Inc and Nsansa Homes"
    
    # Get user input for word to replace and replacement word
    user_input = input("Enter the word to replace and the replacement word separated by a comma: ")

    # Validate user input
    if "," not in user_input:
        print("Invalid input. Please provide both the word to replace and the replacement word separated by a comma.")
        return

    # Split the user input into the word to replace and the replacement word
    word_to_replace, word_replacement = user_input.split(",")
    
    # Perform the replacement and print the result
    # Using replace with max replacement set to 1 to replace only the first occurrence
    replaced_text = input_text.replace(word_to_replace, word_replacement, 1)
    print(f"The result of the replacement is: {replaced_text}")

if __name__ == '__main__':
    # Call the word_replacer function when the script is run
    word_replacer()
