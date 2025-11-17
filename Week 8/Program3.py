# Name: Divyang Parikh
# Date: 11/15/2025
# Program: Checks if the value 5 exists in a list

def find_five():
    user_list = input("Enter numbers separated by spaces: ")
    numbers = [int(num) for num in user_list.split()]

    if 5 in numbers:
        print("The number 5 IS in the list.")
    else:
        print("The number 5 is NOT in the list.")

# Test run
find_five()
