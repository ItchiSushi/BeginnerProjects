# Define a main function that will perform the conversion.
def main():
    # Display message at the start of the program.
    print("This program converts US dollars to South African rands.")
    print()
    # Create a variable and input for the user to provide a value
    # Wrap the input in an eval function which evaluates what is inside the string.
    dollars = eval(input("Enter the amount in dollars: "))
    # Create a rands variable which will be assigned to the convert_to_rands() that was initialised outside the main() function.
    rands = convert_to_rands(dollars)

    print("That is", rands, "rands.")
# Create a variable and assign it to a lambda function that will perform the currency conversion.
convert_to_rands = lambda dollars: dollars * 17.21
# Call the function to begin the program.
main()