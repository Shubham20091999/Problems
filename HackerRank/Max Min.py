# https://www.hackerrank.com/challenges/angry-children/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms

n=int(input())
k=int(input())-1
l=[None]*n
for i in range(n):
    l[i]=int(input())

l.sort()
m=float('inf')
for i in range(k,n):
    if(l[i]-l[i-k]<m):
        m=l[i]-l[i-k]
print(m)