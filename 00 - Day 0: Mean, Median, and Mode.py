# ===================================
#   Problem statement & information
# ===================================

# Given an array X,of N integers, calculate and print the respective mean, median, and mode on separate lines. If your array contains more than one modal value, 
# choose the numerically smallest one.
#
# Note: Other than the modal value (which will always be an integer), your answers should be in decimal form, rounded to a scale of 1 decimal place.

# Difficulty: Easy
# Max Score: 30
# Language: Python

# ===================================
#              Solution
# ===================================

#!/bin/python3

def mean(array):
    c = sum(i for i in array)/len(array)
    return c
        
def median(array):
    array.sort()
    if len(array)% 2 != 0:
        c = array[(len(array) + 1) // 2]
        return c
    else:
        c = (array[len(array) // 2 - 1]+ array[len(array) // 2]) / 2
        return c

def mode(array):
    a = {}
    for k in array:
        if k not in a:
            a[k] = 1
        else:
            a[k] += 1
    max_count = max(a.values())
    mode = [g for g, count in a.items() if count == max_count]
    if len(a) > 2:
        return min(mode)
    else:
        return mode
        
    
if __name__ == "__main__":
    
    size = int(input())

    a = list(map(int, input().split()))
    
    print(mean(a))

    print(median(a))

    print(mode(a))
