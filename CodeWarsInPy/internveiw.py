# Programming challenge description:
# You are given a list of numbers which is supplemented with positions that have to be swapped.
# Input:
# Your program should read lines from standard input. Each line contains a list of space-delimited numbers, followed by a colon, followed by the indexes to be swapped. The first position in the list is at index 0. If there is more than one pair of indexes to be swapped, process each pair in the order they appear in the input, left to right.
import sys
# import numpy as np
# import pandas as pd
# from sklearn import ...


def swapNums(numbers, pairsToSwap):
    for pair in pairsToSwap:
        switch1, switch2 = map(int, pair.split('-'))
        numbers[switch1], numbers[switch2] = numbers[switch2], numbers[switch1]
    return numbers


try:
    while True:
        # read the input
        line = input().strip()
        # break them up
        givenNums, numbersToSwap = line.split(':')
        nums = list(map(int, givenNums.split()))
        pairsToSwap = numbersToSwap.split(',')

        # Swap elements and print the result
        result = swapNums(nums, pairsToSwap)
        for item in result:
            print(item, end=' ')
        print()

except EOFError:
    pass
