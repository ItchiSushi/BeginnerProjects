# Created a function that takes a list and target parameter from user.
def binary_search(list, element):
    # Created multiple variables :middle, start, end, steps
    middle = 0
    start = 0
    end = len(list)
    steps = 0
    # Create a while loop to use recursion to find the target value.
    while start <= end:
        # Display and increase the steps each time a split is done.
        print("Step" , steps, ":" , str(list[start: end + 1]))
        steps += 1
        middle = (start + end) // 2
        # Add if and else conditions to track target position.
        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1
    # Once found, return -1 to break out of the loop
    return -1

# Create a list and populate it with default values.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Here is the list: ", my_list)
# Set a variable to the input function that will prompt the user for a target value.
user_target = int(input("Chose a value in the list to count how many steps it takes to find the value: "))
# Call the binary_search function and populate the list and element parameters with my_list and the user_target.
binary_search(my_list, user_target)