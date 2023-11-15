# ===================================
#   Problem statement & information
# ===================================

# The ratio of boys to girls for babies born in Russia is 1.09:1. If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?
# Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of 3 decimal places.

# Difficulty: Easy
# Max Score: 30
# Language: Python

# ===================================
#              Solution
# ===================================

#!/bin/python3

from functools import reduce

def factorial(num):
    return reduce(lambda x, y: x * y, range(1, num + 1), 1)

def combinations(num_up, num_down):
    return factorial(num_up)/(factorial(num_down) * factorial(num_up-num_down))
    
def binomial_prob(num_succ, num_events, prob_succ):
    prob_insucc = 1 - prob_succ
    return combinations(num_events, num_succ) * (prob_succ ** num_succ) * (prob_insucc ** (num_events - num_succ))
    
if __name__ == '__main__':
    
    boys, girls = list(map(float, input().strip().split()))
    prob_boys = boys/(boys+girls)
    sum_prob = sum(binomial_prob(k, 6, prob_boys) for k in range(3, 7))
    print(round(sum_prob, 3))
