'''

Problem 1 Recall that when the built-in function open() is called to open a file for reading, but it doesn’t exist, an
exception is raised. However, if the file exists, a reference to the opened file object is returned.
Write a function
safeOpen() that takes one parameter,
filename — a string giving the pathname of the file
to be opened for reading. When
safeOpen() is used to open a file, a reference to the opened file object
should be returned if no exception is raised, just like for the
open() function. If an exception is raised
while trying to open the file,
safeOpen() should return the value None.
For example, assuming the file
ghost.txt doesn’t exist, the following is correct output:
>>> # open()
>>> print(open('ghost.txt'))
Traceback (most recent call last):
File "<pyshell#8>", line 1, in <module>
print(open('ghost.txt'))
FileNotFoundError: [Errno 2] No such file or directory: 'ghost.txt'
>>>
>>> # safeOpen()
>>> inputFile = safeOpen('ghost.txt')
>>> print(inputFile)
None
>>>
'''


def safeOpen(fileName):
    '''  Function that takes a file name and returns the file object if it exists else it returns None'''
    try:
        return open(fileName)
    except FileNotFoundError:
        return None


# test cases
print(safeOpen('ghost.txt'))
