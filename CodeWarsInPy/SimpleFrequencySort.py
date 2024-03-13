# In this kata, you will sort elements in an array by decreasing frequency of elements. If two elements have the same frequency, sort them by increasing value.
# loop through arr and make sure its not in the created new list
# as we are looping through the array we want to find the the number that appears the most
# with that highest frequecny number we want to add that to the new list as the count of that number
# reapeat for all elements in the list
def highestFreq(arr):
    highestFrequency = ''
    counter = 0
    newList = []
    for num in arr:
    #     if num in newList:
    #         continue
    #     else:
    #         if arr.count(num) > counter:
    #             counter = arr.count(num)
    #             highestFrequency += str(num)
    # newList.append(highestFrequency)

    #     arr.remove(num)

    return newList


print(highestFreq([2, 3, 5, 3, 7, 9, 5, 3, 7]))
