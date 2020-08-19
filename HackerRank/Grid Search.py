# https://www.hackerrank.com/challenges/the-grid-search/problem
t = int(input())

def gridSearch(arr, term):
    c = len(term[0])
    R = len(arr)
    for i in range(len(arr)):
        pos = arr[i].find(term[0])
        prePos = -1
        while (pos != prePos):
            prePos = pos
            d = 1
            for t in term[1:]:
                if(d+i > R):
                    return 'NO'
                if(t != arr[i+d][pos:pos+c]):
                    pos = arr[i][pos+1:].find(term[0])+pos+1
                    break
                d += 1
            else:
                return 'YES'
    else:
        return 'NO'


for i in range(t):
    R, C = map(int, input().split())
    arr = ['']*R
    for i in range(R):
        arr[i] = input()

    r, c = map(int, input().split())

    term = ['']*r
    for i in range(r):
        term[i] = input()
    print(gridSearch(arr, term))

# #-------------------------------------------------
import re

def gridSearch(G, P):
    l = len(P)
    m = len(P[0])
    for x, y in enumerate(G):
        for i in ((m.start(0)) for m in re.finditer("(?=%s)" % P[0], y)):
            for a in range(1, l):
                if G[a+x][i:i+m] != P[a]:
                    break
            else:
                return "YES"

    return "NO"


for _ in range(int(input())):
    R, C = map(int, input().split())
    G = [input() for _ in range(R)]
    r, c = map(int, input().split())
    P = [input() for _ in range(r)]
    print(gridSearch(G, P))
