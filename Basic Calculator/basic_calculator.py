# Defined a function for addition that the program will call and use.
def add(a, b):
    # Uses math operator for addition.
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))
# Defined a function for subtraction that the program will call and use.
def subtract(a, b):
    # Uses math operator for subtraction.
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))
# Defined a function for division that the program will call and use.
def divide(a, b):
    # Uses math operator for division.
    answer = a / b
    print(str(a) + " ÷ " + str(b) + " = " + str(answer))
# Defined a function for multiplication that the program will call and use.
def multiply(a, b):
    # Uses math operator for multiplication.
    answer = a * b
    print(str(a) + " x " + str(b) + " = " + str(answer))
# Defined a question function that will be called at the start and during and the program.
def question():
    user_question = input("Would you like to use the calculator? Answer Yes or No: ").lower()
    #Use an if else statement to return the user answer for yes or no.
    if user_question != "yes":
        print("Goodbye!")
        quit()
    else:
        return user_question
# Created a while loop that will continue to loop through the program as long as the returned string value of the question function remains "yes".
while question() == "yes":
    # Prompt the user for the first and second number and store them in variables.
    user_number1 = int(input("Enter your first number: "))
    user_number2 = int(input("Enter your second number: "))
    # Prompt the user to choose a math operator from the options provided using the triple quoted (multi-line) docstring.
    calculator_question = input("""
    Which Mathematics application would you like to use?
        
    a) Addition
    b) Subtraction
    c) Division
    d) Multiplication
        
    Choose a, b, c, or d: """).lower()
    #Created if, elif, and else statement that will capture the option that the user has chosen and call the desired function to perform that calculation. Restart the program if the user enters an invalid option.
    if calculator_question == "a":
         add(user_number1, user_number2)
    elif calculator_question == "b":
        subtract(user_number1, user_number2)
    elif calculator_question == "c":
        divide(user_number1, user_number2)
    elif calculator_question == "d":
         multiply(user_number1, user_number2)
    else:
        print("Invalid!")








