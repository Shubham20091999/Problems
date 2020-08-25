n,m=map(int,input().split())
edges=[None]*m

lst=[0]*(n+1)

for i in range(m):
    l,r,k=map(int,input().split())
    lst[l-1]+=k
    lst[r]-=k
m=0
x=0
for i in range(n):
    x+=lst[i]
    if(m<x):
        m=x
print(m)