n=int(input())
l=list(map(lambda e: int(e)-1,input().split()))
indexofNum=[0]*n
for i in range(n):
    indexofNum[l[i]]=i
ans=0
for i in range(n):
    if(indexofNum[i]==i):
        continue
    # we dont need to change position of num==i as we are not gonna consider it next time
    l[indexofNum[i]],indexofNum[l[i]]=l[i],indexofNum[i]

    ans+=1
print(ans)