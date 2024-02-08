import math
import turtle

'''
Melvin Berkoh
CS 100 Section 002
HW 03, February 05, 2024
'''


# 1. Write code that uses turtle graphics to draw an equilateral triangle, a square and a regular pentagon,
# each with side length 100.

# always need to add a screen
myScreen = turtle.Screen()
# make screen a little larger
myScreen.screensize(900, 900)
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
myPen.forward(100)
myPen.left(90)
myPen.forward(100)
myPen.left(90)
myPen.forward(100)
myPen.left(90)
myPen.forward(100)
myPen.left(90)
# reset
myPen.reset()

# creating a pentagon
myPen.forward(100)
myPen.left(120)
myPen.forward(100)
myPen.left(120)
myPen.forward(100)
myPen.right(330)
myPen.forward(100)
myPen.left(90)
myPen.forward(100)
myPen.left(90)
myPen.forward(100)
myPen.reset()

# 2. Write code that uses turtle graphics to draw four concentric circles of radius 50, 100, 150 and 200.

myPen.circle(50)
myPen.home()
myPen.circle(100)
myPen.home()
myPen.circle(150)
myPen.home()
myPen.circle(200)

# had to add this because when in VS when using turtle it  closes after program is ran
turtle.exitonclick()

# 3. Write code that uses the Python math module to compute and print out the values of
# a. 100!
print('100! is ', math.factorial(100))

# b. the log (base 2) of 1,000,000
print('the log (base 2) of 1,000,000 is about ', round(math.log2(1000000), 2))

# c. the greatest common divisor of 63 and 49
print('the greatest common divisor of 63 and 49 is ', math.gcd(63, 49))
