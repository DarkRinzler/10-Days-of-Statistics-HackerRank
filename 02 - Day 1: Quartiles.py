# ===================================
#   Problem statement & information
# ===================================

# Given an array arr, of n integers, calculate the respective first quartile (Q_1), second quartile (Q_2), and third quartile (Q_3). 
# It is guaranteed that Q_1, Q_2, and Q_3 are integers.

# Difficulty: Easy
# Max Score: 30
# Language: Python

# ===================================
#              Solution
# ===================================

#!/bin/python3

import os

def median(arr):
    if len(arr) % 2 != 0:
        med = arr[len(arr) // 2]
        return med
    else:
        med = (arr[len(arr) // 2 -1] + arr[len(arr) // 2]) / 2
        return med

def quartiles(arr):
    arr.sort()
    Q1 = int(median(arr[: len(arr) // 2]))
    Q2 = int(median(arr))
    if len(arr) % 2 != 0:
        Q3 = int(median(arr[len(arr) // 2 + 1 :]))
    else:
        Q3 = int(median(arr[len(arr) // 2 :]))
    return Q1, Q2, Q3
        
      
if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
