
def rotLeft(a, d):
    ans=[0]*len(a)
    for i in range(d,len(a)):
        ans[i]=a[i%len(a)]
    return ans

a=[1,2,3,4,5]
d=4