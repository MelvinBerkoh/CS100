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

# note that the fizz is anything divisible by 3 and buzz is anything that is divisible by 5


def reverse_fizzbuzz(str):

  # split the passed parameter in to an array separating it by space for each word or number in it
    array = str.split()
    # hold the results to return
    result = []

    # loop through the array by index
    for i in range(len(array)):
      # now we check for the key words
        if array[i] == 'Fizz':
          # now we want to check if there is a number before and after the word fizz

          # if the index is 0 and the next word following is buzz we know that we have to add 5 to the results array
            if i == 0 and array[i + 1] == 'Buzz':
                result.append(5)
            # if the index is 0 and the next word following is not buzz we know that we have to add 3 to the results array
            elif i == 0 and array[i + 1] != 'Buzz':
                result.append(3)
            # if there is a number before and after the word fizz we have to
    return result


print(reverse_fizzbuzz("1 2 Fizz 4 Buzz"))
