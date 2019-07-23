


def SumHourGlass(arr,i,j):
        ans=0
        ans+=arr[i][j]+arr[i][j+1]+arr[i][j+2]
        ans+=arr[i+1][j+1]
        ans+=arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
        return ans

def hourglassSum(arr):
    max=-float('inf')
    for i in range(0,4):
        for j in range(0,4):
            val=SumHourGlass(arr,i,j)
            if(val>max):
                max=val
    return max


# arr=[[0,4,3,1],[123,1,123],[8,6,6]]
arr=[]
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

result = hourglassSum(arr)
print(result)
