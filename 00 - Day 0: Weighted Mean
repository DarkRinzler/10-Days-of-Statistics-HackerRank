# ===================================
#   Problem statement & information
# ===================================

# Given an array X, of N integers and an array W, representing the respective weights of 's elements, calculate and print the weighted mean of 's elements. 
#
# Your answer should be rounded to a scale of 1 decimal place (i.e., 12.3 format).

# Difficulty: Easy
# Max Score: 30
# Language: Python

# ===================================
#              Solution
# ===================================

#!/bin/python3

def weightedMean(X, W):
    s1 = sum(i*j for i, j in zip(X, W))
    s2 = sum(i for i in W)
    return print(round(s1/s2, 1))
if __name__ == '__main__':

    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
