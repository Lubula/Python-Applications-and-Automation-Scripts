def add(a, b):
    ans = a + b
    print(str(a), "+", str(b), "=", str(ans))

def sub(a, b):
    ans = a - b
    print(str(a), "-", str(b), "=", str(ans))

def mult(a, b):
    ans = a * b
    print(str(a), "*", str(b), "=", str(ans))

def div(a, b):
    ans = a / b
    print(str(a), "/", str(b), "=", str(ans))

def main():
    while True:
        print("A. Addition\nB. Subtraction\nC. Multiplication\nD. Division\nE. Exit")

        choice = input("Enter your choice (A/B/C/D/E): ").lower()

        if choice == "a":
            print("Addition")
            a = int(input("Input your first number: "))
            b = int(input("Input your second number: "))
            add(a,b)
        elif choice == "b":
            print("Subtraction")
            a = int(input("Input your first number: "))
            b = int(input("Input your second number: "))
            sub(a,b)
        elif choice == "c":
            print("Multiplication")
            a = int(input("Input your first number: "))
            b = int(input("Input your second number: "))
            mult(a,b)
        elif choice == "d":
            print("Division")
            a = int(input("Input your first number: "))
            b = int(input("Input your second number: "))
            div(a,b)
        elif choice == "e":
            print("Program Ended")
            quit()

if __name__ == '__main__':
    main()
