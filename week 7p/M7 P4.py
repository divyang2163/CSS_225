# Author: Divyang Parikh
# Date: 11/08/25
# Problem 4: Write a function that returns a list of unique elements from a given list.

# Function definition: takes a list as input
def uniqueList(lst):
    unique = []         # Empty list to store unique elements
    for i in lst:       # Loop through all numbers in the given list
        if i not in unique:  # Add the number to the new list only if it’s not already there
            unique.append(i)
    return unique  # Return the list with only unique values

# Predefined list given in the assignment
numbers = [1, 3, 3, 3, 6, 2, 3, 5]

# Calling the function and printing the unique list
print("Unique elements from the list are:", uniqueList(numbers))