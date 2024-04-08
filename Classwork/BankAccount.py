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

        # class Account:
        #     # hold id
        #     # blaance
        #     # customerName
        #     # funtions would be withdraw
        #     # desposit
        #     # getBalance
