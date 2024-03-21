def longestLnLine(inFile, outFile):
    ''' The function should read the input file line by line and write to the output file the longest line
    '''
    file1 = open(inFile, 'r')
    longestLine = ''
    for line in file1:
        if len(line) > len(longestLine):
            longestLine = line
    file1.close()
    file2 = open(outFile, 'w')
    file2.write(longestLine)
    file2.close()
    return longestLine


print(longestLnLine('Classwork/test.txt', 'Classwork/longestLine.txt'))
