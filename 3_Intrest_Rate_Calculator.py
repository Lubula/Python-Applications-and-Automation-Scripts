def calculate_monthly_payment(principal, annual_interest_rate, years):
    """
    Calculate the monthly repayment amount for a loan using the formula for
    the monthly payment of an amortizing loan.
    """
    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = (annual_interest_rate / 100) / 12

    # Calculate total number of payments
    total_payments = years * 12

    # Calculate the monthly payment using the formula for amortizing loan
    monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / \
                      ((1 + monthly_interest_rate) ** total_payments - 1)

    return monthly_payment

def main():
    """
    Main function to interact with the user and calculate the monthly repayment amount.
    """
    print("This is the Monthly Repayment Calculator")
    print("")

    # Collect user inputs: principal, annual interest rate, and years
    principal = float(input("Input the Loan Amount: "))
    annual_interest_rate = float(input("Input the Annual Interest Rate (%): "))
    years = int(input("Input the Duration of the Loan (in years): "))

    # Calculate the monthly repayment amount using the provided inputs
    monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)

    # Print the result
    print(f"The Monthly Repayment Amount for this Loan is: ${monthly_payment:.2f}")
    print(f"Over the Duration of {years} Years")
    print(f"At an Annual Interest Rate of {annual_interest_rate}%")

if __name__ == "__main__":
    main()
