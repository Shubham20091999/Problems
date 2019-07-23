def Check(m,n):
    p=m%2
    q=n%2
    if(p==q):
        return 0
    else:
     return 1

I=int(input())

for i in range(0,I):
    l,r=map(int,input().split())
    x=[]
    for j in range(l,r+1):
        x.append(j)
    for j in range(0,len(x)-1):
        x[j+1]=Check(x[j],x[j+1])
    if(x[len(x)-1]==0):
        print("Even")
    else:
        print("Odd")
    



