'''
Prompt : 
Find the longest substring in alphabetical order.

Example: the longest alphabetical substring in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".

There are tests with strings up to 10 000 characters long so your code will need to be efficient.

The input will only consist of lowercase characters and will be at least one letter long.

If there are multiple solutions, return the one that appears first.

Good luck :)

'''


def longest(st):
    # so given a string we have to return it in alphabetical order
    # create an array to letters to compare the letters by index
    # array = []
    # for letter in st:
    #     # add all the values to an array
    #   array.append(letter)
    #   for char in array:
    #     if char > array[]
    result = ''
    for i in range(0, len(st)):
        if st[i] > st[i+1]:
            result = result + st[i]
    print(result)


longest('abcdefg')
