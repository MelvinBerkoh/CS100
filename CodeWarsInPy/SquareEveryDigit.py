""" Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.

Happy Coding!"""


def square_digits(num):
    result = ''
    # loop though the given sequence digit would be the each number while num is the list we are looking though since integers are not itratatable i casted it to a str
    for digit in str(num):
      # now that we can loop though the number we have to cast it back to int in order to do logical operations with the data
        squaredValue = int(digit)**2
        # in order to add it back to the result string the result has to be a string
        result += str(squaredValue)
        # return back a integer value
    return int(result)


print(square_digits(21))
