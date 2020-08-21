# https://www.hackerrank.com/challenges/candies/problem

def candies(n,arr):
    candies = [1]*n
    # Forward
    for i in range(1,n):
        if arr[i]>arr[i-1]:
            candies[i] = candies[i-1]+1
    # Backward
    for i in range(n-1,0,-1):
        if arr[i-1]>arr[i] and candies[i-1]<=candies[i]:
            candies[i-1] = candies[i]+1
    return sum(candies)
n = int(input())
arr = [int(input()) for _ in range(n)]
print(candies(n,arr))