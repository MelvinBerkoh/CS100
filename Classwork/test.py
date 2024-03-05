a = 'apple'

b = 'banana'

c = b[0] + a[-1] + b[3:5]

print(c)

lst = ['M', 'a', 'r', 'c', 'h']
vowels = 'aeiouAEIOU'
c = []

for letter in range(len(lst)):
    if str(letter) in vowels:
        c.append(letter)

print(c)
