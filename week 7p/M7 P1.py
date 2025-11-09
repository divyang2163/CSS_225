# Author: Divyang Parikh
# Date: 11/08/25
# Problem 1: Write a function areaOfCircle(r) that returns the area of a circle of radius r.

import math

def areaOfCircle(r):
    area = math.pi * r ** 2             # Formula for area of a circle: π * r^2
    return area

# Asking the user to enter the radius
radius = float(input("Enter the radius of the circle: "))

# Calling the function and printing the result
print("The area of the circle is:", areaOfCircle(radius))
