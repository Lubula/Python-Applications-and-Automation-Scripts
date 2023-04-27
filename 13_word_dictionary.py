# Define a dictionary with word-definition pairs
word_dict = { 
    "maat": "Egyptian Goddess of Harmony and Balance",
    "atum": "The Creator God",
    "medu netcher": "The Language of God"
}

# Continuously prompt user for input until 'exit' is entered
while True:
    # Collect input from user, input is word
    word = input("Enter a word (type 'exit' to quit): ")
    
    # If the user enters 'exit', exit the loop
    if word.lower() == 'exit':
        print("Goodbye!")
        break

    # Check if word is in dictionary
    if word in word_dict:
        # Print the definition
        print(f"{word}: {word_dict[word]}")
    else:
        # If the word is not in the dictionary, inform the user
        print(f"Sorry, the word '{word}' is not in the dictionary.")
