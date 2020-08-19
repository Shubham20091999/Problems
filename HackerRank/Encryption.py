# https://www.hackerrank.com/challenges/encryption/problem?h_r=internal-search
from math import ceil, floor, sqrt

s = list(input())
l = floor(sqrt(len(s)))
u = ceil(sqrt(len(s)))
r = l
c = l
M = []
if(r*c < len(s)):
    c += 1
if(r*c < len(s)):
    r += 1

# s += ['']*(r*c-len(s))
# for i in range(r):
#     M.append(s[i*c:(i+1)*c])

# for j in range(len(M[0])):
#     for i in range(len(M)):
#         print(M[i][j], end='')
#     print(' ', end='')

for j in range(c):
    for i in range(r):
        try:
            print(s[i*c+j],end='')
        except:
            print('',end='')
    print(' ',end='')
