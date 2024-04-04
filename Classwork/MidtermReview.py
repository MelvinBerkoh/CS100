'''
This is a testing file for midterm questions 
'''


def myFunction(numList):
    for row in numList:
        counter = 0
        for num in row:
            counter += 1
            if num == 0 and counter != 2:

                break
            print(num, end=' ')
        print()


table = [
    [2, 3, 0, 6],
    [0, 3, 4, 5],
    [4, 5, 6, 0]]

myFunction(table)
