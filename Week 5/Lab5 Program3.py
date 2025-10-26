# Author:- Divyang Parikh
# Date: October 25, 2025
# Program: Draws a regular polygon based on user input using turtle graphics

import turtle    # Import the turtle library

# Asking user for input
sides = int(input("Enter the number of sides: "))
length = int(input("Enter the length of each side: "))
line_color = input("Enter the line color: ")
fill_color = input("Enter the fill color: ")

# Creating turtle
t = turtle.Turtle()
t.pensize(3)                     # Make the line a bit thicker
t.color(line_color, fill_color)  # Set outline and fill colors
t.begin_fill()                   # Start filling

# Draw polygon
for i in range(sides):
    t.forward(length)            # Move forward
    t.left(360 / sides)          # Turn left to make equal angles

t.end_fill()                     # Stop filling the shape
turtle.done()                    # Keeps the window open
