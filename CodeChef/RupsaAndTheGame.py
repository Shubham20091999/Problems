
MOD=10**9+7


def Ans2(l,n):
    ans=0
    temp=0
    mul=1
    for i in range(1,n+1):
        if(i!=1 and i!=2):
                mul=2*mul%MOD
        else:
                mul=1
        temp+=l[i-1]*mul
        ans+=2*l[i]*temp%MOD
        ans+=ans
        
    print((ans//2%MOD))

T=int(input())

for t in range(0,T):  
    n=int(input())
    l=list(map(int,input().split()))

    Ans2(l,n)
