# ===================================
#   Problem statement & information
# ===================================

# A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons
# will contain:
# 1. No more than 2 rejects?
# 2. At least 2 rejects?

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
    
    prob_defect, num_batch = list(map(int, input().strip().split()))
    sum_prob_less, sum_prob_more = 0, 0
    for k in range(3):
        sum_prob_less += binomial_prob(k, num_batch, prob_defect * 0.01)
        if k == 1:
            sum_prob_more = 1 - sum_prob_less
    print(round(sum_prob_less, 3))
    print(round(sum_prob_more, 3))
