# Import string for ascii values and random to randomise the string values
import string
import random
# Defined a function that generate the random password.
def password_generation(length):
   # Place the characters into a list so that each character and symbol can be accessed.
   characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
   # Use random.shuffle to randomise the characters in the variable each time the function is called.
   random.shuffle(characters)
   new_password = ""
   # Create a for loop for the length provided by the user to generate a password
   for x in range(length):
        new_password = new_password + (characters[x])
   # Print statement to display password
   print(f"Your new password is {new_password}")
# Create a while loop that will continue looping as long as the user chooses yes
while True:
    # Prompt to user to generate a random password.
    user_password_question = input("Would you like to generate a password? Yes or No: ").capitalize()
    # If they say yes, we prompt for the length of the password
    if user_password_question == "Yes":
        password_length = input("How long would you like your password to be? ")
        password_generation(int(password_length))
    # If initial response is no or something else, display message and exit program
    else:
        print("Goodbye!")
        quit()

