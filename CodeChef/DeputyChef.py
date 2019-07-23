def ArrayValue(a,p):
    if(p==0):
        return a[0]
    return a[p%len(a)]

T=int(input())

for t in range(0,T):
    size=int(input())
    a=list(map(int,input().split()))
    d=list(map(int,input().split()))
    max=0
    soldier=-1
    for i in range(0,size):
        value=0
        if(d[i]>ArrayValue(a,i+1)+ArrayValue(a,i-1)):
            value=d[i]
            if(max<value):
                max=value
                soldier=i
    if(soldier!=-1):
        print(d[soldier])
    else:
        print(-1)



