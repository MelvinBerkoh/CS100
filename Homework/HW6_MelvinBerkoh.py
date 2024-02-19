'''
Melvin Berkoh
CS 100 Section 002
HW 06, February 17, 2024
'''

def hasFinalLetter(strList, letters):
    ''' takes a list of strings and letter to match at the last index of each word in the string list'''
    lstOfStrings = []
    for word in strList:
        if (word[len(word)-1]) == letters:
            lstOfStrings.append(word)

    return lstOfStrings


# Test Cases
print(hasFinalLetter(['Melvin', 'Berkoh', 'is', 'a', 'student'], 'n'))
print(hasFinalLetter(['Melvin', 'Berkoh', 'is', 'a', 'student'], 'o'))
print(hasFinalLetter(['Melvin', 'Berkoh', 'is', 'a', 'student'], 't'))


# Write a function named isDivisible that takes two parameters 1.maxInt, an integer 2.twoInts, a tuple of two integers


def isDivisible(maxInt, twoInts):
    #   create and return a list of all the ints in the range from 1 to
    # maxInt (not including maxInt) that are divisible of both ints in twoInts.
    lstOfInts = []
    for number in range(maxInt):
        if (number % twoInts[0] == 0) and (number % twoInts[1] == 0):
            lstOfInts.append(number)

    return lstOfInts


# test cases
print(isDivisible(28, (2, 4)))
print(isDivisible(100, (5, 10)))
print(isDivisible(32, (4, 8)))