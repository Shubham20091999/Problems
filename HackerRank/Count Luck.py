# https://www.hackerrank.com/challenges/count-luck/problem
diff = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def goNext(x, y):
    global m, n, forestMap
    if(forestMap[x][y] == '*'):
        forestMap[x][y] = 'X'
        return 0
    direc = []
    for (dx, dy) in diff:
        if(0 <= x+dx < m and 0 <= y+dy < n):
            if(forestMap[x+dx][y+dy] == '.' or forestMap[x+dx][y+dy] == '*'):
                direc.append([x+dx, y+dy])

    forestMap[x][y] = 'X'
    if(len(direc) == 0):
        return float('inf')
    if(len(direc) == 1):
        return goNext(direc[0][0], direc[0][1])
    else:
        rets=[]
        for p in direc:
            rets.append(goNext(p[0], p[1]))
        return 1+min(rets)



for _ in range(int(input())):
    m, n = map(int, input().split())
    forestMap = [[]]*m
    y = -1
    x = -1
    for i in range(m):
        forestMap[i] = list(input())
        try:
            y = forestMap[i].index('M')
            x = i
        except:
            pass
    k=int(input())
    
    print('Impressed' if(goNext(x, y)==k) else 'Oops!')
