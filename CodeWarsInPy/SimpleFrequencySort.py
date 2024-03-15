# In this kata, you will sort elements in an array by decreasing frequency of elements. If two elements have the same frequency, sort them by increasing value.
import collections


def highestFreq(arr):
    value = collections.Counter(arr)
    arr.sort(key=lambda x: (-value[x], x))
    return arr


print(highestFreq([2, 3, 5, 3, 7, 9, 5, 3, 7]))
1+2
