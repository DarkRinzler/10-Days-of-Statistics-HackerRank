# ===================================
#   Problem statement & information
# ===================================

# The number of tickets purchased by each student for the University X vs. University Y football game follows a distribution that has a mean of 2.4 and a standard deviation of 2.0.
# A few hours before the game starts, 100 eager students line up to purchase last-minute tickets. If there are only 250 tickets left, what is the probability that all  students will 
# be able to purchase tickets?

# Difficulty: Easy
# Max Score: 30
# Language: Python

# ===================================
#              Solution
# ===================================

#!/bin/python3

import math

def normal_cprob(value, avg, sd):
    norm_cumul_dist = 1/2 * (1 + math.erf((value - avg) / (sd * math.sqrt(2))))
    return norm_cumul_dist

if __name__ == '__main__':
    
    num_tickets = float(input().strip())
    num_stud = float(input().strip())
    avg = float(input().strip())
    sd = float(input().strip())
    
    print(round(normal_cprob(num_tickets, num_stud*avg, math.sqrt(num_stud)*sd), 4))
