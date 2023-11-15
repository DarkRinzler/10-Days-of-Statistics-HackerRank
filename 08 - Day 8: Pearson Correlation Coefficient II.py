# ===================================
#   Problem statement & information
# ===================================

# The regression line of y on x is 3x+4y+8=0, and the regression line of x on y is 4x+3y+7=0. What is the value of the Pearson correlation coefficient?

# Difficulty: Easy
# Max Score: 30
# Language: Python
# Multiple Choice Question - No code required

# ===================================
#              Solution
# ===================================

# Given the request of problem, it is convinient to write both equation in normal form with respect to its regression variable, namely

1. y = (-3/4)*x - 2
2. x = (-3/4)*y -(7/4)

# As we are expressing the regression line for both variables, the corresponding standard deviation value will have the same value. In view of this we can relate Pearson correlation coefficient
# for both equation through the identities

1. (-3/4) = rho * (sigma_y/sigma_x)
2. (-3/4) = rho * (sigma_x/sigma_y)

# In the second equation the standard deviation are flipped as equation 2 is the regression line of the variable x with respect to the variable y. Being both equation 1 and 2 negative, it is clear 
# that the Pearson correlation coefficient will be a negative quantity as the standard deviations are positive quantities by definition. Thereby, by multiplying equation 1 by equation 2, and isolating 
# the Pearson correlation coefficient rho it follows that

rho^2 = 9/16 ------->  rho = ± 3/4

# By virtue of the previous discussion, it follows that the only possible solution satisfying the above constraints is rho = -3/4.
