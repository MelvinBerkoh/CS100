'''
Melvin Berkoh
CS 100 Section 002
HW 05, February 15, 2024
'''
'''
Create a list named months of the months of the year. Write a for loop that iterates over the elements
of months and prints out each one that begins with letter 'J', one month per line.

3. Consider the strings created by these assignment statements:
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"
Write a for loop that prints out all the vowels in
horton in the order they appear in
horton.


'''
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
for month in months:
    if month[0].lower() == 'j':
        print(month)

# 2. Write a for loop that iterates over all of the integers in the range 0 through 99, inclusive, and prints
# out all of those numbers that are divisible by both 2 and 5.
for number in range(100):
    if ((number % 2) == 0) and ((number % 5) == 0):
        print(number)
