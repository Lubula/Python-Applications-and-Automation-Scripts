def main():
    print("This Program Converts US Dollars To Pounds Sterling")
    print("")

    # Prompt the user to enter an amount in dollars
    dollars = float(input("Enter Amount In Dollars: "))  # Using float() instead of eval() for safer input parsing

    # Call the convert_to_pounds function to calculate the equivalent amount in pounds
    pounds = convert_to_pounds(dollars)

    # Display the result with two decimal places for better clarity
    print("That is {:.2f} Pounds".format(pounds))  # Formatting the output to two decimal places

# A lambda function that takes dollars as input and returns the equivalent amount in pounds
convert_to_pounds = lambda dollars: dollars * 0.82

# Call the main function to execute the program
main()
