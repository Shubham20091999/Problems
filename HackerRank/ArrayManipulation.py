

def arrayManipulation(n,q):
    l=[0]*(n+1)
    for i in range(0,len(q)):
        l[q[i][0]]+=q[i][2]
        if(q[i][1]+1<=n):
            l[q[i][1]+1]-=q[i][2]
    max=0
    x=0

    for  i in range(0,n+1):
        x+=l[i]
        if(max<x):
            max=x

    return max

n=5
queries=[[1,2,100],[2,5,100],[3,4,100]]
print(arrayManipulation(n,queries))

# f= open("Inputs.txt","r")
# eles=f.read().split('\n')
# n=int(eles[0].split()[0])
# k=int(eles[0].split()[1])
# q=[]

# for i in range(1,len(eles)):
#     q.append(list(map(int,eles[i].split())))

# print(arrayManipulation1(n,q))

