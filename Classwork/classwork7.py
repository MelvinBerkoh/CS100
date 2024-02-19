
'''
Define a function named isPassingScore that takes two inputs, the passing score and the
student exam score. The function returns True if the student score is the same or better than
the passing score. If student’s score is below passing score the function returns False.
'''


def isPassingScore(passingScore, studentScore):
    '''function that returns True if the student score is the same or better than the passing score. If student’s score is below passing score the function returns False.'''
    if studentScore >= passingScore:
        return True
    else:
        return False


'''
2. Define a function named totalPassingScores that takes as input a passing score and a list of
student scores. The function calculates and returns the total number of passing scores.
Hint – use for loop and the function defined in #1 to validate each score.
'''


def totalPassingScores(passingScore, studentScores):
    '''function that calculates and returns the total number of passing scores.'''
    totalPassingScores = 0
    for score in studentScores:
        if isPassingScore(passingScore, score):
            totalPassingScores += 1
    return totalPassingScores


'''
3. Define a function named getMinValue that  Hint – use for loop and if statements
'''


def getMinValue(nums):
    ''' takes a list of numbers as input and returns the minimum value from the list'''
    nums.sort()
    return nums[0]

