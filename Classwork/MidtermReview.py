'''
This is a testing file for midterm questions 
'''


def myFunction(rows, cols):
    result = 0
    for i in range(rows):
        for j in range(cols):
            result += j
    return result


print(myFunction(3, 4))
