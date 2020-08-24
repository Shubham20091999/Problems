# https://www.hackerrank.com/challenges/greedy-florist/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms
n,k=map(int,input().split())
l=sorted(list(map(int,input().split())),reverse=True)
ans=0
multi=1
while len(l):
    for i in range(k):
        if(len(l)==0):
            break
        ans+=multi*l.pop(0)       
    multi+=1
print(ans)