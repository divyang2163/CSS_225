# Name: Divyang Parikh
# Date: 11/15/2025
# Program: Checks the sum of two inputs against 10

def sum_check():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    total = x + y

    if total > 10:
        print("The sum is greater than 10.")
    elif total < 10:
        print("The sum is less than 10.")
    else:
        print("The sum is exactly 10.")

# Test run
sum_check()
