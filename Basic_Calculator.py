def get_number_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def perform_operation(operation, a, b):
    if operation == "a":
        add(a, b)
    elif operation == "b":
        sub(a, b)
    elif operation == "c":
        mult(a, b)
    elif operation == "d":
        div(a, b)

def main():
    while True:
        print("A. Addition\nB. Subtraction\nC. Multiplication\nD. Division\nE. Exit")

        choice = input("Enter your choice (A/B/C/D/E): ").lower()

        if choice == "e":
            print("Program Ended")
            quit()

        if choice not in {"a", "b", "c", "d"}:
            print("Invalid choice. Please enter A, B, C, D, or E.")
            continue

        print(f"{choice.upper()}. {get_operation_name(choice)}")
        a = get_number_input("Input your first number: ")
        b = get_number_input("Input your second number: ")
        perform_operation(choice, a, b)

def get_operation_name(operation):
    operation_names = {"a": "Addition", "b": "Subtraction", "c": "Multiplication", "d": "Division"}
    return operation_names.get(operation)

def add(a, b):
    ans = a + b
    print(f"{a} + {b} = {ans}")

def sub(a, b):
    ans = a - b
    print(f"{a} - {b} = {ans}")

def mult(a, b):
    ans = a * b
    print(f"{a} * {b} = {ans}")

def div(a, b):
    if b == 0:
        print("Cannot divide by zero.")
    else:
        ans = a / b
        print(f"{a} / {b} = {ans}")

if __name__ == '__main__':
    main()
