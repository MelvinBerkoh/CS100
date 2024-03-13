# In this kata, you will sort elements in an array by decreasing frequency of elements. If two elements have the same frequency, sort them by increasing value.
# loop through arr and make sure its not in the created new list
# as we are looping through the array we want to find the the number that appears the most
# with that highest frequecny number we want to add that to the new list as the count of that number
# reapeat for all elements in the list
def highestFreq(arr):
    highestCount = ''
    counter = 0
  #  list to hold the result
    newList = []
    # list so that we dont loop twice
    accountForNumber = []
    # loop through all the elments of the array/list
    for num in arr:
        if num not in accountForNumber:
            accountForNumber.append(num)
        # get the count of each element in list
            frequency = arr.count(num)
            # determine the number with the highest count
            for i in range(frequency):
                # add that count to the new list
                newList.append(num)
            # sort list in decreasing order
    newList.sort(reverse=True)

    return newList


print(highestFreq([2, 3, 5, 3, 7, 9, 5, 3, 7]))
