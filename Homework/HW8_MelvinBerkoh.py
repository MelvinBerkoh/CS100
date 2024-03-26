'''
Melvin Berkoh
CS 100 Section 002
HW 08, March 07, 2024
'''

'''
This problem provides practice using a while True loop.
Write a function named twoWords that gets and returns two words from a user. The first word is of a
specified length, and the second word begins with a specified letter.
The function twoWords takes two parameters:
1. an integer, length, that is the length of the first word and
2. a character, firstLetter, that is the first letter of the second word. The second word may begin with
either an upper or lower case instance of firstLetter.
The function twoWords should return the two words in a list. Use a while True loop and a break statement
in the implementation of twoWords.
The following is an example of the execution of twoWords:
print(twoWords(4, 'B'))
Enter a 4-letter word please: two
Enter a 4-letter word please: one
Enter a 4-letter word please: four
Enter a word beginning with B please: apple
Enter a word beginning with B please: pear
Enter a word beginning with B please: banana
['four', 'banana']

'''


def twoWords(number, letter):
    result = []
    # make sure to edit this before submitting due to not using breaks
    # ask user question cast number to str and keep letter as string
    question1 = input('Enter a '+str(number)+'-letter word please: ')
    while (True):
        if (len(question1) != number):
            question1 = input('Enter a '+str(number)+'-letter word please: ')
        else:
            break
    result.append(question1)
    question2 = input('Enter a word beginning with ' + letter + ' please: ')
    while (True):
        if ((question2[0] != letter) and (question2[0] != letter.lower())):
            question2 = input(
                'Enter a word beginning with ' + letter+' please: ')
        else:
            break
    result.append(question2)
    return result


# print(twoWords(4, 'B'))


# Problem 2
'''
Write a function named twoWordsV2 that has the same specification as Problem 1, but implement it
using while and not using break. (Hint: provide a different boolean condition for while.)
Since only the implementation has changed, and not the specification, for a given input the output should
be identical to the output in Problem 1
'''


def twoWordsV2(number, letter):
    result = []

    # ask user question cast number to str and keep letter as string
    question1 = input('Enter a '+str(number)+'-letter word please: ')
    while (len(question1) != number):

        question1 = input('Enter a '+str(number)+'-letter word please: ')

    result.append(question1)

    question2 = input('Enter a word beginning with ' + letter + ' please: ')
    while ((question2[0] != letter) and (question2[0] != letter.lower())):
        question2 = input('Enter a word beginning with ' + letter+' please: ')

    result.append(question2)
    return result


# print(twoWordsV2(4, 'B'))

# problem 3
'''
Write a function named enterNewPassword. This function takes no parameters. It prompts the user to
enter a password until the entered password has 8-15 characters, including at least one digit. Tell the
user whenever a password fails one or both of these tests.
'''


def enterNewPassword():
    password = input(
        'Please enter a password that has 8-15 characters, including at least one digit: ')
    # what we want is to first compare the length of the password to make sure its withe range

    while (True):
        # if the password entered is not within the given range repeat the prompt
        if ((len(password) < 8) or (len(password) > 15)):
            print('The password you entered is not between 8-15 characters :(')
            password = input(
                'Please enter a password that has 8-15 characters, including at least one digit: ')
            continue  # Restart the loop if the password is not within the range
    # Check for the presence of at least one digit
        digit = any(char.isdigit() for char in password)
        if not digit:
            print('The password you entered does not contain a digit :(')
            password = input(
                'Please enter a password that has 8-15 characters, including at least one digit: ')
            continue  # Restart the loop if there is no digit in the password
        # If both conditions are met, password is accepted
        print('Password accepted!')
        break  # Exit the loop since the password is accepted


# enterNewPassword()
'''
Implement the GuessNumber game. In this game, the computer
• Think of a random number in the range 0-50. (Hint: use the random module.)
• Repeatedly prompt the user to guess the mystery number.
• If the guess is correct, congratulate the user for winning. If the guess is incorrect, let the user know if
the guess is too high or too low.
• After 5 incorrect guesses, tell the user the right answer.
The following is an example of correct input and output.
I'm thinking of a number in the range 0-50. You have five tries to guess it.
Guess 1? 32
32 is too high
Guess 2? 18
18 is too low
Guess 3? 24
You are right! I was thinking of 24!

'''


def guessNumber(num):
    print(
        'I am thinking of a number in the range 0-50. You have five tries to guess it.')
    counter = 0
    while (counter < 5):
        counter += 1
        guess = input('Guess '+str(counter) + '?')
        if (num > int(guess)):
            print(guess + ' is too low')
        elif (num < int(guess)):
            print(guess + ' is too high')
        else:
            print('You are right! I was thinking of ' + guess + '!')
            break


# testCases
guessNumber(-24)
print(guessNumber(10))
print(guessNumber(30))
