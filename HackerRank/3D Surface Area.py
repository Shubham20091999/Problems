# https://www.hackerrank.com/challenges/3d-surface-area/problem?h_r=internal-search
# m, n = map(int, input().split())

# arr = [0]*(m)

# for i in range(0, m):
#     arr[i] = list(map(int, input().split()))

# ans = 2*m*n
# for i in range(0, len(arr)):
#     ans += arr[i][0]+arr[i][-1]
#     for j in range(1, len(arr[0])):
#         ans += abs(arr[i][j]-arr[i][j-1])

# for j in range(0, len(arr[0])):
#     ans += arr[0][j]+arr[-1][j]
#     for i in range(1, len(arr)):
#         ans += abs(arr[i][j]-arr[i-1][j])

# print(ans)

# ------------------------------------------

m, n = map(int, input().split())

arr = [0]*(m+2)
arr[0], arr[-1] = [0]*(n+2), [0]*(n+2)

for i in range(1, m+1):
    arr[i] = [0] + list(map(int, input().split()))+[0]

ans = 2*m*n
change = [(0, -1), (-1, 0), (0, 1), (1, 0)]
for i in range(1, len(arr)-1):
    for j in range(1, len(arr[0])-1):
        for d in change:
            ans += max(0, arr[i][j]-arr[i-d[0]][j-d[1]])
print(ans)
