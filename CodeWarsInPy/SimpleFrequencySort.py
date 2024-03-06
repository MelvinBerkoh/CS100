# In this kata, you will sort elements in an array by decreasing frequency of elements. If two elements have the same frequency, sort them by increasing value.

def highestFreq(arr):
    highestFrequency = ''
    counter = 0
    newList = []
    for num in arr:
        if arr.count(num) > counter:
            highestFrequency = num
            counter = arr.count(num)
        arr.remove(num)
    newList.append(highestFrequency)
    return newList


print(highestFreq([2, 3, 5, 3, 7, 9, 5, 3, 7]))
