# ===================================
#   Problem statement & information
# ===================================

# A group of five students enrolls in Statistics immediately after taking a Math aptitude test. Each student's Math aptitude test score, x, and Statistics course grade, y, can be expressed 
# as a list of (x,y) points. If a student scored an 80 on the Math aptitude test, what grade would we expect them to achieve in Statistics? Determine the equation of the best-fit line using 
# the least squares method, then compute and print the value of y when x=80.

# Difficulty: Easy
# Max Score: 30
# Language: Python

# ===================================
#              Solution
# ===================================

# ===================================
#             Method 1
# ===================================

#!/bin/python3

def mean(array):
    return sum(array) / len(array)

def stdDev(array):
    var = sum((x - mean(array)) ** 2 for x in array) / len(array)
    return var ** 0.5
    
def Pcorr(num, setX, setY):
    sdX, sdY = stdDev(setX), stdDev(setY)
    xm, ym = mean(setX), mean(setY)
    cov = sum((i-xm)*(j-ym) for i, j in zip(setX, setY))/(num*sdX*sdY)
    return cov
    
def coeff_b(num, setX, setY):
    return Pcorr(num, setX, setY)* stdDev(setY) / stdDev(setX)
    
def coeff_a(num, setX, setY):
    return mean(setY) - coeff_b(num, setX, setY) * mean(setX)
    
def least_square(num, setX, setY, score):
    return coeff_a(num, setX, setY) + coeff_b(num, setX, setY) * score
    
if __name__ == '__main__':
    
    X, Y = [], []
    
    for k in range(5):
        left, right = list(map(int, input().split()))
        X.append(left)
        Y.append(right)
    
    print(round(least_square(5, X, Y, 80), 3))

# ===================================
#             Method 2
# ===================================

#!/bin/python3

def mean(array):
    return sum(array) / len(array)
        
def coeff_b(num, setX, setY):
    num_coeff = (num * sum(i*j for i, j in zip(setX, setY)) - (sum(setX) * sum(setY)))
    den_coeff = (num * sum(i ** 2 for i in setX) - sum(setX) * sum(setX))
    return num_coeff / den_coeff
    
def coeff_a(num, setX, setY):
    return mean(setY) - coeff_b(num, setX, setY) * mean(setX)
    
def least_square(num, setX, setY, score):
    return coeff_a(num, setX, setY) + coeff_b(num, setX, setY) * score
    
if __name__ == '__main__':
    
    X, Y = [], []
    
    for k in range(5):
        left, right = list(map(int, input().split()))
        X.append(left)
        Y.append(right)
    
    print(round(least_square(5, X, Y, 80), 3))

