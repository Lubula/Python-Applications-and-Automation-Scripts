# program that converts us dollers to british pounds
# use a lambda function
# can add an api to add all the currency that can be called 

def main():
    print("This Program Converts US Dollers To Pounds Sterling")
    print("")

    dollars = eval(input("Enter Amount In Dollers: "))
    pounds = convert_to_pounds(dollars)
    print("That is", pounds, "Pounds")

convert_to_pounds = lambda dollars: dollars * 0.82

main()