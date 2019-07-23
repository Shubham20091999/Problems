tree=[]
pos=[]

def findSmallerPos(a,val):
    max=val+2
    min=val-2
    if(val+2>len(pos)):
        max=len(pos)
    if(val<2):
        min=0
    for i in range(min,max):
        if(a<pos[i]):
            return i

    return len(pos)

def search(a,i,T=False):
    l=i
    r=len(pos)-1
    if(pos[l]==a):
        return l
    if(pos[r]==a):
        return r
    while True:
        i=(l+r)//2
        if(pos[i]==a):
            return i
        if(l>=r):
            if(T==False):
                return -1
            else:
                return(-1,l)
        if(a<pos[i]):
            r=i-1
        else:
            l=i+1


def Insert(a,Tprint=True):
    i=0
    if(len(pos)==0):
        tree.append(a)
        pos.append(0)
        if(Tprint):
            print(pos[i]+1)
    else:
        while True:
            if(a>=tree[i]):
                nxt_pos=pos[i]*2+2
            else:
                nxt_pos=2*pos[i]+1
            temp=search(nxt_pos,i,True)
            if(isinstance(temp,tuple)):
                (i,val)=temp
            else:
                i=temp
            if(i==-1):
                posi=findSmallerPos(nxt_pos,val)
                pos.insert(posi,nxt_pos)
                tree.insert(posi,a)
                if(Tprint):
                    print(nxt_pos+1)
                break

def SearchInTree(a):
    i=0
    nxt_pos=0
    while True:
        if(a==tree[i]):
            return i
        elif(a<tree[i]):
            nxt_pos=pos[i]*2+1
        else:
            nxt_pos=pos[i]*2+2
        i=search(nxt_pos,i)
    

def Delete(a,i=False):
    if(i==False):
        i=SearchInTree(a)
        print(pos[i]+1)
    nxt_pos=2*pos[i]+2
    nxt_i=search(nxt_pos,i)
    if(nxt_i!=-1):
        ans=nxt_i
        while True:
            nxt_pos=2*pos[nxt_i]+1
            nxt_i=search(nxt_pos,nxt_i)
            if(nxt_i==-1):
                break
            ans=nxt_i
        tree[i]=tree[ans]
        Delete(tree[ans],ans)
    else:
        nxt_pos=2*pos[i]+1
        nxt_i=search(nxt_pos,i)
        if(nxt_i!=-1):
            ans=nxt_i
            while True:
                nxt_pos=2*pos[nxt_i]+2
                nxt_i=search(nxt_pos,nxt_i)
                if(nxt_i==-1):
                    break
                ans=nxt_i
            tree[i]=tree[ans]
            Delete(tree[ans],ans)
        else:
            pos.pop(i)
            tree.pop(i)    


    
    

def BST(l):
    for  i in range(0,len(l)):
        Insert(l[i])

def BSTdel(l):
    for i in range(0,len(l)):
        Delete(l[i])


# T=int(input())
# for i in range(0,T):
#     (op,num)=input().split()
#     num=int(num)
#     if(op=='i'):
#         Insert(num)
#     else:
#         Delete(num)

# import random
# sizeN=100000
# sizex=100
# count=0
# list=[]
# for i in range(0,1):
#     for  i in range(0,sizeN):
#         count+=1
#         num= random.randint(-sizex,sizex)
#         # list.append(num)
#         Insert(num)

#     while True:
#         count-=1
#         if(len(pos)==0):
#             break
#         index=random.randint(0,len(pos)-1)
#         Delete(tree[index])

l=[10,15,13,20,12,18,23,11,16,24]
BST(l)
print(l)
BSTdel(l)
