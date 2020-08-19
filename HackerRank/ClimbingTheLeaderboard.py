# # # https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

########################
from bisect import bisect_right

n = int(input())
scores = sorted(set(map(int,input().split())))
m = int(input())
alice = map(int,input().split())

# your code goes here
for a in alice:
    print(len(scores)-bisect_right(scores,a)+1)
