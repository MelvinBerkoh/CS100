'''
Melvin Berkoh
CS 100 Section 002
HW 11 April 11, 2024
'''


class Dog:
    '''
    Dog gives each dog its own name, breed, and trick
    '''
    species = 'Canis familiaris'
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
        '''The method knows should check if the passed parameter is in the tricks list. 
        If found will return a message with True or False '''
        if trickKnows in self.tricks:
            message = 'Yes, ' + self.name + ' knows ' + trickKnows
            return message + '\n True'
        else:
            message = 'No, ' + self.name + ' doesn\'t know ' + trickKnows
            return message + '\n False'
