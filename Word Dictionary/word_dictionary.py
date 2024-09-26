# import PyDictionary library
from PyDictionary import PyDictionary
# Create a variable for the PyDictionary
dictionary = PyDictionary()
# Create a variable and assign it to the input function that will capture users input.
word = input("Enter a word: ")
# Display the different meanings of the word using the print function.
print(dictionary.meaning(word))
