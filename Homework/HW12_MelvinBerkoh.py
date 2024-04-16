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
For example, the following is correct input/output:
>>> inputFile = open('radar.txt')
>>> content = inputFile.read()
>>> print(content)
35.2
1.8
65.6
67.9z
70.2
73.2 a3.9 65.6 69.8
6$4.9
54.9
>>> inputFile.close()
>>>
>>> averageSpeed()
Enter file name: ghost.txt
File not found. Please try again.
Enter file name: phantom.txt
File not found. Yet another human error. Goodbye.
>>>
>>> averageSpeed()
>>> Enter file name: radar.txt
>>> Average speed is 62.07 miles per hour.
>>>

'''
