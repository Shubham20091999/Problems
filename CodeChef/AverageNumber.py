t=int(input())
for j in range(0,int(t)):
    n,k,v=map(int,input().split())
    a=sum(map(int,(input().split())))
    temp=(v*(k+n)-a)/k
    if(int(temp)==temp and temp>0):
        print(int(temp))
    else:
        print(-1)

