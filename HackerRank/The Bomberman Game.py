# https://www.hackerrank.com/challenges/bomber-man/problem

#output of 3,7,11... will be same -> 3x
#output of 5,9,13... will be same -> 5x
#output of 2,4,6... will be complete fill -> 2x
#5x and {0} will be different but after blast both will be same
#ie {6} will be same as {2}

from copy import deepcopy
r, c, n = map(int,input().split())
inp=['']*r
for i in range(r):
    inp[i]=list(input())
diff = [(0, 1), (1, 0), (-1, 0), (0, -1)]

layout = [[0 for _ in range(c)] for _ in range(r)]

for i in range(r):
    for j in range(c):
        if(inp[i][j] == 'O'):
            layout[i][j] = 3


def fillUp(layout: list) -> list:
    global r, c
    for i in range(r):
        for j in range(c):
            if(layout[i][j] == 0):
                layout[i][j] = 3
    return deepcopy(layout)


def isInside(i, j):
    global r, c
    if(i >= 0 and j >= 0 and i < r and j < c):
        return True
    return False


def boomUp(layout: list) -> list:
    global r, c
    for i in range(r):
        for j in range(c):
            if(layout[i][j] == 1):
                layout[i][j] = 0
                for d in diff:
                    if(isInside(i+d[0], j+d[1]) and layout[i+d[0]][j+d[1]] != 1):
                        layout[i+d[0]][j+d[1]] = 0

    return deepcopy(layout)


def passUp(layout: list) -> list:
    global r, c
    for i in range(r):
        for j in range(c):
            if(layout[i][j] != 0):
                layout[i][j] -= 1
    return deepcopy(layout)


def printFill():
    global r, c
    for _ in range(r):
        for _ in range(c):
            print('O', end='')
        print('')


def printLayout(layout: list) -> None:
    global r, c
    for i in range(r):
        for j in range(c):
            if(layout[i][j] != 0):
                print('O', end='')
            else:
                print('.', end='')
        print('')


# 1
deepcopy(layout)
passUp(layout)
n-=1
if(n==0):
    printLayout(layout)
    exit(0)
# 2
passUp(layout)
fillUp(layout)
n-=1
if(n==0):
    printLayout(layout)
    exit(0)
# 3
boomUp(layout)
layout_3 = passUp(layout)
n-=1
if(n==0):
    printLayout(layout)
    exit(0)
# 4
passUp(layout)
fillUp(layout)
n-=1
if(n==0):
    printLayout(layout)
    exit(0)
# 5
boomUp(layout)
layout_5 = passUp(layout)
n-=1
if(n==0):
    printLayout(layout)
    exit(0)

if(n!=0):
    if(n%2==1):
        printFill()
    else:
        if(n%4==0):
            printLayout(layout_5)
        else:
            printLayout(layout_3)
