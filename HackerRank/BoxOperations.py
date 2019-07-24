# not fast enough

def Floor(box,l,r,d):
    for i in range(l,r+1):
        box[i]=box[i]//d

def AddC(box,l,r,c):
    for i in range(l,r+1):
        box[i]+=c

def printAdd(box,l,r):
    ans=0
    for i in range(l,r+1):
        ans+=box[i]
    print(ans)

def printMin(box,l,r):
    print(min(box[l:r+1]))

def BoxOps(box,ops):
    for i in range(0,len(ops)):
        tmp_ops=ops[i]
        if(tmp_ops[0]==1):
            AddC(box,tmp_ops[1],tmp_ops[2],tmp_ops[3])
            continue
        if(tmp_ops[0]==2):
            Floor(box,tmp_ops[1],tmp_ops[2],tmp_ops[3])
            continue
        if(tmp_ops[0]==4):
            printAdd(box,tmp_ops[1],tmp_ops[2])
            continue
        if(tmp_ops[0]==3):
            printMin(box,tmp_ops[1],tmp_ops[2])
            continue


(n,k)=list(map(int,input().split()))

box=list(map(int,input().split()))
ops=[]
for i in range(0,k):
    ops.append(list(map(int,input().split())))

BoxOps(box,ops)
