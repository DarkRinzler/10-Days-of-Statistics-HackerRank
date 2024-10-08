# ===================================
#   Problem statement & information
# ===================================

# The final grades for a Physics exam taken by a large group of students have a mean of 70 and a standard deviation of 10. If we can approximate the distribution of these grades by a 
# normal distribution, what percentage of the students:
# • Scored higher than 80 (i.e., have a grade > 80)?
# • Passed the test (i.e., have a grade >= 60)?
# • Failed the test (i.e., have a grade < 60)?
# Find and print the answer to each question on a new line, rounded to a scale of 2 decimal places.

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
    
    avg_grade, std_grade = list(map(float, input().strip().split()))
    
    high_grade = float(input().strip())
    
    pass_grade = float(input().strip())
    
    high_test = 1 - normal_cprob(high_grade, avg_grade, std_grade)
    
    med_test = normal_cprob(pass_grade, avg_grade, std_grade)
    
    print(round(high_test * 100, 2))
    
    print(round((1 - med_test) * 100, 2))
    
    print(round(med_test *100, 2))
