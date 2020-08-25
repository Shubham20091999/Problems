l=[None]*6
for i in range(6):
    l[i]=list(map(int,input().split()))

def getNeigh(i,j):
    diff=[(0,0),(1,0),(-1,0),(-1,-1),(1,1),(1,-1),(-1,1)]
    for d in diff:
        yield (i+d[0],j+d[1])
ans=-float('inf')
for i in range(1,5):
    for j in range(1,5):
        temp=0
        for m,n in getNeigh(i,j):
            temp+=l[m][n]
        if(temp>ans):
            ans=temp
print(ans)