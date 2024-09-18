# Define a function that will perform the monthly interest calculation
def main():
    print("This is a monthly payment loan calculator!")
    print("")
    # Create a while loop that will loop through the calculation when the user wants to perform multiple calculations.
    while True:
        # Create and set appropriate variables and initialize them to inputs that will be captured by the user.
        principal =  float(input("Provide the loan amount: "))
        apr = float(input("Provide the annual interest rate: "))
        years = int(input("Provide the amount of years: "))
        # Create and set appropriate variables that will perform basic calculations with the input provided variables.
        month_interest_rate = apr / 1200
        amount_of_months = years * 12
        # Finally set one main variable to calculate the monthly payment.
        monthly_payment = principal * month_interest_rate / (1 - (1+ month_interest_rate) ** (-amount_of_months))
        # Display the amount payable each month in Rands and by 2 decimals
        print("The monthly payment for this loan  is: R%.2f " % monthly_payment)
        print("")
        # Prompt the user to do another calculation. If the user chooses yes, the while loop continues. If the user
        # chooses no, a goodbye message is displayed and the program quits.
        question = input("Would you like to do another calculation? Yes or No: ").capitalize()
        if question == "Yes":
            print("")
            continue
        else:
            print("Goodbye!")
            quit()

# Call the function main()
main()
