def calculate_monthly_payment(principal, annual_interest_rate, years):
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    total_payments = years * 12

    monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate)**total_payments) / \
                      ((1 + monthly_interest_rate)**total_payments - 1)

    return monthly_payment

def main():
    print("This is the monthly repayment Calculator")
    print("")

    principal = float(input("Input the Loan Amount: "))
    annual_interest_rate = float(input("Input the annual interest rate: "))
    years = int(input("Input the amount of years: "))

    monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)

    print(f"The Monthly Repayment Amount For This Loan Is: {monthly_payment:.2f}")
    print(f"Over the duration of {years} Years")
    print(f"At an interest rate of {annual_interest_rate}%")

main()
