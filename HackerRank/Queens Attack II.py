# https://www.hackerrank.com/challenges/queens-attack-2/problem

from math import sqrt
n, k = map(int, input().split())
x, y = map(int, input().split())
obs = set([])
for i in range(0, k):
    obs.add(tuple(map(int, input().split())))

count = 0

# 1
for yi in range(y+1, n+1):
    if((x, yi) not in obs):
        count += 1
    else:
        break
# 2
for yi in range(1, y):
    if((x, y-yi) not in obs):
        count += 1
    else:
        break
# 3
for xi in range(x+1, n+1):
    if((xi, y) not in obs):
        count += 1
    else:
        break
# 4
for xi in range(1, x):
    if((x-xi, y) not in obs):
        count += 1
    else:
        break

# 5
lim = min(n-x, n-y)+1
for d in range(1, lim):
    if((x+d, y+d) not in obs):
        count += 1
    else:
        break
# 6
lim = min(x, n+1-y)
for d in range(1, lim):
    if((x-d, y+d) not in obs):
        count += 1
    else:
        break

# 7
lim = min(x, y)
for d in range(1, lim):
    if((x-d, y-d) not in obs):
        count += 1
    else:
        break

# 8
lim = min(n+1-x, y)
for d in range(1, lim):
    if((x+d, y-d) not in obs):
        count += 1
    else:
        break

print(count)


###################

# count = [n-y, y-1, n-x, x-1, min(x-1, y-1),
#          min(n-y, n-x), min(x-1, n-y), min(n-x, y-1)]


# def isDiag(x1, y1):
#     if(sqrt((x-x1)**2+(y-y1)**2)/sqrt(2) == min((abs(x-x1), (abs(y-y1))))):
#         return True
#     return False


# def inLine(x1, y1):
#     if(x1 == x or y1 == y):
#         return True
#     return False


# def getPosInLine(x1, y1):
#     if(x1 == x):
#         if(y1 > y):
#             return 1
#         return 2
#     if(x1 > x):
#         return 3
#     return 4


# def getPosDiag(x1, y1):
#     if(x1 > x and y1 > y):
#         return 6
#     if(x1 < x and y1 > y):
#         return 7
#     if(x1 > x and y1 < y):
#         return 8
#     return 5


# for o in obs:
#     if(inLine(o[0], o[1])):
#         if(count[getPosInLine(o[0], o[1])] > max(abs(o[0]-x), abs(o[1]-y))):
#             count[getPosInLine(o[0], o[1])] = max(abs(o[0]-x), abs(o[1]-y))
#     elif(isDiag(o[0], o[1])):
#         count[getPosDiag(o[0], o[1])]+=1

# print(sum(count))
