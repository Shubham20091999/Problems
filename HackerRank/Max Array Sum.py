# https://www.hackerrank.com/challenges/max-array-sum/
n = int(input())
li = list(map(int, input().split()))

li[0] = max(li[0], 0)
li[1] = max(li[1], 0)
li[2] = max(li[2], 0)+li[0]

for i in range(3, n):
    li[i] = max(li[i], 0)+max(li[i-2], li[i-3])
print(max(li[-1], li[-2]))
