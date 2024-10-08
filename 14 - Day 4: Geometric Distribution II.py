# ===================================
#   Problem statement & information
# ===================================

# The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect is found during the first 5 inspections?

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
    
    sum_prob_defect = 0
    
    sum_prob_defect = sum(geometric_prob(i, prob_defect) for i in range(1, num_item+1))
    
    print(round(sum_prob_defect, 3))
