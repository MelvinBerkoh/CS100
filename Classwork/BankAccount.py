import random


class UserAccount:
    ''' holds the user info for the or object created'''
    bankName = "Bank Of America"

    def __init__(self, firstName, lastName, ssn, phoneNumber, email):
        self.firstName = firstName
        self.lastName = lastName
        self.ssn = int(ssn)
        self.phoneNumber = int(phoneNumber)
        self.email = email
        self.id = ''
        # gets 7 numbers between 0 and 30
        randomList = random.sample(range(0, 30), 7)
        # should loop through the list of random numbers and set it equal to the self.id
        for num in randomList:
            self.id += str(num)

    def getName(self):
        ''' Returns user's First and Last name'''
        return "User ID: " + self.id + "name is " + self.firstName + " " + self.lastName

    def getSSN(self):
        ''' Returns user's social security number '''
        return "User ID: " + self.id + "SSN: " + str(self.ssn)

    def getPhoneNumber(self):
        ''' Returns user's phone number'''
        return "User ID: " + self.id + "Phone Number: " + str(self.phoneNumber)

    def getEmail(self):
        ''' Returns user's email address'''
        return "User ID: " + self.id + "Email: " + self.email

    def getBankName(self):
        ''' returns the Bank Name'''
        return "User ID: " + self.id + "Bank Name: " + self.bankName

    def getID(self):
        ''' returns the User ID of the customer '''
        return "User ID: " + self.id


# create a class that inherits from the UserAccount class
class Account(UserAccount):
    ''' Each user has their own bank account information'''

    def __init__(self, firstName, lastName, ssn, phoneNumber, email):
        super().__init__(firstName, lastName, ssn, phoneNumber, email)
        self.balance = 0

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        if type(amount) == int and type(amount) == float:

            if amount > self.balance:
                message = 'Error : You dont have enough funds to withdraw $', str(
                    amount)
            else:
                self.balance -= amount
                message = 'You have successfully withdrew $' + \
                    str(amount) + 'Current balance : $ ' + str(self.balance)
            return message
        else:
            return 'Error you need to use a integer or float'

    def deposit(self, amount):
        if type(amount) == int and type(amount) == float:
            self.balance += amount
            return 'You have successfully deposited  $' + str(amount) + 'Current balance : $ ' + str(self.balance)
        else:
            return 'Error you need to use a integer or float'
