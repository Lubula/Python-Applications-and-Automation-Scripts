def word_replacer():
    input_text = "Nsansa Inc and Nsansa Homes"
    word_to_replace, word_replacement = input("Enter the word to replace and the replacement word separated by a comma: ").split(",")
    print(f"The result of the replacement is: {input_text.replace(word_to_replace, word_replacement)}")

if __name__ == '__main__':
    word_replacer()

word_replacer()