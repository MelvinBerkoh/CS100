'''
Melvin Berkoh
CS 100 Section 002
HW 11 April 11, 2024
'''
'''
Problem 1
Write a class definition line and a one line docstring for the class
Dog. Write an __init__ method for the class Dog that gives each dog its own
name and breed. Test this on a successful creation of a Dog object.
>>> import dog
>>> sugar = dog.Dog('Sugar', 'border collie')
>>> sugar.name
'Sugar'
>>> sugar.breed
'border collie'
'''


class Dog:
    '''
    Dog gives each dog its own name and breed
    '''

# this is the constructor for a python class
# self parameter
    def __init__(self, name, breed, tricks):
        self.name = name
        self.breed = breed
        self.tricks = list(tricks)

    def teach(self, trick):
        self.tricks.append(trick)
        message = self.name + ' knows ' + trick
        return message


'''
Problem 2
Add a data attribute
tricks of type
list to each
Dog instance and initialize it in
__init__ to the empty list. The
user does not have to supply a list of tricks when constructing a
Dog instance. Make sure that you test this
successfully.
>>> sugar.tricks
[]
'''
'''
Write a method
teach as part of the class
Dog. The method
teach should add a passed string parameter to
tricks and print a message that the dog knows the trick.
>>> sugar.teach('frisbee')
Sugar knows frisbee

'''
