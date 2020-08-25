from collections import Counter
n,r=map(int,input().split())
l=list(map(int,input().split()))
dr=Counter(l)
dl=Counter()

count=0
for i in range(len(l)):
    dr[l[i]]-=1
    if(l[i]%r==0):
        count+=dl[l[i]//r]*dr[l[i]*r]
    dl[l[i]]+=1
        
print(count)