def compareTriplets(a, b):
    ans=[0,0]
    for  i in range(len(a)):
        if(a[i]>b[i]):
            ans[0]+=1
            continue
        if(a[i]<b[i]):
            ans[1]+=1
            continue
    return ans