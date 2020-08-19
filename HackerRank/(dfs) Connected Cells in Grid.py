# https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem

m = int(input())
n = int(input())
diff = [1, 0, -1]


def flood(x, y):
    global mat, n, m, diff
    if(x >= m or y >= n or mat[x][y] == 0 or x < 0 or y < 0):
        return 0
    mat[x][y] = 0
    ret = 1
    for dx in diff:
        for dy in diff:
            ret += flood(x+dx,y+dy)
    return ret

def floodAll():
    global m, n
    max = 0
    for i in range(m):
        for j in range(n):
            temp = flood(i, j)
            if(temp > max):
                max = temp
    return max


mat = [None for _ in range(m)]
for i in range(m):
    mat[i] = list(map(int, input().split()))
print(floodAll())
