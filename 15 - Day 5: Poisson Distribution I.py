# ===================================
#   Problem statement & information
# ===================================

# A random variable, X, follows Poisson distribution with mean of 2.5. Find the probability with which the random variable X is equal to 5.

# Difficulty: Easy
# Max Score: 30
# Language: Python

# ===================================
#              Solution
# ===================================

#!/bin/python3

import math

def Poisson(num_avg, num_succ):
    prob = num_avg ** num_succ * math.exp(-num_avg) / math.factorial(num_succ)
    return prob

if __name__ == '__main__':
    
    mean = float(input().strip())
    
    value = int(input().strip())
    
    print(round(Poisson(mean, value), 3))
