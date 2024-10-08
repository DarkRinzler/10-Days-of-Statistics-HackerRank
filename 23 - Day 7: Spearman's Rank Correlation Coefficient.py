# ===================================
#   Problem statement & information
# ===================================

# Given two -element data sets, X and Y, calculate the value of Spearman's rank correlation coefficient.

# Difficulty: Easy
# Max Score: 30
# Language: Python

# ===================================
#             Solution
# ===================================

def rank(array):
    new_array = sorted(array)
    index_dict = {num: index+1 for index, num in enumerate(new_array)}
    rank_array = [index_dict[num] for num in array]
    return rank_array

def stdDev(array):
    mean = sum(array) / len(array)
    var = sum((x - mean) ** 2 for x in array) / len(array)
    return var ** 0.5
    
def SPcorr(num, setX, setY):
    sdX, sdY = stdDev(setX), stdDev(setY)
    xm, ym = sum(setX)/len(setX), sum(setY)/len(setY)
    cov = sum((i-xm)*(j-ym) for i, j in zip(setX, setY))/(num*sdX*sdY)
    return cov

if __name__ == '__main__':
    
    n = int(input().strip())
    X = list(map(float, input().strip().split()))
    Y = list(map(float, input().strip().split()))
    
    print(round(SPcorr(n, rank(X), rank(Y)), 3))
