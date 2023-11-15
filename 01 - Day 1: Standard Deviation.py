# ===================================
#   Problem statement & information
# ===================================

# Given an array arr, of n integers, calculate and print the standard deviation. Your answer should be in decimal form, rounded to a scale of 1 decimal place.
#
# An error margin of ±0.1 will be tolerated for the standard deviation.

# Difficulty: Easy
# Max Score: 30
# Language: Python

# ===================================
#              Solution
# ===================================

#!/bin/python3

def stdDev(arr):
    s = sum((k - sum(arr) / len(arr)) **2 for k in arr) / len(arr)
    return print(round(s ** 0.5, 1))
    
if __name__ == '__main__':
    
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
