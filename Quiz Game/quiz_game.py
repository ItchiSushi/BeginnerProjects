# Create a dictionary that stores questions and answers
quiz = {"Question 1": {
            "question": "What is the capital of France?",
            "answer": "Paris"
        },
        "Question 2": {
            "question": "Do penguins have feet?",
            "answer": "Yes"
        },
        "Question 3": {
            "question": "What color are crow birds?",
            "answer": "Black"
        },
        "Question 4": {
            "question": "How many legs do spiders have?",
            "answer": "8"
        },
        "Question 5": {
            "question": "Which president fought to free South Africa from Apartheid?",
            "answer": "Mandela"
        }

}
# Create a variable that tracks the score of the player
score = 0
# Loop through the dictionary using the key values pairs
for key, value in quiz.items():
    # Display each question to the user and allow them to answer
    print(key)
    print(value['question'])
    answer = input("answer: ").capitalize()
    # Tell them if they were right or wrong
    if answer == value['answer']:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print(f"The answer is {value['answer']}")
# Show the final result when quiz is completed
print(f"You got {score}/5! {str(int(score/5 * 100))}%!")