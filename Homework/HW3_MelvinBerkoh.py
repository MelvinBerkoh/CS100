import math
import turtle

'''
Melvin Berkoh
CS 100 Section 002
HW 03, February 05, 2024
'''

'''
Write code that uses turtle graphics to draw an equilateral triangle, a square and a regular pentagon,
each with side length 100.
2. Write code that uses turtle graphics to draw four concentric circles of radius 50, 100, 150 and 200.
3. Write code that uses the Python math module to compute and print out the values of
a. 100!
b. the log (base 2) of 1,000,000
c. the greatest common divisor of 63 and 49
'''
# 1. Write code that uses turtle graphics to draw an equilateral triangle, a square and a regular pentagon,
# each with side length 100.

# always need to add a screen
myScreen = turtle.Screen()
# make a pen
myPen = turtle.Turtle()
# forward moves the pen while left rotates the pen
# Creating an equilateral triangle
myPen.forward(100)
myPen.left(120)
myPen.forward(100)
myPen.left(120)
myPen.forward(100)
# reset the position of the turtle
myPen.reset()

# Creating a square
# had to add this because when in VS when using turtle it  closes after program is ran
turtle.exitonclick()
