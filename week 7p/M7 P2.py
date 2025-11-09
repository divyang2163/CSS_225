# Author: Divyang Parikh
# Date: 11/08/25
# Problem 2: Write a Python function to check if a number is in range(1,10).

# Function to check if the number is in a given range
def check_range(num):
    if num in range(1, 10):             # The range(1,10) includes numbers 1 through 9
        print(f"{num} is in the range.")
    else:
        print(f"{num} is not in the range.")

# Taking user input and calling the function
number = int(input("Enter a number: "))
check_range(number)