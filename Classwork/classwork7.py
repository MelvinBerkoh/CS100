import turtle
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
    nums.sort()     # this sorts the list in numerical order
    return nums[0]


# def getMinValue(nums):
#     ''' takes a list of numbers as input and returns the minimum value from the list'''
#     minValue = nums[0]
#     for number in nums:
#         if number < minValue:
#             minValue = number
#     return minValue
# test cases for getMinValue
print(getMinValue([13, 22, 37, 41, 5]))
print(getMinValue([50, 44, 32, 2, 10]))
print(getMinValue([10, 3, 24, 51, 4]))


'''
4. Define a function named drawPolygon that takes the following parameters:
a. t – turtle
b. numSides – number of sides for the regular polygon
c. sideLength – length of each side
It draws the polygon with the given parameters. Make no assumption about turtle state or
position. It should draw counterclockwise.
Hint – for a regular polygon with n sides, the exterior angle is 360/n
'''

myScreen = turtle.Screen()
myScreen.screensize(900, 900)
t = turtle.Turtle()


def drawPolygon(t, numSides, sideLength):
    '''It draws the polygon with the given parameters.'''
    for sides in range(numSides):
        if numSides >= 3:
            t.forward(sideLength)
            t.left(360 / numSides)
            sides = sides + 1
        else:
            message = "Number of sides must be greater than 2"
            return message
    t.reset()


# create test cases for drawPolygon
drawPolygon(t, 3, 100)
drawPolygon(t, 4, 100)
drawPolygon(t, 5, 100)
