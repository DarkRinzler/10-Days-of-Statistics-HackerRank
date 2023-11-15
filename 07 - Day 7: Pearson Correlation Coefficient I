# ===================================
#   Problem statement & information
# ===================================

# Given two -element data sets, X and Y, calculate the value of the Pearson correlation coefficient.

# Difficulty: Easy
# Max Score: 30
# Language: Python

# ===================================
#              Solution
# ===================================

#!/bin/python3

def stdDev(array):
    s = sum((i - sum(array) / len(array)) **2 for i in array) / len(array)
    return s ** 0.5
    
def mean(array):
    c = sum(array)/len(array)
    return c

def Pcorr(num, setX, setY):
    sdX, sdY = stdDev(setX), stdDev(setY)
    xm, ym = mean(setX), mean(setY)
    cov = sum((i-xm)*(j-ym) for i, j in zip(setX, setY))
    return cov/(num*sdX*sdY)
    
if __name__ == '__main__':
    
    n = int(input().strip())
    
    X = list(map(float, input().strip().split()))
    Y = list(map(float, input().strip().split()))
    
    print(round(Pcorr(n, X, Y), 3))
