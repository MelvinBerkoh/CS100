'''
Problem 1
'''


def safeOpen(fileName):
    '''  Function that takes a file name and returns the file object if it exists else it returns None'''
    try:
        return open(fileName)
    except FileNotFoundError:
        return None


# test cases
print(safeOpen('ghost.txt'))


'''
Problem 2
'''


def safeFloat(x):
    '''  Function that takes a number or string and returns a floating point number constructed from a number or string. If the string doesn’t represent a valid floating point value, an exception is raised. If an exception is raised while trying to convert a number or string, safeFloat() should return 0.0 floating point value.'''
    try:
        return float(x)

    except ValueError:

        return 0.0


# testcase
print(safeFloat('abc'))

'''
Problem 3
A radar speed gun is a device used in law-enforcement to measure the speed of moving vehicles in miles
per hour. The measured speeds are supposed to be stored in a file, one number per line, as follows:
65.6
70.2
54.9
Unfortunately, due to an intermittent fault, occasionally multiple numbers are written on a single line as
follows:
73.2 65.6 69.8
Furthermore, occasionally the radar gun outputs a single stray character such as: 67.9z, 6$4.9, or a3.9, to
illustrate just a few.
Given a file that has radar speed gun readings, write a function
averageSpeed() to calculate the average of
the numbers in the file. Your code must adhere to the following specifications:
a. Prompt the user for the name of the input file to process. When the user enters a nonexistent file
name, give the user a second chance. After two wrong entries in a row, quit the program with an
appropriate message.
b. Ignore numbers containing stray characters.
c. Ignore any reading for slow vehicles moving at 2 miles per hour or less.
d. Print the final average to the console.
e. Make use of the functions
safeOpen() and
safeFloat().

>>>

'''
# test this file with the following code


def averageSpeed():
    '''  Function that calculates the average of the numbers in the file. '''
    # prompt the user for the name of the file
    fileName = input('Enter the name of the file: ')
    attempts = 0
    file = safeOpen(fileName)
    # check if the file exists
    while file == None:
        attempts += 1
        if attempts == 2:
            print('You have exceeded the number of attempts')
            break
        fileName = input('Enter the name of the file: ')
# now that we have the file opened we need to read from it line by line

    total = 0
    count = 0
    for line in file:
        # split the line by space
        for word in line.split():
            # check if the word is a number
            if safeFloat(word) > 2:
                total += safeFloat(word)
                count += 1
    print('The average speed is: ', total/count)
    file.close()
