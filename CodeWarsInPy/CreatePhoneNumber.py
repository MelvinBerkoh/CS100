# Question link from code wars https://www.codewars.com/kata/525f50e3b73515a6db000b83/python
# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
def create_phone_number(lst):
    string = '({}) {}-{}'
    temp = ''
    for num in lst:
        temp += str(num)
    string = string.format(temp[0:3], temp[3:6], temp[6:10])
    return string


# test cases
print(create_phone_number([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))
print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
