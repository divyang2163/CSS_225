# Author:- Divyang Parikh
# Date: October 25, 2025
# Program: Prints each number from a list and its square

numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20] #Create the list of numbers

#Print each number one by one
print("Each number:")
for num in numbers:          # Loop through the list
    print(num)               # Print the current number
  
#Print each number and its square
print("\nEach number and its square:")   # \n to make a line between the programs
for num in numbers:                      # Loop again through the list
    print(num, "squared is", num ** 2)   # squaring numbers
