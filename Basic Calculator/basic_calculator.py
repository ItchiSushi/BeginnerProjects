# Start by defining the functions needed to calculate the area of a circle such as add, subtract, divide, multiply
# Now we print the options for the use to choose from
# Ask the user for the values
# Call the appropriate functions
# Create a while loop to continue the program until the user wants to exit

def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))

def subtract(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))

def divide(a, b):
    answer = a / b
    print(str(a) + " ÷ " + str(b) + " = " + str(answer))

def multiply(a, b):
    answer = a * b
    print(str(a) + " x " + str(b) + " = " + str(answer))

user_answer = "Yes"

while user_answer:
    user_question = input("""
    Which Mathematics application would you like to use?
    
    a) Addition
    b) Subtraction
    c) Division
    d) Multiplication
    
    Choose a, b, c, or d: """)



