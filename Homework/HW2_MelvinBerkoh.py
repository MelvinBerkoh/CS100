'''
Melvin Berkoh
CS 100 Section 002
HW 02, February 01, 2024

'''

'''
This question practices the use of a list method. Assign to the variable grades a list of 10 letter grades
from among 'A', 'B', 'C', 'D', and 'F'. For example:
grades = ['A', 'F', 'C', 'F', 'A', 'B', 'A', 'C', 'A', 'B']
Write a Python expression that creates a list named frequency, in which the elements are the number
of times each of the letters A, B, C, D and F appear in grades. For example, for the above value of
grades, the following would be correct output:
frequency = [4, 2, 2, 0, 2]
Your expression must give the correct values for any list of grades, not just the one in your list. Hint:
use the list method count.
'''
# create initial list of grades
grades = ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'F']
# create empty list the hold times shown up
frequency = []
# create variables to hold the count of each grade
amountOfA = grades.count('A')
amountOfB = grades.count('B')
amountOfC = grades.count('C')
amountOfD = grades.count('D')
amountOfF = grades.count('F')

# add all of the values to the new list would prefer to use a loop but I cant at this moment
frequency.append(amountOfA)
frequency.append(amountOfB)
frequency.append(amountOfC)
frequency.append(amountOfD)
frequency.append(amountOfF)

# display the results
print(frequency)
'''
2. This question practices list membership, list indexes and list slices.
a. Write a Python statement that creates a list named dog_breeds that contains the elements
'collie', 'sheepdog', 'Chow', and 'Chihuahua' in the order given.
b. Write a Python statement that uses list slicing to create a list herding_dogs that is made up of
the first two elements of dog_breeds.
c. Write a Python statement that uses list indexing to create a list tiny_dogs that is made up of
the last element of dog_breeds.
d. Write a Python statement that tests whether 'Persian' is in the list dog_breeds and prints
either True or False depending on the answer.
'''
# Write a Python statement that creates a list named dog_breeds that contains the elements
# 'collie', 'sheepdog', 'Chow', and 'Chihuahua' in the order given.
dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuahua']

# Write a Python statement that uses list slicing to create a list herding_dogs that is made up of
# the first two elements of dog_breeds.
herding_dogs = dog_breeds[0: 1] + dog_breeds[1: 2]

print(herding_dogs)

# Write a Python statement that uses list indexing to create a list tiny_dogs that is made up of
# the last element of dog_breeds.
tiny_dogs = []
tiny_dogs.append(dog_breeds[-1])
print(tiny_dogs)

# Write a Python statement that tests whether 'Persian' is in the list dog_breeds and prints
# either True or False depending on the answer.
# type casting the count of persian in the list dog breeds to a boolean. This could only work in one case since im not allowed to use if statements yet
boolean = bool(dog_breeds.count('Persian'))
print(boolean)
