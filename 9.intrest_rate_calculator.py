# collect the necessary inputs: principal, apr,years
# calculate the monthly repayment
# show the user

def main():
    print("This is the monthly repayment Calculator")
    print("")

    principal = float(input("Input the Loan Amount: "))
    monthly_intrest_rate = float(input("Input the annual intrest rate: "))
    years = int(input("Input the amount of years: "))

    amount_of_months = years * 12
    monthly_payments = principal / 1000 *10.16 

    print("The Monthly Repayment Amount For This Loan Is : " + str(monthly_payments))
    print("Over the duration of", amount_of_months, "Months")
    print("At an interst rate of", monthly_intrest_rate, "%")
    print("Disclaimer: only calculates the repayment of loan amount at 11.5% over 20years")

main()