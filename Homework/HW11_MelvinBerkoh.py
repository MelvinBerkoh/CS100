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
        ''' The method
teach should add a passed string parameter to
tricks and print a message that the dog knows the trick'''
        self.tricks.append(trick)
        message = self.name + ' knows ' + trick
        return message

    def knows(self, trickKnows):
        if trickKnows in self.tricks:
            message = 'Yes, ' + self.name + ' knows ' + trickKnows
            return message + '\n True'
        else:
            message = 'No, ' + self.name + ' doesn\'t know ' + trickKnows
            return message + '\n False'


'''
Problem 5
Create a class attribute
species of type
str to be shared by all instances of the class
Dog and set its value to
'canis familiaris'. The class attribute
species should be defined within the class
Dog but outside of any
method.
>>> dog.Dog.species
'Canis familiaris'
>>> sugar.species
'Canis familiaris'

'''
