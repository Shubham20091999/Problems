# https://www.hackerrank.com/challenges/knightl-on-chessboard/problem

# def piecemove(node, moves, maxb):
#     x, y = node
#     a, b = moves
#     mx, my = maxb
#     for i, j in set([moves, moves[::-1]]):
#         for k in (1, -1):
#             for l in (1, -1):
#                 if 0 <= x + k * i <= mx and 0 <= y + l * j <= my:
#                     yield (x + k * i, y + l * j)


# def bfs(n, moves):
#     board = {(i, j): {'visited': False} for i in range(n) for j in range(n)}
#     maxb = (n-1, n-1)
#     level = 0
#     q = [(0, 0)]
#     while len(q) > 0:
#         for _ in list(q):
#             node = q.pop(0)
#             if board[node]['visited'] == True:
#                 continue
#             board[node]['visited'] = True
#             q.extend(t for t in piecemove(node, moves, maxb)
#                      if board[t]['visited'] == False)
#         level += 1
#         if maxb in q:
#             return level
#     return -1


# def knightlOnAChessboard(n):
#     return [[bfs(n, (i, j)) for i in range(1, n)] for j in range(1, n)]


# out = knightlOnAChessboard(5)
# # out=knightlOnAChessboard(int(input()))
# for row in out:
#     for e in row:
#         print(e, end=' ')
#     print('')
# ---------------------------------------
def getNextPos(a, b, x, y, n):
    ret = []
    for d in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        if(0 <= d[0]*a+x < n and 0 <= d[1]*b+y < n):
            ret.append((d[0]*a+x, d[1]*b+y))
        if(a != b):
            if(0 <= d[0]*b+x < n and 0 <= d[1]*a+y < n):
                ret.append((d[0]*b+x, d[1]*a+y))
    return ret


def getKnighted(a, b, n):
    visitedPos = [[False for _ in range(n)]for _ in range(n)]
    iterPos = [(0, 0)]
    level = 0
    while len(iterPos) > 0:
        for _ in range(len(iterPos)):
            p = iterPos.pop(0)
            if(visitedPos[p[0]][p[1]] == True):
                continue
            visitedPos[p[0]][p[1]] = True

            for nextP in getNextPos(a, b, p[0], p[1], n):
                if(nextP[0] == n-1 and nextP[1] == n-1):
                    return level+1
                if(visitedPos[nextP[0]][nextP[1]] == False):
                    iterPos.append(nextP)
        level += 1
    return -1

n=int(input())
for i in range(1, n):
    for j in range(1, n):
        print(getKnighted(i, j,n), end=' ')
    print('')
