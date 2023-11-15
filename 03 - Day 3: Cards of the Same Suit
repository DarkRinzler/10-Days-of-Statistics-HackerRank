# ===================================
#   Problem statement & information
# ===================================

# You draw 2 cards from a standard -card deck without replacing them. What is the probability that both cards are of the same suit?

# Difficulty: Easy
# Max Score: 10
# Language: Python
# Multiple Choice Question - No code required

# ===================================
#              Solution
# ===================================

# ===================================
#             Method 1
# ===================================

# Given that in a deck of card we have 52 cards, it is clear that there will be 13 card of the same suit and 4 suits in total. The probability of taking one card from the deck will be 1 obviously. As we 
# have taken a card out now the number of card in the deck will be 51 and the card of the same suit will be 12. Therefore, the probability of drawning another card of the same suit will be the product
# of the initial probability times the probability of drawning another card of the same suit, namely

1. P(A) = 12/51

# where the outcomes set A can be defined as

2. A = {{1,...,13} x n | n in {1,...,13}}

# ===================================
#             Method 2
# ===================================

# As a second approach we may use the definition of combinations through the factorial operation. Given that there are 52 cards, the number of possible unordered possible pair of card that can be created 
# from the deck is

1. C(2,52) = 26 * 51

# In an analogous manner, the number of possible unordered possible pair of card that can be created for a given specific suits will be

2. C(2,13) = 13 * 6

# From the previous results, it is clear that the probability that 2 cards of the same suit will be drawn from the deck is equal to the ratio of 2 over 1. This will give the probability for an arbitrary 
# single suit. As the number of suits is equal to 4, we have

3. P(A) = 4* (C(2,13)/C(2,52)) = 4 * 3/51 = 12/51 
