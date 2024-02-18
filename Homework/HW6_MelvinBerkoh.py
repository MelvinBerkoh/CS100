'''
Melvin Berkoh
CS 100 Section 002
HW 06, February 17, 2024
'''
''''
a. Write a function named isDivisible that takes two parameters
1.maxInt, an integer
2.twoInts, a tuple of two integers
The function isDivisible should create and return a list of all the ints in the range from 1 to
maxInt (not including maxInt) that are divisible of both ints in twoInts.
b. Create three test cases, each consisting of a value for
maxInt and a value for
twoInts, for your
function in Problem 2a. One of these tests should return the empty list. For each test case

'''
# Write a function named isDivisible that takes two parameters 1.maxInt, an integer 2.twoInts, a tuple of two integers


def isDivisible(maxInt, twoInts):
    #   create and return a list of all the ints in the range from 1 to
    # maxInt (not including maxInt) that are divisible of both ints in twoInts.
    lstOfInts = []
    for number in range(maxInt):
        if (number % twoInts[0] == 0) and (number % twoInts[1] == 0):
            lstOfInts.append(number)

    return lstOfInts


print(isDivisible(28, (2, 4)))
print(isDivisible(100, (5, 10)))
print(isDivisible(32, (4, 8)))
