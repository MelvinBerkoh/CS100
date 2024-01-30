s1 = 'good'
s2 = 'bad'
s3 = 'silly'

# ll appers in s3
print('ll' in s3)
# blank space doesnt not appear in s1
print(' ' in s1)
# the concatenation of s1, s2 and s3
s4 = s1+s2+s3
print(s4)
#  blank space appears in the concatenation of s1,s2,s3
print(' ' in s4)
#  the concatention of 10 copies of s3
s5 = s3*10

# the total number of characters in the concatenation of s1, s2, and s3

print(len(s4))
