# https://www.hackerrank.com/challenges/maximum-palindromes/problem
# To Find Modulo Inverse
# https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/

M = int(1e9) + 7
fact = [1]
for i in range(1, 10**5 + 1):
    fact.append(fact[-1]*i % M)

# Saved for which mod is already calculated 
savedModInv={}

# Check geeks for geeks Link
# To Find the modulo inverse of a number a wrt m
def modinv(a):
    global M
    if(a not in savedModInv):
        savedModInv[a]=pow(a, M - 2, M)# Calculates a**(M-2)%M but faster see code in extra section
    return savedModInv[a]

def getNumberOfMaximumPalindromes(l, r):
    global freqLeft
    
    # Frequincies of various alphabet between l and r
    # Setting it equal to r and then removing frequencies to the left of (l-1) as we have to include l and r both
    freq = freqLeft[r][:]
    # Number of odd frequencies 
    numMaxOdd = 0
    for i in range(26):
        freq[i] -= freqLeft[l-1][i]
        if(freq[i] % 2 != 0):
            freq[i] -= 1
            numMaxOdd += 1

    res = 1
    total = 0

    for f in freq:
        res *= modinv(fact[f//2])
        total += f//2
        res %= M

    return (max(1, numMaxOdd)*fact[total]*res) % (10**9+7)


freqLeft = [[0]*26]
# Saving frequencies of letters to the left of the ith letter
for s in input():
    tmp = freqLeft[-1][:]
    tmp[ord(s)-97] += 1
    freqLeft.append(tmp)

for i in range(int(input())):
    l, r = map(int, input().split())
    print(getNumberOfMaximumPalindromes(l, r))

#---------Extra----------------
def power(x, y, m):
    if (y == 0):
        return 1

    p = power(x, y // 2, m) % m
    p = (p * p) % m

    if(y % 2 == 0):
        return p
    else:
        return ((x * p) % m)