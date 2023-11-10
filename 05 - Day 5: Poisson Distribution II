# ===================================
#   Problem statement & information
# ===================================

# The manager of a industrial plant is planning to buy a machine of either type A or type B. For each day’s operation:
# • The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88. The daily cost of operating  is C_A = 160 + 40 * X^2.
# • The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55. The daily cost of operating  is C_B = 128 + 40 * Y^2.
# Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure that they operate like new at the start of each day. Find and print 
# the expected daily cost for each machine.

# Difficulty: Easy
# Max Score: 30
# Language: Python

# ===================================
#              Solution
# ===================================

#!/bin/python3

if __name__ == '__main__':
    
    avg_X, avg_Y = list(map(float, input().strip().split()))
    
    Cost_A = 160 + 40 * (avg_X + avg_X ** 2)
    
    Cost_B = 128 + 40 * (avg_Y + avg_Y ** 2)
    
    print(round(Cost_A, 3))
    
    print(round(Cost_B, 3))
