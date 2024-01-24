import string
import math
'''
Melvin Berkoh
CS 100 Section 002
HW 01, January 19, 2024
'''
# three assignment lines, each of which creates a variable (object) with a meaningful name and assigns it an int value.

currentAge = 20
currentYear = 2024
currentMonth = 1

# three assignment lines, each of which creates a variable (object) with a meaningful name and assigns it a float value.

money = 123.45
weightInPounds = 123.23
lengthInCm = 12.4

# three assignment lines, each of which creates a string variable with a meaningful name.

dateOfBirth = '2003-15-03'
name = 'Melvin Berkoh'
favoriteAnimal = 'Cat'

'''
Exercise 1.1

1.In a print statement, what happens if you leave out one of the parentheses, or both?

Answer: You will receive an error when trying to run the code. Since the print statement is in a sense a function it needs to have both parenthesis. 

2. If you are trying to print a string, what happens if you leave out one of the quotation marks,
or both?

Answer:  you will receive an error when trying to run the code. If the code is missing one of the quotation marks it would treat everything after that quotation mark as a string. The quotes mark the beginning  and end of a string literal.
In Addition to that if a word is put into a print statement without quotes and is not a reserved keyword it would be treated as a variable. 

3. You can use a minus sign to make a negative number like -2. What happens if you put a plus
sign before a number? What about 2++2?

Answer: if you put plus in front of the number it makes that number positive. If you input 2++2 it would result in the addition of the two numbers.
For example a++b would be the same as a+(+b) make the b positive and adding them. If the input was a+(-b) it would add a negative number subtracting the two numbers.

'''

'''
Exercise 1.2. Start the Python interpreter and use it as a calculator.

'''
# 1. How many seconds are there in 42 minutes 42 seconds?
minutesToSeconds = 42 * 60
result = minutesToSeconds + 42
print(result, ' seconds')

# 2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
milesToKm = 10 * 1.61
print(milesToKm, ' miles')

# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?
pace = milesToKm / result  # pace in miles to seconds

# this would convert the seconds to minutes note that the reminder is seconds
print('The pace in which you are running (miles to minutes) is: ',
      round((pace*60), 2), 'mins')
# this would convert the seconds to minutes note that the reminder is minutes
print('The pace in which you are running (miles to hours) is: ',
      round((pace*60*60), 2), 'mph')


'''
Exercise 2.1. Repeating my advice from the previous chapter, whenever you learn a new feature,
you should try it out in interactive mode and make errors on purpose to see what goes wrong. • 

'''
# 1. We’ve seen that n = 42 is legal. What about 42 = n?
# 42 = n
# Answer: You will receive a SyntaxError i believe due to the order in which you write the assignment statement its usually variableName = value
# How about x = y = 1?
# x = y = 1
# Answer: This expression is valued it would assignment the value of 1 to y then the value of y to x so both x and y would hold the value of 1

# • In some languages every statement ends with a semi-colon, ;. What happens if you put a semi-colon at the end of a Python statement?
# x = 1;
# Answer: in the python language semicolons are not needed but can be used as a end of statement. In my IDE when I save with a semicolon at the end of a statement it gets removed

# What if you put a period at the end of a statement?
# print('hello world').
# Answer: periods at the end of a statement gives a SyntaxError. When using the period in python it is used followed by a member function for example math.pi as shown in an example later on.

'''
Exercise 2.2. Practice using the Python interpreter as a calculator:
'''
# 1. The volume of a sphere with radius r is 43 πr3. What is the volume of a sphere with radius 5?

# radius of 43
result = 4/3 * math.pi * 43**3
print('The volume of a sphere with radius 43:', round(result, 2), 'm^3')

# radius of 5
result = 4/3 * math.pi * 5**3
print('The volume of a sphere with radius 5:', round(result, 2), 'm^3')

# 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?


numberOfBooks = 60
basePrice = 24.95 * numberOfBooks
discountedPrice = basePrice - (basePrice * .4)
numberOfBooks = numberOfBooks - 1
total = discountedPrice + 3 + (.75*numberOfBooks)
print('If you purchased sixty books the total price would be : $', round(total, 2))

# 3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile)
# and 1 mile at easy pace again, what time do I get home for breakfast?
