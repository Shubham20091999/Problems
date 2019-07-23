

def reverseArray(a):
    ans=[]
    for i in range(len(a)-1,-1,-1):
        ans.append(a[i])
    return ans

reverseArray([1,2,3,4])