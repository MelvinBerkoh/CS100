'''
Melvin Berkoh
CS 100 Section 002
HW 12 April 22, 2024
'''

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


'''
# test this file with the following code


def averageSpeed():
    '''  Function that calculates the average of the numbers in the file. '''
    attempts = 0
    # loop to allow the user to enter the file name twice
    while attempts < 2:
        fileName = input('Enter the name of the file: ')
        file = safeOpen(fileName)
        # check if the file exists
        try:
            if file is not None:
                total = 0
                count = 0
                try:
                    # loop through the file and get the numbers
                    for line in file:
                        for word in line.split():
                            try:
                                # check if the word is a number
                                speed = safeFloat(word)
                                # check if the number is greater than 2
                                if speed > 2:
                                    total += speed
                                    count += 1
                            except ValueError:
                                pass
                    if count > 0:
                        print('The average speed is:', total / count)
                    else:
                        print('No valid speeds found in the file.')
                    return
                finally:
                    file.close()
            else:
                print('File not found.')
        except FileNotFoundError:
            print('File not found.')
        attempts += 1
    print('You have exceeded the number of attempts.')


averageSpeed()
