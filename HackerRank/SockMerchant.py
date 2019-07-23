
def Insert(i,l):
    if(i<len(l)):
        return l
    else:
        l+=[0]*(i-len(l))
        l+=[0]
    return l

def sockMerchant(n, ar):
    dict={}
    for i in range(0,n):
        if ar[i] not in dict:
            dict[ar[i]]=0
        dict[ar[i]]+=1
    ans=0
    for vals in dict.values():
        ans+=vals//2
    return ans

n=9
ar=[10,20,20,10,10,30,50,10,20]
print(sockMerchant(n, ar))
