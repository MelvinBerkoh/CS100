# Programming challenge description:
# You are given a list of numbers which is supplemented with positions that have to be swapped.
# Input:1 2 3 4 5 6 7 8 9  : 0-8
# Output : 9 2 3 4 5 6 7 8 1
# Your program should read lines from standard input. Each line contains a list of space-delimited numbers, followed by a colon, followed by the indexes to be swapped. The first position in the list is at index 0. If there is more than one pair of indexes to be swapped, process each pair in the order they appear in the input, left to right.
import sys

for line in sys.stdin:
   