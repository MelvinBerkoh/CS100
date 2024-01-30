
'''
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.
'''


def sum_array(arr):
    # first want to take the array and look for the min and max number
    minNum = min(arr)
    maxNum = max(arr)
    # remove the max and min numbers from the list
    arr.remove(minNum)
    arr.remove(maxNum)

    # use the built in function to add all the values remaining in the list
    return sum(arr)


print(sum_array([1, 2, 3, 3, 4, 5]))
