
def diagonalDifference(arr):
    ans=0
    for i in range(len(arr)):
        ans+=arr[i][i]-arr[i][len(arr)-i-1]
    return abs(ans)