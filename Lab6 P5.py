# Author: Divyang Parikh
# Date: 10/30/25
# Problem 5 – Convert radians to degrees

import math  # Import math module

radians = float(input("Enter value in radians: "))  # Ask user to enter a value in radians

# Manual conversion formula: degrees = radians * (180 / π)
manual_degrees = radians * (180 / math.pi)

# Use math.degrees() function to verify the result
math_degrees = math.degrees(radians)

# Display both results
print("Manual conversion (radians to degrees):", manual_degrees)
print("Using math.degrees() function:", math_degrees)