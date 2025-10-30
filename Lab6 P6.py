# Author: Divyang Parikh
# Date: 10/30/25
# Problem 6 – Compute factorial manually and using math.factorial()

import math  # Import math module

num = int(input("Enter a number to find its factorial: "))  # Ask user for input

fact = 1                  # Calculate factorial manually using a for loop
for i in range(1, num + 1):
    fact *= i             # Multiply all numbers from 1 to num

# Display both results
print("Manual factorial result:", fact)
print("Using math.factorial():", math.factorial(num))