# Author:- Divyang Parikh
# Date: October 25, 2025
# Program: Draws a fun smiley face with sunglasses using turtle graphics

import turtle

# Creating turtle and basic setup
t = turtle.Turtle()
t.speed(7)                # Set drawing speed
t.pensize(3)              # Make lines thicker for visibility
turtle.bgcolor("purple")  # Background color

# Draw the yellow face circle
t.penup()
t.goto(0, -100)           # Move turtle down to center face properly
t.pendown()
t.color("black", "yellow")  # Outline and fill color
t.begin_fill()
t.circle(100)             # Draw circle with radius 100
t.end_fill()

# Draw left sunglass lens
t.penup()
t.goto(-45, 30)
t.pendown()
t.color("black", "black")
t.begin_fill()
t.circle(20)
t.end_fill()

# Draw right sunglass lens
t.penup()
t.goto(45, 30)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()

# Connect sunglasses (bridge)
t.penup()
t.goto(-25, 45)
t.pendown()
t.pensize(5)
t.forward(50)

# Draw smile
t.penup()
t.goto(-40, -20)
t.setheading(-60)
t.pendown()
t.pensize(5)
t.color("black")
t.circle(50, 120)  # Draw an arc for the smile

# Hide turtle and finish
t.hideturtle()
turtle.done()
