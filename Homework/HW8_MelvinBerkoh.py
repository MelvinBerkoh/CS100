'''
Melvin Berkoh
CS 100 Section 002
HW 08, March 07, 2024
'''

'''
This problem provides practice using a while True loop.
Write a function named twoWords that gets and returns two words from a user. The first word is of a
specified length, and the second word begins with a specified letter.
The function twoWords takes two parameters:
1. an integer, length, that is the length of the first word and
2. a character, firstLetter, that is the first letter of the second word. The second word may begin with
either an upper or lower case instance of firstLetter.
The function twoWords should return the two words in a list. Use a while True loop and a break statement
in the implementation of twoWords.
The following is an example of the execution of twoWords:
print(twoWords(4, 'B'))
Enter a 4-letter word please: two
Enter a 4-letter word please: one
Enter a 4-letter word please: four
Enter a word beginning with B please: apple
Enter a word beginning with B please: pear
Enter a word beginning with B please: banana
['four', 'banana']

'''


def twoWords(number, letter):
    result = []
    # make sure to edit this before submitting due to not using breaks
    # ask user question cast number to str and keep letter as string
    question1 = input('Enter a '+str(number)+'-letter word please: ')
    while (True):
        if (len(question1) != number):
            question1 = input('Enter a '+str(number)+'-letter word please: ')
        else:
            break
    result.append(question1)
    question2 = input('Enter a word beginning with ' + letter + ' please: ')
    while (True):
        if ((question2[0] != letter) and (question2[0] != letter.lower())):
            question2 = input(
                'Enter a word beginning with ' + letter+' please: ')
        else:
            break
    result.append(question2)
    return result


print(twoWords(4, 'B'))


# Problem 2

def twoWordsV2(number, letter):
    result = []

    # ask user question cast number to str and keep letter as string
    question1 = input('Enter a '+str(number)+'-letter word please: ')
    while (len(question1) != number):

        question1 = input('Enter a '+str(number)+'-letter word please: ')

    result.append(question1)

    question2 = input('Enter a word beginning with ' + letter + ' please: ')
    while ((question2[0] != letter) and (question2[0] != letter.lower())):
        question2 = input('Enter a word beginning with ' + letter+' please: ')

    result.append(question2)
    return result


print(twoWordsV2(4, 'B'))
