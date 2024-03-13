# In this kata, you will sort elements in an array by decreasing frequency of elements. If two elements have the same frequency, sort them by increasing value.
# loop through arr and make sure its not in the created new list
# as we are looping through the array we want to find the the number that appears the most
# with that highest frequecny number we want to add that to the new list as the count of that number
# reapeat for all elements in the list
def highestFreq(arr):
    #  create dictionary to hold key as the number and count as the value
    counterDict = {}
    # return result
    sortedValues = []
    # loop through list 
    for num in arr:
      # if that number is account for add one to value
        if num in counterDict:
            counterDict[num] +=1
        else:
          # if number is not accounted for intialize the key and value
          counterDict[num] = 1
    c
print(highestFreq([2, 3, 5, 3, 7, 9, 5, 3, 7]))
