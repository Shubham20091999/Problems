
def leftRot(a,d):
    ans=[]
    for i in range(d,d+len(a)):
        ans.append(a[i%len(a)])
    return ans

a=[1,2,3,4,5]
d=4
print(leftRot(a,d))



