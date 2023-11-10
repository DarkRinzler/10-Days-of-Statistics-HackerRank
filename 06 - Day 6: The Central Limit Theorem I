# ===================================
#   Problem statement & information
# ===================================

# A large elevator can transport a maximum of 9800 pounds. Suppose a load of cargo containing 49 boxes must be transported via the elevator. The box weight of this type of cargo follows 
# a distribution with a mean of 205 pounds and a standard deviation of 49 pounds. Based on this information, what is the probability that all 49 boxes can be safely loaded into the freight 
# elevator and transported?

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
    
    max_weight = float(input().strip())
    num_box = float(input().strip())
    avg = float(input().strip())
    stdv = float(input().strip())
    
    prob = normal_cprob(max_weight, num_box*avg, math.sqrt(num_box)*stdv)
    
    print(round(prob, 4))
    
