# ===================================
#   Problem statement & information
# ===================================

# In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that their sum will be at most 9.

# Difficulty: Easy
# Max Score: 10
# Language: Python
# Multiple Choice Question - No code required

# ===================================
#              Solution
# ===================================

# The are two possible approach to the problem. The first consists in counting all the possible combination of pair numbers such that their sum is <= 9 and divide it by the total number of outcomes from 
# the sample set 

1. S ={{1,2,3,4,5,6} x {1,2,3,4,5,6}}

#The second approach in contrast counts all the possible combination of pair numbers such that their sum is > 9 and the subtracts the probability
# related to it from 1. Given the large sample set and the sum constraint, the second approach would be more time efficient. As such, a simple computation shows that the possible distinct outcomes 
# satisfying the sum constraint will be 

2. A = {(4,6), (5,5), (5,6), (6,6), (6,4), (6,5)} 

# The total possible outcomes will be equal to 36, in other words the total number of sides on each die raised to the power of the number of dice considered. Given the definition of probability 
# and the fact that 

3. P(A^c) = 1 - P(A)

# we find the desired result

4. P(A) = 1/6  ------> P(A^c) = 5/6

