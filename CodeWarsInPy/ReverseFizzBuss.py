'''
FizzBuzz is often one of the first programming puzzles people learn. Now undo it with reverse FizzBuzz!

Write a function that accepts a string, which will always be a valid section of FizzBuzz. 
Your function must return an array that contains the numbers in order to generate the given section of FizzBuzz.

Notes:

If the sequence can appear multiple times within FizzBuzz, return the numbers that generate the first instance of that sequence.
All numbers in the sequence will be greater than zero.
You will never receive an empty sequence.

'''

'''
test case 
reverse_fizzbuzz("1 2 Fizz 4 Buzz")        -->  [1, 2, 3, 4, 5]
reverse_fizzbuzz("Fizz 688 689 FizzBuzz")  -->  [687, 688, 689, 690]
reverse_fizzbuzz("Fizz Buzz")              -->  [9, 10]
'''

# note that the fizz is anything divisble by 3 and buzz is anything that is divisble by 5


def reverse_fizzbuzz(str):

  # split the passed parameter in to an array separating it by space for each word or number in it
    array = str.split()
    # hold the results to return
    result = []

    # loop through the array by index
    for i in range(len(array)):
      # now we check for the key words
        if array[i] == 'Fizz':
            result.append(int(array[i-1])+1)

        elif arrry[i] == 'Buzz':

        elif array[i] == 'FizzBuzz':

        else:
            result.append(array[i])

    return result


reverse_fizzbuzz('hell this this work')
