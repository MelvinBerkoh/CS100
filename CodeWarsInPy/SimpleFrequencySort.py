# In this kata, you will sort elements in an array by decreasing frequency of elements. If two elements have the same frequency, sort them by increasing value.

def highestFreq(arr):
    highestFrequency = ''
    counter = 0
    newList = []
    for letter in arr:
        if arr.count(letter) > counter:
            highestFrequency = letter
            counter = arr.count(letter)
    return highestFrequency


print(highestFreq('aahhbbbbyyyyyyy'))
