def birthdayCakeCandles(arr):
    max=0
    num=0
    for i in range(len(arr)):
        if(max<arr[i]):
            max=arr[i]
            num=1
        elif(max==arr[i]):
            num+=1
    return num

print(birthdayCakeCandles([3,2,1,3]))

