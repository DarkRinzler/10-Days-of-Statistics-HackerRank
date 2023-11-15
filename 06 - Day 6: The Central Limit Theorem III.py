# ===================================
#   Problem statement & information
# ===================================

# You have a sample of 100 values from a population with mean 500 and with standard deviation 80. Compute the interval that covers the middle 95% of the distribution of the sample mean; 
# in other words, compute A and B such that P(A < x < B) = 0.95. Use the value of z = 1.96. Note that z is the z-score.

# ===================================
#              Solution
# ===================================

#!/bin/python3

import math

if __name__ == '__main__':
    
    sample = float(input().strip())
    mean = float(input().strip())
    sd = float(input().strip())
    perc = float(input().strip())
    z_value = float(input().strip())
    
    print(round(mean - z_value * (sd / math.sqrt(sample)), 2))
    print(round(mean + z_value * (sd / math.sqrt(sample)), 2))
