# Author: Divyang Parikh
# # Date: 11/08/25
# Problem 5: Use the given chunk of code to draw a pattern of concentric squares using the turtle module.

import turtle

# Function to draw one square of a given side length (sz)
def drawSquare(t, sz):
    """Get turtle t to draw a square with side length sz"""
    for i in range(4):     # Repeat 4 times for 4 sides
        t.forward(sz)      # Move forward by the side length
        t.left(90)         # Turn left 90° to make a corner

# Set up the screen and the turtle
wn = turtle.Screen()        # Create a window
alex = turtle.Turtle()      # Create a turtle named alex
alex.color("blue")          # Set turtle color to blue
alex.pensize(2)             # Slightly thicker line for visibility

# Draw several squares, each bigger and offset outward
size = 20                   # Starting side length
for i in range(5):          # Loop to draw 5 squares
    drawSquare(alex, size)  # Draw square of current size
    size += 20              # Increase size for the next square
    alex.penup()            # Lift pen to move without drawing
    alex.backward(10)       # Move backward slightly to center next square
    alex.right(90)
    alex.forward(10)        # Move down slightly to position next square
    alex.left(90)
    alex.pendown()          # Put the pen down again

wn.exitonclick()            # Wait for user click to close the window
