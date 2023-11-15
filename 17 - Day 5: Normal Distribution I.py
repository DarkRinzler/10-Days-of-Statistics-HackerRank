# ===================================
#   Problem statement & information
# ===================================

# In a certain plant, the time taken to assemble a car is a random variable, X, having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours. What is the 
# probability that a car can be assembled at this plant in:
# • Less than 19.5 hours?
# • Between 20 and 22 hours?

# Difficulty: Easy
# Max Score: 30
# Language: Python

# ===================================
#              Solution
# ===================================

#!/bin/python3

import math

def normal_cprob(value, avg, std):
    norm_cumul_dist = 1/2 * (1 + math.erf((value - avg) / (std * math.sqrt(2))))
    return norm_cumul_dist

if __name__ == '__main__':
    
    avg_car, std_car = list(map(float, input().strip().split()))
    
    t_val1 = float(input().strip())
    
    t_val2_min, t_val2_max = list(map(float, input().strip().split()))
    
    t_prob1 = normal_cprob(t_val1, avg_car, std_car)
    
    t_prob2 = normal_cprob(t_val2_max, avg_car, std_car) - normal_cprob(t_val2_min, avg_car, std_car)
    
    print(round(t_prob1, 3))
    
    print(round(t_prob2, 3))
