# https://www.hackerrank.com/challenges/minimum-loss/problem

# If all prices are distinct as said in the question
n=int(input())
l=list(map(int,input().split()))
d=dict()
for i in range(n):
    try:
        d[l[i]]=i
    except:
        d[l[i]]=i

l.sort()
min=float('inf')

for i in range(1,len(l)):
    if(l[i]-l[i-1]<min):
        if(d[l[i]]<d[l[i-1]]):
            min=l[i]-l[i-1]
print(min)

# ------------------------------------
# If all prices are not distinct
n=int(input())
l=list(map(int,input().split()))
d=dict()
for i in range(n):
    try:
        d[l[i]]+=[i]
    except:
        d[l[i]]=[i]

def checkLesser(l1,l2):
    for m in l1:
        for n in l2:
            if(m<n):
                return True
    return False

l=sorted(l)
min=float('inf')

for i in range(1,len(l)):
    if(l[i]-l[i-1]<min):
        if(checkLesser(d[l[i]],d[l[i-1]])):
            min=l[i]-l[i-1]
print(min)


