# Import random for the random selection of the dice
import  random
# define a function to roll the dice
def roll_dice():
    # create a dictionary that will hold the values of the dice
    dice = {
        1: "⚀",
        2: "⚁",
        3: "⚂",
        4: "⚃",
        5: "⚄",
        6: "⚅"
    }
    user_answer = input("Would you like to roll the dice? Yes or No: ")
    # Create a while loop repeatedly ask the user to roll. If yes, the dice will roll twice, if no, the loop will end.
    while user_answer.capitalize() == "Yes":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        # Display the dice after it has been rolled.
        print(f"The dice rolled: {dice1} and {dice2}")
        print("\n".join(dice[dice1]))
        print("\n".join(dice[dice2]))
        # Prompt user again to roll
        user_answer = input("Roll dice again? Yes or No: ")
# Call the dice function to begin program.
roll_dice()