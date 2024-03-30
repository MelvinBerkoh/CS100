'''
Melvin Berkoh
CS 100 Section 002
HW 08, March 07, 2024
'''
import string


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
'''


def repeat_words(in_file, out_file):
    '''
    For each line of the input file, the function repeat_words should write to the output file all of the words
    that appear more than once on that line. Each word should be lower cased and stripped of leading and
    trailing punctuation. Each repeated word on a line should be written to the corresponding line of the
    output file only once, regardless of the number of times the word is repeated.
    '''
    # Open input file for reading
    file1 = open(in_file, 'r')
    lines = file1.readlines()

    # Open output file for writing
    file2 = open(out_file, 'w')
    # Iterate over each line in the input file
    for line in lines:
        line = line.lower().strip()  # Convert to lowercase and remove leading/trailing spaces
        line = line.translate(str.maketrans(
            '', '', string.punctuation))  # Remove punctuation
        words = line.split()  # Split the line into words

        # Create a list to store repeated words in the current line
        repeated_words = []
        # Iterate over each word in the line
        for word in words:
            # Check if the word is repeated and not already written to output file
            if words.count(word) > 1 and word not in repeated_words:
             # Write the repeated word to output file
                file2.write(word + ' ')
            # Add the word to the list of repeated words
                repeated_words.append(word)
                # Write newline to separate lines in output file
                file2.write('\n')

    file1.close()
    file2.close()


# test case
print(repeat_words('Homework/test.txt', 'Homework/output.txt'))
