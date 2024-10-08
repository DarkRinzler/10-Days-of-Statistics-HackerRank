# ===================================
#   Problem statement & information
# ===================================

# Andrea has a simple equation: Y = a + b_1*f_1+...+ b_m*f_m for (m+1) real constants (a,f_1,..,f_m). We can say that the value of Y depends on m features. Andrea studies this equation for n 
# different feature sets (f_1,f_2,f_3,..,f_m) and records each respective value of Y. If she has q new feature sets, can you help Andrea find the value of Y for each of the sets?

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

import numpy as np

def tran(matrix):
    return matrix.transpose()
    
def inv(matrix):
    return np.linalg.inv(matrix)
    
def prod(matrix_1, matrix_2):
    return np.dot(matrix_1, matrix_2)

def prod_all(matrix_1):
    return prod(inv(prod(tran(matrix_1), matrix_1)), tran(matrix_1))

def coeff(matrix_1, matrix_2):
    return prod(prod_all(matrix_1), matrix_2)
    
if __name__ == '__main__':
    
    columns, rows = list(map(int, input().split()))
    
    X = np.ones((rows, columns + 1))
    Y = np.zeros((rows, 1))
    
    for k in range(rows):
        entries = list(map(float, input().split()))
        X[k, 1:] = entries[:columns]
        Y[k] = entries[columns]
        
    result = int(input())
    
    for k in range(result):
        entries = list(map(float, input().split()))
        Z = np.insert(entries, 0, 1)
        print(round(prod(Z, coeff(X, Y))[0], 2))
    
