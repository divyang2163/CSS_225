# Author:- Divyang Parikh
# Date: October 25, 2025
# Program: Prints whether numbers 1–50 are divisible by 3, 5, or both

# Loop through numbers 1 to 50
for i in range(1, 51):  # range(1, 51) gives 1 through 50
    # Check divisibility
    if i % 3 == 0 and i % 5 == 0:
        print("Divisible by both")
    elif i % 3 == 0:
        print("Divisible by three")
    elif i % 5 == 0:
        print("Divisible by five")
    else:
        print(i)
