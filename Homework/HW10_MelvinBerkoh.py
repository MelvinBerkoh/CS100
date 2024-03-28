

'''
Problem 1
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

'''

Problem 2
Write a function named
initialLetters that  There should be no duplicate words in any value in the
dictionary.
For example, the following is correct output:
print(initialLetters(horton))
{'I': ['I'], 's': ['say'], 'w': ['what'], 'm': ['mean'], 'a': ['and']}

'''


def initialLetters(wordList):
    '''
    Takes one parameter,wordList – a list of words. Create and return a dictionary in which each initial letter of a word in
    wordList is a key and the corresponding value is a list of the words in wordList that begin with that letter.
    '''
    # create the dictionary
    result = {}
    # loop though the wordList
    for word in wordList:
        # check to see if the first letter in the word we are looking at is in the dictionary
        if word[0] in result:

            # if found add the word to the value of that key
            result[word[0]] = word
        else:
            # if the first letter of the word  isn't found create a key with the letter and make the value word
            result[word[0]] = word

    # return the dictionary
    return result


print(initialLetters(['I', 'say', 'what', 'I', 'mean', 'A',
                      'and', 'I', 'mean', 'what', 'I', 'say']))
