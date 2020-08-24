# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms
n=int(input())

l=sorted(map(int,input().split()))
m=float('inf')
for i in range(1,n):
    if(abs(l[i]-l[i-1])<m):
        m=abs(l[i]-l[i-1])
print(m)

