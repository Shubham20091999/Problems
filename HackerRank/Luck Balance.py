# https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms
n,k=map(int,input().split())
imp=[]
ans=0

for _ in range(n):
    l,r=map(int,input().split())
    if(r==0):
        ans+=l
    else:
        imp.append(l)
imp.sort(reverse=True)
print(ans+sum(imp[:k])-sum(imp[k:]))