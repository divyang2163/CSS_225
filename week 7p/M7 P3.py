# Author: Divyang Parikh
# Date: 11/08/25
# Problem 3: Write a function that multiplies all the numbers in a list.

# Function definition: takes a list as input
def multiplyList(lst):
    result = 1        # Starting with 1 because multiplying by 0 will make everything 0
    for i in lst:     # Loop through each number in the list
        result *= i   # Multiply result by each number
    return result

# Predefined list as mentioned in the problem
numbers = [5, 2, 7, -1]

print("The product of all numbers in the list is:", multiplyList(numbers))