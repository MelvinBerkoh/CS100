# creating list
pets = ['ant', 'bat', 'cat', 'dog', 'fish']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
mixedList = [1.1, 2, 'hello', 4, 'a' == 'A']
print(type(numbers))

# List 1st is a lost of prices for a pair of boots at different online retailers
lst = [99.00, 56.00, 24.00, 78.90, 12.99]
# added 10 to the list
lst.append(160.0)
# how many times foes 160 appear in the list
print(lst.count(160))

# find the min value in list
minPrice = min(lst)

# find the index of the minimum price
print(lst.index(minPrice))

# remove the minium price form the list
lst.remove(minPrice)
print(lst)

# sort the list in increasing order
lst.sort()
print(lst)

# tuples are not mutable
tp1 = (1, 2, 2, 3, 3, 4)
tp1.count(2)
print(tp1)
