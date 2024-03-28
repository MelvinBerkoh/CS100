'''

Problem 2
Write a function named
initialLetters that takes one parameter,
wordList – a list of words. Create and return
a dictionary in which each initial letter of a word in
wordList is a key and the corresponding value is a list
of the words in
wordList that begin with that letter. There should be no duplicate words in any value in the
dictionary.
For example, the following is correct output:
print(initialLetters(horton))
{'I': ['I'], 's': ['say'], 'w': ['what'], 'm': ['mean'], 'a': ['and']}

'''
'''
Problem 1
 The keys in the dictionary should be case-
sensitive, which means 'a' and 'A' are two different keys.
For example, the following is correct output:
horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetterCount(horton))
{'I': 4, 's': 2, 'w': 2, 'm': 2, 'a': 1}
'''


def initialLetterCount(wordList):
    '''
    Takes one parameter,wordList — a list of words. The function creates and return a dictionary in which each initial letter of a word in
    wordList is a key and the corresponding value is the number of words in wordList that begin with that letter. 
    '''
    # create the dictionary
    result = {}

    # loop though the wordList
    for word in wordList:
        # check to see if the first letter in the word we are looking at is in the dictionary
        if word[0] in result:

            # if found add one to the value of that key
            result[word[0]] += 1
        else:
            # if the first letter of the word  isn't found create a key with the letter and make the value one
            result[word[0]] = 1

    # return the dictionary
    return result


# test case
print(initialLetterCount(['I', 'say', 'what', 'I', 'mean', 'A',
                          'and', 'I', 'mean', 'what', 'I', 'say']))
