# simple dictionary
# python dictionary that has a key value pair that represents a word and definition
# collect input from user, input is word
# check if word in dictionary
# print the definition

def main():
    word_dict = { 
        "maat": "Egyptian Goddess of Harmony and Balance",
        "atum": "THe Creator God",
        "medu netcher" : "The Language of God"
    }
    
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        if word in word_dict:
            print(word,":", word_dict[word])

main()

# add a file that has the text for the diction or use a python library 
# import py dictionary as this has already been created 