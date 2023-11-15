# ===================================
#   Problem statement & information
# ===================================

# Suppose a family has 2 children, one of which is a boy. What is the probability that both children are boys?

# Difficulty: Easy
# Max Score: 10
# Language: Python
# Multiple Choice Question - No code required

# ===================================
#              Solution
# ===================================

# The solution consists in counting all the possible distinct combination of children in a family from the sample set 

1. S ={{M,F} x {M,F}}

# The total sample set will be 

2. S ={(M,M), (M,F), (F,M), (F,F)}

#As wish to only consider families having at least one boy, we may drop the sample set pair (F,F) as it would not be part of the possibilities considered. Therefore, the possible outcome set reduced to

2. A = {(M,M), (M,F), (F,M)} 

# Given the above result, it is clear that the probability of having two boys is

3. P((M,M)) = 1/3 
