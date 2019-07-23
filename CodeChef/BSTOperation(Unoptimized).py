

t=[]

def ListInsert(i,a):
    global t
    if(i<len(t)):
        if(t[i]=='-'):
            t[i]=a
        else:
            t.insert(i,a)
    else:
        temp=['-']*(i-len(t))
        t+=temp
        t.insert(i,a)


def Delete(a):
    global t
    j=0
    for i in range(0,len(t)):
        if(a==t[i]):
            j=i
    print(j+1)
    while True:
        if(2*j+2>len(t)):
            break
        t[j]=t[2*j+2]
        j=2*j+2    
    t[j]='-'
    

def Insert(a):
    global t
    i=0
    while True:
        if(i>=len(t) or t[i]=='-'):
            break
        if(a>t[i]):
            i=2*i+2
        else:
            i=2*i+1
    
    ListInsert(i,a)
    print(i+1)

def BST(l):
    for  i in range(0,len(l)):
        Insert(l[i])



# T=int(input())
# for i in range(0,T):
#     (op,num)=input().split()
#     num=int(num)
#     if(op=='i'):
#         Insert(num)
#     else:
#         Delete(num)

l=[3,5,8,6,2]
BST(l)
print(t)

Delete(3)

print(t)