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
