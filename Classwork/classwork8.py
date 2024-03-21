def lineStats(inFile, outFile):
    ''' The function should read the input file line by line and write to the output file for each corresponding line
    two statistics separated by space, the number of characters in the line and the number of words in the line
    '''
    file1 = open(inFile, 'r')
    for line in file1:
        numOfCharacters = len(line)
        numOfWords = str(len(line.split()))
        print(numOfCharacters)
    file1.close()
    stats = 'The number of characters is: ' + str(numOfCharacters) + \
        '\n' + 'The number of words is: ' + numOfWords
    file2 = open(outFile, 'w')
    file2.write(stats)
    print(file2)
    file2.close()


lineStats('Classwork/test.txt', 'Classwork/stats.txt')
