# ===================================
#   Problem statement & information
# ===================================

# The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect occurs the 5th item produced?

# Difficulty: Easy
# Max Score: 30
# Language: Python

# ===================================
#              Solution
# ===================================

#!/bin/python3

def geometric_prob(num_succ_event, prob_succ):
    prob_insucc = 1 - prob_succ
    return prob_succ * (prob_insucc ** (num_succ_event - 1))
    
if __name__ == '__main__':
    
    prob_num_defect, prob_den_defect = list(map(int, input().strip().split()))
    
    num_item = int(input().strip())
    
    prob_defect = float(prob_num_defect / prob_den_defect)
    
    print(round(geometric_prob(num_item, prob_defect), 3))
