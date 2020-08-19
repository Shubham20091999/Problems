# https://www.hackerrank.com/challenges/two-pluses/problem
from math import ceil, floor

m, n = map(int, input().split())
# Padding None
grid = [None]*(m+2)
grid[0] = [None]*(n+2)
grid[-1] = [None]*(n+2)
for i in range(1, m+1):
    # 0 if G None if B
    grid[i] = [None]+list(map(lambda e: 0 if(e == 'G')
                              else None, list(input())))+[None]

diff = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def printGrid(grid):
    for i in range(0, m+2):
        for j in range(0, n+2):
            if(grid[i][j] == None):
                print('X', end='')
            else:
                print(grid[i][j], end='')
        print('')


# Position of Plus
plusPos = []
# Length of arm at Plus
plusLen = []

# Adding all Pluses into plusPos and plusLen
for i in range(1, m+1):
    for j in range(1, n+1):
        if(grid[i][j] != None):
            while True:
                for d in diff:
                    if(grid[i+d[0]*(grid[i][j]+1)][j+d[1]*(grid[i][j]+1)] == None):
                        break
                else:
                    grid[i][j] += 1
                    continue
                break
            if(grid[i][j] != None):
                plusPos.append((i, j))
                plusLen.append(grid[i][j])

# Returns max of multiplication after overlap check
# if overlap is there then the value will be less
# else the value can be directly calculated 
def areaWithoutOverlap(pos1, d1, pos2, d2):
    dx = abs(pos1[0]-pos2[0])
    dy = abs(pos1[1]-pos2[1])
    #if in same horizontal line
    if(dy == 0):
        if(dx <= d1+d2):
            return (max(d1, d2)-ceil((d1+d2-dx)/2))*(min(d1, d2)-floor((d1+d2-dx)/2))
    #if in same vertical line
    elif(dx == 0):
        if(dy <= d1+d2):
            return (max(d1, d2)-ceil((d1+d2-dy)/2))*(min(d1, d2)-floor((d1+d2-dy)/2))
    #if they rectangle
    else:
        #if two arms of both rectangle intersect
        if((dx <= d1 and dy <= d2) and (dx <= d2 and dy <= d1)):
            return max((min(dx, dy)*4+1)**2, (d1*4+1)*((min(dx, dy)-1)*4+1), (d2*4+1)*((min(dx, dy)-1)*4+1))
        #if point of overlap is above point 2
        if((dx <= d1 and dy <= d2)):
            return max((d1*4+1)*((dy-1)*4+1), ((dx-1)*4+1)*(d2*4+1))
        #if point of overlap is left of point 2
        if((dx <= d2 and dy <= d1)):
            return max((d1*4+1)*((dx-1)*4+1), ((dy-1)*4+1)*(d2*4+1))
    #if no overlap
    return (d1*4+1)*(d2*4+1)

maxVal = 0
#Making pairs of pluses and saving the max value
for i in range(len(plusPos)-1):
    for j in range(i+1, len(plusPos)):
        temp = areaWithoutOverlap(
            plusPos[i], plusLen[i], plusPos[j], plusLen[j])
        if(temp > maxVal):
            maxVal = temp

print(maxVal)

# OR:
# While saving pluses and arm lengths 
# also save pluses with same centers and just iterate over each of them while checking overlap
# if overlap exist than skip that one
# otherwise compare with maxValue