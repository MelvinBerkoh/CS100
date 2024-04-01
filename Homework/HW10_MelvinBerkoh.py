'''
Melvin Berkoh
CS 100 Section 002
HW 09 April 1, 2024

'''

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
    # loop through the wordList
    for word in wordList:
        # the initial letter of the word
        initial_letter = word[0]
        # check if the initial letter is already a key in the dictionary
        if initial_letter in result:
            # check if the word is not already in the list associated with the key
            if word not in result[initial_letter]:
                # append the word to the list associated with the key
                result[initial_letter].append(word)
        else:
            # if the initial letter is not a key, create a new key with an empty list as value
            result[initial_letter] = [word]

    # return the dictionary
    return result


print(initialLetters(['In', 'say', 'what', 'I', 'mean', 'A',
                      'and', 'I', 'mean', 'what', 'I', 'say']))

'''
Write a function named
shareOneLetter that takes one parameter,
wordList – a list of words. Create and
return a dictionary in which each word in
wordList is a key and the corresponding value is a list of all the
words in
wordList that share at least one letter with that word. There should be no duplicate words in any
value in the dictionary.
For example, the following is correct output:
print(shareOneLetter(horton))
{'I': ['I'], 'say': ['say', 'what', 'mean', 'and'], 'what': ['say', 'what', 'mean', 'and'], 'mean': ['say', 'what', 'mean', 'and'],
'and': ['say', 'what', 'mean', 'and']}

'''


def sharedOneLetter(wordList):
    result = {}
    # loop through word list
    for word in wordList:
        if word not in result:
            result[word] = [word]
            for letter in word:
                for otherWord in wordList:
                  if letter in otherWord:
                     result[word].append(otherWord)

    return result


print(sharedOneLetter(['hi', 'name', 'is', 'paul', 'is']))

word = 'hi'
print(word.split())
