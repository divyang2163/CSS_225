# Name: Divyang Parikh
# Date: 11/15/2025
# Program: Returns True if year is leap year, False otherwise

def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# Test run
y = int(input("Enter a year: "))
print("Leap Year?", is_leap(y))
