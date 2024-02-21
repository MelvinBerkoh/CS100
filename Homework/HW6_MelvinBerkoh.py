'''
Melvin Berkoh
CS 100 Section 002
HW 06, February 17, 2024
'''


def hasFinalLetter(strList, letters):
    ''' takes a list of strings and letter to match at the last index of each word in the string list'''
    lstOfStrings = []
    for word in strList:
        if (word[len(word)-1]) in letters:
            lstOfStrings.append(word)

    return lstOfStrings


# Test Cases
testCase1 = ['Melvin', 'Berkoh', 'is', 'a', 'student']
testCase1Letter = 'nhjl'
print(hasFinalLetter(testCase1, testCase1Letter))
testCase2 = ['Melvin', 'Berkoh', 'is', 'a', 'student']
testCase2Letter = 'oxZ'
print(hasFinalLetter(testCase2, testCase2Letter))
testCase3 = ['Melvin', 'Berkoh', 'is', 'a', 'student', 'bucket']
testCase3Letter = 'tAbx'
print(hasFinalLetter(testCase3, testCase3Letter))


# Write a function named isDivisible that takes two parameters 1.maxInt, an integer 2.twoInts, a tuple of two integers
def isDivisible(maxInt, twoInts):
    # create and return a list of all the ints in the range from 1 to maxInt (not including maxInt) that are divisible of both ints in twoInts.
    lstOfInts = []
    for number in range(1, maxInt):
        if (number % twoInts[0] == 0) and (number % twoInts[1] == 0):
            lstOfInts.append(number)
    return lstOfInts


# test cases
maxInt1 = 28
maxInt2 = 100
maxInt3 = 32
t1 = (2, 4)
t2 = (5, 10)
t3 = (7, 8)
print(isDivisible(maxInt1, t1))
print(isDivisible(maxInt2, t2))
print(isDivisible(maxInt3, t3))
