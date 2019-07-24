def miniMaxSum(arr):
    arr=sorted(arr)
    ans=0
    for i in range(1,4):
        ans+=arr[i]
    return [ans+arr[0],ans+arr[4]]

a=[1,2,3,4,5]
print(miniMaxSum(a))