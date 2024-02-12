'''
Melvin Berkoh
CS 100 Section 002
HW 04, February 11, 2024
'''


'''
1. Write Python code that does the following:
'''
# a. Assigns the values 3, 4 and 5 to the variables a, b and c, respectively.

a = 3
b = 4
c = 5
#  Write an if statement that prints “OK” if a is less than b
if a < b:
    print("OK")
#  Write an if statement that prints “OK” if c is less than b
if c < b:
    print("OK")
#  Write an if statement that prints “OK” if the sum of a and b is equal to c
if (a+b) == c:
    print("OK")
#  Write an if statement that prints “OK” if the sum of a squared and b squared equals c squared.

if (a**2)+(b**2) == c**2:
    print("OK")
'''
2. Repeat the previous problem with the additional requirement that “NOT OK” is printed if the
condition is false.
'''
if a < b:
    print("OK")
else:
    print("NOT OK")
#  Write an if statement that prints “OK” if c is less than b
if c < b:
    print("OK")
else:
    print("NOT OK")
#  Write an if statement that prints “OK” if the sum of a and b is equal to c
if (a+b) == c:
    print("OK")
else:
    print("NOT OK")
#  Write an if statement that prints “OK” if the sum of a squared and b squared equals c squared.

if (a**2)+(b**2) == c**2:
    print("OK")
else:
    print("NOT OK")
'''
3. Write a program that asks the user for a color, a line width, a line length and a shape. Assume that
the user will specify a shape that is either a line, a triangle, or a square. Use turtle graphics to draw
the shape that the user requests of the size, color, line width and line length that the user requests.
For example, if these are the user choices for color, width, line length and shape, the blue triangle
below would be correct graphical output
what color? blue
what line width? 25
what line length? 100
line, triangle or square? triangle
'''
