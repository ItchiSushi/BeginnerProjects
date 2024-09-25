# Define a function that will check if the year entered by user is a leap year.
def is_leap_year(year):
    # Use nested if statements to check if the year provided in the variable can be modded to 0. If it is, then the year is a leap year.
    # If not then it will display a message saying that it is not a leap year.
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("That is a Leap Year!")
            else:
                print("Not a Leap Year!")
        else:
            print("That is a Leap Year!")
    else:
        print("Not a Leap Year!")
# Call the function is_leap_year() and prompt the user to enter a year. Convert to the input to an integer so that it is parseable in the function.
is_leap_year(int(input("Enter a year to check if it is a leap year: ")))