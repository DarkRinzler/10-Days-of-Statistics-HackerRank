# ===================================
#   Problem statement & information
# ===================================

# The interquartile range of an array is the difference between its first (Q_1) and third (Q_3) quartiles (i.e., Q_3-Q_1).
# Given an array, values, of n integers and an array, freqs, representing the respective frequencies of value's elements, construct a data set, S, where 
# each values[i] occurs at frequency freqs[i]. Then calculate and print S's interquartile range, rounded to a scale of 1 decimal place (i.e., 12.3 format).
#
# Tip: Be careful to not use integer division when averaging the middle two elements for a data set with an even number of elements, and be sure to not 
# include the median in your upper and lower data sets.

# Difficulty: Easy
# Max Score: 30
# Language: Python

# ===================================
#              Solution
# ===================================

#!/bin/python3

def median(arr):
    if len(arr) % 2 != 0:
        med = round(arr[len(arr) // 2], 1)
        return med
    else:
        med = round((arr[len(arr) // 2 -1] + arr[len(arr) // 2]) / 2, 1)
        return med

def quartiles(arr):
    Q1 = round(median(arr[: len(arr) // 2]), 1)
    Q2 = median(arr)
    if len(arr) % 2 != 0:
        Q3 = round(median(arr[len(arr) // 2 + 1:]), 1)
    else:
        Q3 = round(median(arr[len(arr) // 2:]), 1)
    return Q1, Q2, Q3

def interQuartile(values, freqs):
    new_val = []
    for k, i in zip(values, freqs):
        new_val.extend([k] * i)
    new_val.sort()
    print("{:.1f}".format(quartiles(new_val)[2]-quartiles(new_val)[0]))
    

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))
    
    interQuartile(val, freq)
