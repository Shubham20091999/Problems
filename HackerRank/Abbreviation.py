# https://www.youtube.com/watch?v=sSno9rV8Rhg

import sys
sys.setrecursionlimit(10**3+10)


memo = []
a = None
b = None

# Recursive and Memoized
def memoized(i, j):
    global memo, a, b
    if(memo[i][j] != None):
        return memo[i][j]
    if(i == len(b)):
        for k in range(j, len(a)):
            if(a[k].isupper()):
                memo[i][j] = False
                return False
        memo[i][j] = True
        return True
    elif(j == len(a)):
        memo[i][j] = False
        return False
    if(a[j] == b[i]):
        memo[i][j] = memoized(i+1, j+1)
        return memo[i][j]
    if(a[j].upper() == b[i]):
        memo[i][j] = memoized(i, j+1) or memoized(i+1, j+1)
        return memo[i][j]
    if(a[j].islower()):
        memo[i][j] = memoized(i, j+1)
        return memo[i][j]
    memo[i][j] = False
    return False


for _ in range(int(input())):
    a = input()
    b = input()
    memo = [[None for _ in range(len(a)+1)] for _ in range(len(b)+1)]
    print('YES' if(memoized(0, 0)) else 'NO')
