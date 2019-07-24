
def plusMinus(a):
    ans=[0,0,0]
    for i in range(len(a)):
        if(a[i]>0):
            ans[0]+=1
            continue
        if(a[i]<0):
            ans[1]+=1
            continue
        ans[2]+=1
    return ans