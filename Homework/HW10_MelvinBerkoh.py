'''
Problem 1
Write a function named
initialLetterCount that takes one parameter,
wordList — a list of words. Create and
return a dictionary in which each initial letter of a word in
wordList is a key and the corresponding value
is the number of words in
wordList that begin with that letter. The keys in the dictionary should be case-
sensitive, which means 'a' and 'A' are two different keys.
For example, the following is correct output:
horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetterCount(horton))
{'I': 4, 's': 2, 'w': 2, 'm': 2, 'a': 1}
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
