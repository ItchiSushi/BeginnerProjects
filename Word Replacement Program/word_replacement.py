# A function is created that will contain the functionality to replace the word in a sentence
def replace_word():
    # Created a string variable and initialized it to the input. The input will caption what the user types on keyboard and store it into the sentence variable.
    sentence = input("Type a sentence: ")
    # An if and else statement is created that will check if sentence is just a number with no words. If true, a message will be displayed and the program will quit.
    if sentence.isdigit():
        print("You entered numbers instead of words!")
        quit()
    word_to_replace = str(input("Enter the word you would like to replace: "))
    # Another if statement which will check if the word exists in the string variable and if true, it will replace that word.
    if sentence.__contains__(word_to_replace):
        word_replacement = str(input("Enter the replacement word: "))
        print(sentence.replace(word_to_replace, word_replacement))
    # Else, the program will prompt the user to enter the word to replace, and then to enter the new word that will replace the existing word using '.replace'. This will find the word in the sentence variable and replace that word with the new word.
    else:
        print("That word does not exist in this sentence!")
        quit()
# The function replace_word() is called at the end of the code which will execute the code inside that function.
replace_word()