'''

'''


'''
Problem 1
'''


def file_copy(in_file, out_file):
    '''
    Takes two string parameters (in_file and out_file) and copies the content of
    in_file into out_file. NOTE: Function doesn't return anything so the return type is none
    '''
    file1 = open(in_file, 'r')  # opens file as saves it as file 1
    output = ''  # string to hold the data from file1

    # loop through the file by line and copy the contents into the output variable
    for line in file1:
        output += str(line)

    file1.close()
    file2 = open(out_file, 'w')  # open second file for writing
    file2.write(output)    # append the data
    file2.close()


print(file_copy('Homework/test.txt', 'Homework/output.txt'))   # test case

'''
Problem 2
'''


def file_stats(in_file):
    '''
    Function takes one string parameter (in_file) that is the name of an existing text file. The function
    file_stats should calculate three statistics about in_file: the number of lines it contains, the number of words and the number of characters,
    and print the three statistics on separate lines
    '''
    file1 = open(in_file, 'r')                            # open the file

    # read method reads the whole file and returns a string version of it
    readFile = file1.read()

    # to calc the number of characters it would be the length of that variable (readFile)
    numberOfChar = len(readFile)

    # since strings are immutable you can use this logic to get the number of lines by splitting by the newline character
    numberOfLines = len(readFile.split('\n'))

    # again immutable so can use the same logic this time splitting by the space
    numberOfWords = len(readFile.split(' '))

    finalStr = 'The number of words in the given file : ' + \
        str(numberOfWords)+'\n' + 'The number of characters in the given file: ' + \
        str(numberOfChar)+'\n' + \
        'The number of lines in the given file: ' + str(numberOfLines)
    return finalStr


print(file_stats('Homework/test.txt'))  # test case

'''
Problem 3
Write a function named
repeat_words that takes two string parameters:
1.
in_file: the name of an input file that exists before
repeat_words is called
2.
out_file: the name of an output file that
repeat_words creates
Assume that the input file is in the current working directory and write the output file to that directory.
For each line of the input file, the function
repeat_words should write to the output file all of the words
that appear more than once on that line. Each word should be lower cased and stripped of leading and
trailing punctuation. Each repeated word on a line should be written to the corresponding line of the
output file only once, regardless of the number of times the word is repeated.
For example, if the following is the content of the file
catInTheHat.txt:
Too wet to go out and too cold to play ball.
So we sat in the house.
We did nothing at all.
So all we could do was to Sit! Sit! Sit! Sit!
The following function call:
inF = 'catInTheHat.txt'
outF = 'catRepWords.txt'
repeat_words(inF, outF)
should create the file
catRepWords.txt with the content:
too to
sit
Hint: Be sure to test your solution with input in which some repeated words on a line are a mixture of upper
and lower case, and in which repeated words sometimes are preceded or followed by punctuation
'''


def repeat_words(in_file, out_file):
    file1 = in_file.open('r')
    lst = file1.readlines()
    
    for item in lst:
     highestCount = 0
     
     for word in item:
       if word.count() > highestCount:
         highestCount = word.count()
         mostFrequentWord = word
         
        
